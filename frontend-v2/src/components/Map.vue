<template>
  <div>
    <Loading :loading="loading"></Loading>
    <div class="wrapper-status-button">
      <StatusButton v-if="selectedFeatureStatus" :theme="selectedFeatureStatus.theme" :text="selectedFeatureStatus.text" size="large"></StatusButton>
    </div>
    <div id='geocoder' class='geocoder'></div>
    <mapbox
    :accessToken="mapboxToken"
    :map-options="mapOptions"
    :geolocate-control="geolocateControl"
    @map-load="onMapLoaded"
    @geolocate-geolocate="onUserIsGeolocated"></mapbox>
    <!-- Can't bind options to a Vue DataObject because it breaks mapbox -->
  </div>
</template>

<script>
import Loading from "@/components/Loading";
import StatusButton from "@/components/StatusButton";
import Mapbox from "mapbox-gl-vue";
import { Colors, Map, Settings, OpenStatus } from "@/services/constants";
import MapboxGeocoder from "mapbox-gl-geocoder";
import "mapbox-gl-geocoder/dist/mapbox-gl-geocoder.css";
import FeatureService from "@/services/features";
import {
  MapBoxColorExpression,
  MapBoxPatternExpression,
  Patterns
} from "@/utils/mapHelper";
/**
 *  We have to keep the map reference outside vue 'data' object
 *  otherwise the mapbox styles break
 */
let mapRef = {};
let geocoder;
let currentMapId; // store a temp id for current map status (work around since layer removal does not work properly)
export default {
  name: "Map",
  components: {
    Loading,
    Mapbox,
    StatusButton
  },
  data: function() {
    return {
      mapboxToken: Settings.MapBoxToken,
      mapOptions: {
        container: "map",
        style: Map.Defaults.Style,
        center: [Map.Defaults.Longitude, Map.Defaults.Latitude],
        zoom: Map.Defaults.Zoom
      },
      loading: true,
      geolocateControl: {
        show: true,
        position: "top-left",
        options: {
          trackUserLocation: false,
          positionOptions: {
            enableHighAccuracy: true
          }
        }
      },
      selectedFeature: null
    };
  },
  computed: {
    selectedFeatureStatus() {
      if (!this.selectedFeature) return;
      switch (this.selectedFeature.properties.condition) {
        case OpenStatus.Open:
          return {
            theme: "success",
            text: "Permitted"
          };
        case OpenStatus.ClosingSoon:
          return {
            theme: "warning",
            text: "Closing Soon"
          };
        case OpenStatus.Closed:
          return {
            theme: "alert",
            text: "Restricted"
          };
        case OpenStatus.Unknown:
        default:
          return {
            theme: "primary",
            text: "Unknown"
          };
      }
    }
  },
  mounted() {},
  methods: {
    async onMapLoaded(map) {
      try {
        mapRef = map;
        await this.loadMapboxWidgets(mapRef);
        this.$emit("mapLoaded");
        this.loading = false;
      } catch (error) {
        console.error(error);
      }
    },
    onUserIsGeolocated(geolocateControl, pos) {
      this.loadFeatures(pos.coords.latitude, pos.coords.longitude);
    },
    async loadMapboxWidgets(map) {
      // Geocoder (Search Bar)
      // TODO: It'd be nice if we can make this its own controller
      // Limit results to hawaii only
      const bboxHawaii = [-160.3, 16.7, -151.8, 23.3];
      geocoder = new MapboxGeocoder({
        accessToken: Settings.MapBoxToken,
        bbox: bboxHawaii
      });
      geocoder.on("result", ev => {
        const [lon, lat] = ev.result.geometry.coordinates;
        this.loadFeatures(lat, lon);
      });
      document.getElementById("geocoder").appendChild(geocoder.onAdd(mapRef));

      // Load patterns for layers
      await Promise.all([
        new Promise((resolve, reject) => {
          mapRef.loadImage(Patterns.GreenPattern, (err, img) => {
            if (err) reject(err);
            mapRef.addImage("GreenPattern", img);
            resolve();
          });
        }),
        new Promise((resolve, reject) => {
          mapRef.loadImage(Patterns.RedPattern, (err, img) => {
            if (err) reject(err);
            mapRef.addImage("RedPattern", img);
            resolve();
          });
        }),
        new Promise((resolve, reject) => {
          mapRef.loadImage(Patterns.YellowPattern, (err, img) => {
            if (err) reject(err);
            mapRef.addImage("YellowPattern", img);
            resolve();
          });
        })
      ]);
    },
    async loadFeatures(lat, lon) {
      this.loading = true;
      // TODO: Yield features instead of return whole array (since it requires multiple requests)
      const features = await FeatureService.getFeaturesNearBy(lat, lon);
      const source = [];
      for (const f of features) {
        if (!this.$store.state.renderedFeatures[f._id]) {
          const geo = f.geojson;
          geo.properties.condition = await f.getStatus();
          geo.properties.id = f._id;
          source.push(geo);
          // Keep a "set" of all distinct rendered features so we don't render them twice
          this.$store.state.renderedFeatures[f._id] = geo;
        }
      }
      // Create an id for this source and layer (mapbox accepts unique sources and layers only)
      if (mapRef.getSource(currentMapId)) {
        try {
          mapRef.removeSource(currentMapId);
          mapRef.removeLayer(`${currentMapId}-pattern`);
          mapRef.removeLayer(`${currentMapId}-color`);
          mapRef.removeLayer(`${currentMapId}-selected`);
        } catch (error) {
          // swallow
          console.log(error);
        }
      }

      currentMapId = Date.now().toString();
      mapRef.addSource(currentMapId, {
        type: "geojson",
        data: {
          type: "FeatureCollection",
          features: Object.values(this.$store.state.renderedFeatures)
        }
      });

      mapRef.addLayer({
        id: `${currentMapId}-pattern`,
        type: "fill",
        source: currentMapId,
        minzoom: 14,
        paint: {
          "fill-pattern": MapBoxPatternExpression
        },
        filter: ["==", "$type", "Polygon"]
      });

      mapRef.addLayer({
        id: `${currentMapId}-color`,
        type: "fill",
        source: currentMapId,
        paint: {
          "fill-color": MapBoxColorExpression,
          "fill-opacity": 0.3,
          "fill-outline-color": Colors.LayerBorder
        },
        filter: ["!in", "id"]
      });

      mapRef.addLayer({
        id: `${currentMapId}-selected`,
        type: "fill",
        source: currentMapId,
        paint: {
          "fill-color": MapBoxColorExpression,
          "fill-opacity": 0.8
        },
        filter: ["in", "id"]
      });

      const selectFeatureClick = function(e) {
        this.selectedFeature = e.features[0];
        mapRef.setFilter(`${currentMapId}-selected`, [
          "in",
          "id",
          this.selectedFeature.properties.id
        ]);
        mapRef.setFilter(`${currentMapId}-color`, [
          "!in",
          "id",
          this.selectedFeature.properties.id
        ]);
      };
      // Select feature on click
      mapRef.on("click", `${currentMapId}-color`, selectFeatureClick);
      mapRef.on("click", `${currentMapId}-pattern`, selectFeatureClick);
      this.loading = false;
    }
  }
};
</script>

<style lang='css'>
.mapboxgl-ctrl-geocoder {
  min-width: 100%;
  width: 100%;
}

.mapboxgl-ctrl-geocoder input[type="text"] {
  min-width: 100%;
}
</style>

<style scoped>
#map {
  height: calc(100vh);
  width: 100%;
}

#geocoder {
  position: absolute;
  z-index: 1;
  width: 50%;
  left: 50%;
  margin-left: -25%;
  margin-top: 10px;
}

.wrapper-status-button {
  position: absolute;
  bottom: 50px;
  z-index: 1;
  width: 250px;
  max-width: 250px;
  min-width: 250px;
  margin-left: -125px;
  left: 50%;
  text-align: center;
}
</style>

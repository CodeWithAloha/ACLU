<template>
  <div>
    <mapbox
    @map-load="onMapLoaded"
    :accessToken="mapboxToken"
    :map-options="mapOptions"
    :geolocate-control="geolocateControl"></mapbox>
    <!-- Can't bind options to a Vue DataObject because it breaks mapbox -->
  </div>
</template>

<script>
import Mapbox from "mapbox-gl-vue";
import { Map, Settings } from "@/services/constants";
import Geolocation from "@/services/geolocation";
import FeatureService from "@/services/features";
import { log } from 'util';

/**
 *  We have to keep the map reference outside vue 'data' object
 *  otherwise the mapbox styles break
 */
let mapRef = {};
export default {
  name: "Map",
  components: {
    Mapbox
  },
  data: function() {
    return {
      mapboxToken: Settings.MapBoxToken,
      mapOptions: {
        container: "map",
        style: Map.Defaults.Style, // 'mapbox://styles/mapbox/streets-v9',
        center: [
          Map.Defaults.Longitude,
          Map.Defaults.Latitude
        ],
        zoom: Map.Defaults.Zoom
      },
      geolocateControl: {
        show: true,
        position: "top-left",
        options: {
          trackUserLocation: true,
          positionOptions: {
            enableHighAccuracy: true
          }
        }
      }
    };
  },
  methods: {
    onMapLoaded: async function(map) {
      try {
        this.$emit("mapLoaded");
        mapRef = map;
        const pos = await Geolocation.getCurrentPosition();
        await this.centerAtUserLocation(map, pos.coords);
        await this.loadFeatures(pos.coords)
      } catch (error) {
        console.error(error);
      }
    },
    centerAtUserLocation: async function(map, pos) {
      mapRef.flyTo({
        center: [pos.longitude, pos.latitude],
        zoom: 13
      });
    },
    loadFeatures: async function(pos) {
      // TODO: Yield features instead of return whole array
      const features = await FeatureService.getFeaturesNearBy(pos);
      features.forEach(f => this.addFeatureToLayer(f))
      console.log(features);
    },
    addFeatureToLayer(feature){
      mapRef.addLayer({
        id: feature._id,
        type: "fill",
        paint: {
          "fill-color": "#ff0000"
        },
        source: {
          type: "geojson",
          data: feature.geojson
        }
      });
    }
  }
};
</script>

<style scoped>
#map {
  width: 100%;
  height: 100vh;
}
</style>

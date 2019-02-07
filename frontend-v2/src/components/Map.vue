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
import Constants from "@/services/constants";
import Geolocation from "@/services/geolocation";

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
      mapboxToken: Constants.Settings.MapBoxToken,
      mapOptions: {
        container: "map",
        style: Constants.Map.Defaults.Style, // 'mapbox://styles/mapbox/streets-v9',
        center: [
          Constants.Map.Defaults.Longitude,
          Constants.Map.Defaults.Latitude
        ],
        zoom: Constants.Map.Defaults.Zoom
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
      } catch (error) {
        console.log(error);
      }
    },
    centerAtUserLocation: async function(map, pos) {
      mapRef.flyTo({
        center: [pos.longitude, pos.latitude],
        zoom: 13
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

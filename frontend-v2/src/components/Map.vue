<template>
  <div>
    <mapbox
    @map-load="onMapLoaded"
    :accessToken="mapboxToken"
    :map-options="{
      container: 'map',
      style: 'mapbox://styles/mapbox/streets-v9',
      center: [-74.50, 40],
      zoom: 9
    }"></mapbox>
    <!-- Can't bind options to a Vue DataObject because it breaks mapbox -->
  </div>
</template>

<script>
import Mapbox from "mapbox-gl-vue";
import Constants from "@/services/constants";
import Geolocation from "@/services/geolocation";

export default {
  name: "Map",
  components: {
    Mapbox
  },
  data: function() {
    return {
      map: {},
      mapboxToken: process.env.VUE_APP_MAPBOX_TOKEN,
      style: Constants.Map.Defaults.Style,
      centerLon: Constants.Map.Defaults.Longitude,
      centerLat: Constants.Map.Defaults.Latitude,
      zoom: Constants.Map.Defaults.Zoom
    };
  },
  methods: {
    onMapLoaded: async function(map) {
      this.$emit("mapLoaded");
      this.map = map;
      await this.centerAtUserLocation();
    },
    centerAtUserLocation: async function() {
      try {
        // const pos = await Geolocation.getCurrentPosition();
        this.map.flyTo({
          // center: [pos.coords.longitude, pos.coords.latitude],
          zoom: 13
        });
      } catch (error) {
        console.log(error);
      }
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

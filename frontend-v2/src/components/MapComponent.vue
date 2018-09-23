<template>
  <div>
		<Loading :loading="loading"></Loading>
    <mapbox
		@map-load="onMapLoaded"
		:accessToken="mapboxToken"
		:mapOptions="mapOptions"></mapbox>
  </div>
</template>

<script>
import Mapbox from "mapbox-gl-vue";
import Constants from "@/services/constants";

export default {
  name: "MapComponent",
  components: {
    Mapbox
  },
  data: function() {
    console.log(JSON.stringify(Constants));
    return {
      mapboxToken: process.env.VUE_APP_MAPBOX_TOKEN,
      mapOptions: {
        style: "mapbox://styles/mapbox/light-v9",
        center: [
          Constants.Map.Defaults.Longitude,
          Constants.Map.Defaults.Latitude
        ],
        zoom: Constants.Map.Defaults.Zoom
      }
    };
  },
  methods: {
    onMapLoaded: function() {
      this.$emit("mapLoaded");
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

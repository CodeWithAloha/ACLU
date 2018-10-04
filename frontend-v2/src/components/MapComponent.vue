<template>
  <div>
    <mapbox
		:accessToken="mapboxToken"
		:mapOptions="mapOptions"></mapbox>
  </div>
</template>

<script>
import Mapbox from "mapbox-gl-vue";

export default {
  name: "MapComponent",
  components: {
    Mapbox
  },
  data: function() {
    return {
      mapboxToken: process.env.VUE_APP_MAPBOX_TOKEN,
      mapOptions: {
        style: "mapbox://styles/mapbox/light-v9",
        center: [-96, 37.8],
        zoom: 3
      }
    };
  }
};
</script>

<style scoped>
#map {
  width: 100%;
  height: 500px;
}
</style>

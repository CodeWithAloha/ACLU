<template>
  <div>
    <mapbox
		@map-load="onMapLoaded"
		:accessToken="mapboxToken"
		:mapOptions="mapOptions"></mapbox>
  </div>
</template>

<script>
import Mapbox from 'mapbox-gl-vue'
import Constants from '@/services/constants'
import Geolocation from '@/services/geolocation'

export default {
  name: 'Map',
  components: {
    Mapbox
  },
  data: function () {
    return {
			mapRef: null,
      mapboxToken: process.env.VUE_APP_MAPBOX_TOKEN,
      mapOptions: {
        style: 'mapbox://styles/mapbox/light-v9',
        center: [
          Constants.Map.Defaults.Longitude,
          Constants.Map.Defaults.Latitude
        ],
        zoom: Constants.Map.Defaults.Zoom
      }
    }
  },
  methods: {
    onMapLoaded: function (map) {
			this.$emit('mapLoaded')
			this.mapRef = map
		},
		centerOnUserLocation: async function() {
			try {
				const position = await Geolocation.getCurrentPosition()
				// this.$store.commit("locationFound", pos.coords);
				// TODO: store location in use`r session?
				map.flyTo({
					center: [pos.coords.longitude, pos.coords.latitude],
					zoom: 13
				});
			} catch (error) {
				console.log(error)
			}
		}
	}
}
</script>

<style scoped>
#map {
  width: 100%;
  height: 100vh;
}
</style>

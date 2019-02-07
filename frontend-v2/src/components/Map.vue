<template>
  <div>
    <mapbox
    @map-load="onMapLoaded"
    :accessToken="mapboxToken"
    :map-options="mapOptions"></mapbox>
    <!-- Can't bind options to a Vue DataObject because it breaks mapbox -->
  </div>
</template>

<script>
import Mapbox from 'mapbox-gl-vue'
import Constants from '@/services/constants'
import Geolocation from '@/services/geolocation'

/**
 *  We have to keep the map reference outside vue 'data' object
 *  otherwise the mapbox styles break
 */
let mapRef = {}
export default {
  name: 'Map',
  components: {
    Mapbox
  },
  data: function () {
    return {
      mapboxToken: process.env.VUE_APP_MAPBOX_TOKEN,
      mapOptions: {
        container: 'map',
        style: Constants.Map.Defaults.Style, // 'mapbox://styles/mapbox/streets-v9',
        center: [
          Constants.Map.Defaults.Longitude,
          Constants.Map.Defaults.Latitude
        ],
        zoom: Constants.Map.Defaults.Zoom
      }
    }
  },
  methods: {
    onMapLoaded: async function (map) {
      this.$emit('mapLoaded')
      mapRef = map
      await this.centerAtUserLocation(map)
    },
    centerAtUserLocation: async function (map) {
      try {
        const pos = await Geolocation.getCurrentPosition()
        mapRef.flyTo({
          center: [pos.coords.longitude, pos.coords.latitude],
          zoom: 13
        })
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

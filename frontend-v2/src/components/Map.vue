<template>
  <div>
    <Loading v-if="loading"/>
    <div id="geocoder" class="geocoder"></div>
    <mapbox
      :accessToken="mapboxToken"
      :map-options="mapOptions"
      :geolocate-control="geolocateControl"
      @map-load="onMapLoaded"
      @geolocate-geolocate="onUserIsGeolocated"
    ></mapbox>
    <!-- Can't bind options to a Vue DataObject because it breaks mapbox -->
  </div>
</template>

<script>
import Loading from '@/components/Loading'
import Mapbox from 'mapbox-gl-vue'
import { Map, Settings } from '@/services/constants'
import 'mapbox-gl-geocoder/dist/mapbox-gl-geocoder.css'
import { MapboxHandler, MapboxHandlerEvents } from '@/utils/mapboxHandler'

/**
 *  We have to keep the map reference outside vue 'data' object
 *  otherwise the mapbox styles break
 */
let mapRef, mapboxHandler

export default {
  name: 'Map',
  components: {
    Loading,
    Mapbox
  },
  data: function () {
    return {
      mapboxToken: Settings.MapBoxToken,
      mapOptions: {
        container: 'map',
        style: Map.Defaults.Style,
        center: [Map.Defaults.Longitude, Map.Defaults.Latitude],
        zoom: Map.Defaults.Zoom
      },
      loading: true,
      geolocateControl: {
        show: true,
        position: 'top-left',
        options: {
          trackUserLocation: false,
          positionOptions: {
            enableHighAccuracy: true
          }
        }
      }
    }
  },
  computed: {
    splash () {
      return this.$store.state.splash
    }
  },
  watch: {
    splash (newValue, oldValue) {
      // This method must be called after the map is shown after being initially hidden.
      mapRef.resize()
    }
  },
  methods: {
    onLoading () {
      this.loading = true
    },
    onFinishedLoading () {
      this.$store.commit('showSplash')
      this.loading = false
    },
    async onMapLoaded (map) {
      try {
        mapRef = map
        mapboxHandler = new MapboxHandler(map, this.$store)

        // Subscribe to map events
        mapboxHandler.on(MapboxHandlerEvents.MapLoading, this.onLoading)
        mapboxHandler.on(MapboxHandlerEvents.FeaturesLoading, this.onLoading)
        mapboxHandler.on(MapboxHandlerEvents.MapLoaded, this.onFinishedLoading)
        mapboxHandler.on(
          MapboxHandlerEvents.FeaturesLoaded,
          this.onFinishedLoading
        )
        mapboxHandler.on(MapboxHandlerEvents.FeatureSelected, feature => {
          this.$emit('featureSelected', feature)
        })
        await mapboxHandler.loadMapboxWidgets()
      } catch (error) {
        console.error(error)
      }
    },
    async onUserIsGeolocated (geolocateControl, pos) {
      await mapboxHandler.loadFeatures(
        pos.coords.latitude,
        pos.coords.longitude
      )
    }
  }
}
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
</style>

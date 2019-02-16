<template>
  <div>
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
import Mapbox from 'mapbox-gl-vue'
import { Map, Settings } from '@/services/constants'
import Geolocation from '@/services/geolocation'
import MapboxGeocoder from 'mapbox-gl-geocoder'
import 'mapbox-gl-geocoder/dist/mapbox-gl-geocoder.css'
import FeatureService from '@/services/features'
import MapHelper from '@/utils/mapHelper'

/**
 *  We have to keep the map reference outside vue 'data' object
 *  otherwise the mapbox styles break
 */
let mapRef = {}
let geocoder
export default {
  name: 'Map',
  components: {
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
      geolocateControl: {
        show: true,
        position: 'top-left',
        options: {
          trackUserLocation: true,
          positionOptions: {
            enableHighAccuracy: true
          }
        }
      }
    }
  },
  mounted () {},
  methods: {
    async onMapLoaded (map) {
      try {
        mapRef = map
        await this.loadMapboxWidgets(mapRef)
        this.$emit('mapLoaded')
        // TODO: Cleanup unused geolocation
        // const pos = await Geolocation.getCurrentPosition();
        // await this.centerAtUserLocation(map, pos.coords);
        // await this.loadFeatures(pos.coords);
      } catch (error) {
        console.error(error)
      }
    },
    onUserIsGeolocated (geolocateControl, pos) {
      this.loadFeatures(pos.coords.latitude, pos.coords.longitude)
    },
    loadMapboxWidgets (map) {
      // Geocoder (Search Bar)
      // TODO: It'd be nice if we can make this its own controller
      // Limit results to hawaii only
      const bboxHawaii = [-160.3, 16.7, -151.8, 23.3]
      geocoder = new MapboxGeocoder({
        accessToken: Settings.MapBoxToken,
        bbox: bboxHawaii
      })
      geocoder.on('result', ev => {
        const [lon, lat] = ev.result.geometry.coordinates
        this.loadFeatures(lat, lon)
      })
      document.getElementById('geocoder').appendChild(geocoder.onAdd(mapRef))
    },
    async loadFeatures (lat, lon) {
      // TODO: Yield features instead of return whole array
      const features = await FeatureService.getFeaturesNearBy(lat, lon)
      for (const f of features) {
        this.addFeatureToLayer(f)
      }
      // features.forEach(f => )
      // console.log(features);
    },
    async addFeatureToLayer (feature) {
      // if (mapRef.getLayer(feature._id)) {
      //   mapRef.removeLayer(feature._id);
      // }
      try {
        const layer = await MapHelper.getFeatureLayer(feature)
        mapRef.addLayer(layer)
      } catch (error) {
        console.log(`Couldn't add layer for feature ${feature._id}.`)
        console.error(error)
      }
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

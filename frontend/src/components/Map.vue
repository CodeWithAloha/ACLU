<template lang='html'>
  <div class="container">
    <div class='map'></div>
    <!--<div class="icon" v-html="locationIcon" v-if="locationDetermined"></div>-->
    <Nav v-if="locationDetermined"></Nav>
    <bottombar :longitude="this.location.longitude" :latitude="this.location.latitude"></bottombar>
  </div>
</template>

<script>
import Mapbox from 'mapbox-gl'
import { mapState } from 'vuex'
import 'mapbox-gl/dist/mapbox-gl.css'

import MapboxGeocoder from 'mapbox-gl-geocoder'
import 'mapbox-gl-geocoder/dist/mapbox-gl-geocoder.css'

import Axios from 'axios'
import bottombar from './BottomBar.vue'

Mapbox.accessToken = 'pk.eyJ1IjoicnVzc2VsbHZlYTIiLCJhIjoiY2lmZzVrNWJkOWV2cnNlbTdza2thcGozNSJ9.zw6CcZLxP6lq0x-xfwp6uA'

export default {
  data: function () {
    return {
      location: {
        longitude: 0,
        latitude: 0
      }
    }
  },
  computed: mapState({
    locationDetermined: {}
  }),
  mounted () {
    const map = new Mapbox.Map({
      container: document.querySelector('.map'),
      style: 'mapbox://styles/mapbox/streets-v9',
      center: [-158.000072, 21.441922],
      zoom: 9
    })

    var geocoder = new MapboxGeocoder({
      accessToken: Mapbox.accessToken
    })
    map.addControl(geocoder)

    // on geocoder retrieve
    geocoder.on('result', (ev) => {
      // clear map of layers
      // this.removeAllLayers(map)
      this.setAllLayers(ev.result.geometry.coordinates[0], ev.result.geometry.coordinates[1], map)
    })

    map.on('load', () => {
      /* change this to zoom in on bounds of rule */
      if ('geolocation' in navigator) {
        navigator.geolocation.getCurrentPosition(pos => {
          this.$store.commit('locationFound', pos.coords)
          map.flyTo({
            center: [pos.coords.longitude, pos.coords.latitude],
            zoom: 13
          })
          this.setAllLayers(pos.coords.longitude, pos.coords.latitude, map)
          this.location.longitude = pos.coords.longitude
          this.location.latitude = pos.coords.latitude
          console.log(this.location.longitude)
        }, err => {
          console.log(err)
          alert('We can\'t seem to determine your position')
        })
      }
    })
  },
  methods: {
    setLayers (data, map) {
      for (var i = 0; i < data._items.length; i++) {
        var geojson = data._items[i].geojson
        var id = data._items[i]._id

        map.addLayer({
          id: id,
          type: 'fill',
          paint: {
            'fill-color': '#ff0000'
          },
          source: {
            type: 'geojson',
            data: geojson
          }
        })
      }
    },
    setAllLayers (lng, lat, map) {
      var url = 'http://localhost:5000/features/?where={"geojson.geometry":{"$near":{"$geometry":{"type":"Point", "coordinates":[' + lng + ', ' + lat + ']}, "$maxDistance": 25000}}}'
      this.getLayerData(url, map)
    },
    getLayerData (href, map) {
      return Axios.get(href)
        .then(response => {
          this.setLayers(response.data, map)
          console.log('asdf')
          if (response.data._links.next) {
            var url = 'http://localhost:5000/' + response.data._links.next.href
            return this.getLayerData(url, map)
          }
        })
    },
    removeAllLayers (map) {
      map.eachLayer(function (layer) {
        map.removeLayer(layer)
      })
    }
  },
  components: { bottombar }
}
</script>

<style lang='css' scoped>
  .map {
    height: 100vh;
    width: 100%;
  }

  .icon {
    position: fixed;
    width: 2rem;
    top: 50%;
    left: 50%;
    transform: translate(-50% -50%);
    z-index: 9;
  }

  .icon > svg {
    width: 2rem;
    height: 2rem;
    fill: #ff0000;
  }
</style>

<template lang='html'>
  <div class="container">
    <div class='map'></div>
    <div class="icon" v-html="locationIcon" v-if="locationDetermined"></div>
    <Nav v-if="locationDetermined"></Nav>
  </div>
</template>

<script>
/* eslint no-new:0 */
import Mapbox from 'mapbox-gl'
import { mapState } from 'vuex'
import 'mapbox-gl/dist/mapbox-gl.css'
// const locationIcon = require('../assets/location.svg')
// import Vue from 'vue'

Mapbox.accessToken = 'pk.eyJ1IjoicnVzc2VsbHZlYTIiLCJhIjoiY2lmZzVrNWJkOWV2cnNlbTdza2thcGozNSJ9.zw6CcZLxP6lq0x-xfwp6uA'

export default {
  data: function () {
    return {}
    //   locationIcon
    // }
  },
  computed: mapState({
    locationDetermined: 'locationDetermined'
  }),
  mounted () {
    const map = new Mapbox.Map({
      container: document.querySelector('.map'),
      style: 'mapbox://styles/mapbox/streets-v9',
      center: [-158.000072, 21.441922],
      zoom: 9
    })
    map.on('load', () => {
      import('./parks.geojson').then(data => {
        map.addLayer({
          id: 'parks',
          type: 'fill',
          paint: {
            'fill-color': '#ff0000'
          },
          source: {
            type: 'geojson',
            data
          }
        })

        if ('geolocation' in navigator) {
          navigator.geolocation.getCurrentPosition(pos => {
            this.$store.commit('locationFound', pos.coords)
            map.flyTo({
              center: [pos.coords.longitude, pos.coords.latitude],
              zoom: 13
            })
          }, err => {
            console.log(err)
            alert('We can\'t seem to determine your position')
          })
        }
      })

      map.on('click', 'parks', e => {
        const bounds = new Mapbox.LngLatBounds()
        e.features[0].geometry.coordinates.forEach(ll => {
          if (typeof ll === 'object') {
            return
          }
          bounds.extend(ll)
        })
        const center = bounds.getCenter()

        new Mapbox.Popup()
          .setLngLat(center)
          .setHTML(e.features[0].properties.name)
          .addTo(map)
      })
    })
  },
  methods: {},
  components: {}
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

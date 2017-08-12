<template lang='html'>
  <div id="example">
  <md-whiteframe md-elevation="2">
    <md-toolbar>
      <h1 class="md-title">Hello!</h1>
    </md-toolbar>
  </md-whiteframe>
  
  <md-layout md-gutter class="main-content">
    <md-layout md-flex="35" class="form-content">
      <md-layout md-column>
        <md-input-container>
          <label for="name">Name</label>
          <md-input v-model="name" id="name" name="name"></md-input>
        </md-input-container>

        <md-input-container>
          <label for="email">Email</label>
          <md-input v-model="email" id="email" name="email"></md-input>
        </md-input-container>
      </md-layout>
    </md-layout>
    
    <md-layout md-flex="65" class="page-content map">      
    </md-layout>   
  </md-layout>
</div>
</template>

<script>
/* eslint no-new:0 */
import Mapbox from 'mapbox-gl'
import { mapState } from 'vuex'
import 'mapbox-gl/dist/mapbox-gl.css'
// import geocode and styles
import MapboxGeocoder from 'mapbox-gl-geocoder'
import 'mapbox-gl-geocoder/dist/mapbox-gl-geocoder.css'
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
    // add geocode text field
    map.addControl(new MapboxGeocoder({
      accessToken: Mapbox.accessToken
    }))
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
    })
  },
  methods: {},
  components: {}
}
</script>

<style lang='css' scoped>
  .map {
    height: 100vh;
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

  .container {
    padding: 15px;
    width: inherit;
  }

  .md-input-container {
    width: 100%;
  }

  .md-column {
    padding: 10px;
  }
</style>

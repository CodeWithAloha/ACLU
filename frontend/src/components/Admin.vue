<template lang='html'>
  <div id="example">
  <md-whiteframe md-elevation="2">
    <md-toolbar>
      <h1 class="md-title">Add New Asset</h1>
    </md-toolbar>
  </md-whiteframe>
  
  <md-layout md-gutter class="main-content">
    <md-layout md-flex="35" class="form-content">
      <md-layout md-column>


        <md-input-container>
          <label for="name">Organization Name</label>
          <md-input v-model="name" id="organization_name" name="organization_name"></md-input>
        </md-input-container>

        <md-input-container>
          <label for="email">Name</label>
          <md-input v-model="email" id="name" name="name"></md-input>
        </md-input-container>

        <label for="email">Time Of Day Start</label>
        <el-time-select
          v-model="time_start"
          :picker-options="{
            start: '08:30',
            step: '00:15',
            end: '18:30'
          }"
          placeholder="Select time">
        </el-time-select>

        <label for="email">Time Of Day End</label>
        <el-time-select
          v-model="time_end"
          :picker-options="{
            start: '08:30',
            step: '00:15',
            end: '18:30'
          }"
          placeholder="Select time">
        </el-time-select>

          <label for="email">Effecteive Datetime Start</label>
          <el-date-picker
            v-model="datetime_start"
            type="datetime"
            placeholder="Select date and time">
          </el-date-picker>

          <label for="email">Effecteive Datetime End</label>
          <el-date-picker
            v-model="datetime_end"
            type="datetime"
            placeholder="Select date and time">
          </el-date-picker>

        <md-input-container>
          <label for="users=">Day Of Restriction</label>
          <md-select name="option" id="option" multiple v-model="items">
            <md-option v-for="option in options"
              :key="option"
              :value="option">
              {{ option.name }}
            </md-option>
          </md-select>
        </md-input-container>

        <md-input-container>
          <label for="email">Holiday Restriction</label>
          <md-input v-model="email" id="name" name="name"></md-input>
        </md-input-container>

        <md-input-container>
          <label for="email">Ownership</label>
          <md-input v-model="email" id="name" name="name"></md-input>
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
import MapboxDraw from '@mapbox/mapbox-gl-draw/dist/mapbox-gl-draw'
import '@mapbox/mapbox-gl-draw/dist/mapbox-gl-draw.css'

Mapbox.accessToken = 'pk.eyJ1IjoicnVzc2VsbHZlYTIiLCJhIjoiY2lmZzVrNWJkOWV2cnNlbTdza2thcGozNSJ9.zw6CcZLxP6lq0x-xfwp6uA'

export default {
  data: function () {
    return {
      time_start: '',
      time_end: '',
      datetime_start: '',
      datetime_end: '',
      options: [
        { id: 1, name: 'Monday' },
        { id: 2, name: 'Tuesday' },
        { id: 3, name: 'Wednesday' },
        { id: 4, name: 'Thursday' },
        { id: 5, name: 'Friday' },
        { id: 6, name: 'Saturday' },
        { id: 7, name: 'Sunday' }
      ],
      items: []
    }
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

    map.addControl(new MapboxDraw())
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
    height: 100;
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

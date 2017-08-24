<template>
  <div class="container">
    <md-toolbar>
      <md-button class="md-icon-button">
        <md-icon>menu</md-icon>
      </md-button>

      <h2 class="md-title" style="flex: 1">Rule List</h2>
    </md-toolbar>
    <div class="main-content">
      <div class="rule-name">
        <h2>{{name}}</h2>
        <!--
        <div class="status-sign" align=right>
          <md-avatar class="md-avatar-icon md-large">
            <img v-if="rule.status == 0" src="../assets/greenbox.png" alt="Avatar">
            <img v-if="rule.status == 1" src="../assets/greenbox.png" alt="Avatar">
            <img v-if="rule.status == 2" src="../assets/greenbox.png" alt="Avatar">
          </md-avatar>
        </div>
        -->
      </div>
      <!--
      <div class="bill-text">
        <div class="title">
            <h4>Bill Text</h4>
          </div>
          <div class="description">
            <p>{{ rule.description }}</p>
            <div v-for="(time, index) in rule.time">
              ({{index + 1}}) <b>{{time.name}}</b> {{time.description}}
            </div>
          </div>
        </div>
        <div class="ordiance">
          <div class="title">
            <h4>Ordiance</h4>
          </div>
          <div class="description">
            <div class="map"></div>
          </div>
        </div>
      </div
        -->
    </div>
    <md-bottom-bar>
      <md-bottom-bar-item md-icon="subject">Organization</md-bottom-bar-item>
      <md-bottom-bar-item md-icon="subject">Rules</md-bottom-bar-item>
    </md-bottom-bar>
  </div>

</template>

<script>
/* eslint no-new:0 */
import Mapbox from 'mapbox-gl'
import 'mapbox-gl/dist/mapbox-gl.css'

import Axios from 'axios'
// const locationIcon = require('../assets/location.svg')
// import Vue from 'vue'

Mapbox.accessToken = 'pk.eyJ1IjoicnVzc2VsbHZlYTIiLCJhIjoiY2lmZzVrNWJkOWV2cnNlbTdza2thcGozNSJ9.zw6CcZLxP6lq0x-xfwp6uA'

export default {
  name: 'Rule',
  data () {
    return {
      // static rules *remove when api is created
      name: ''
    }
  },
  methods: {
    getRule: function (id) {
      var url = 'http://localhost:5000/features/' + this.$route.params.ruleId
      return Axios.get(url)
        .then(function (response) {
          return response.data
        })
    }
  },
  mounted () {
    this.getRule(this.$route.params.id)
      .then(data => {
        console.log(data)
        this.name = data.name
        console.log(this.name)
      })
    // use API to grab rule and set it here with this.$route.params.ruleId

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
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .bill-text {
    display: inline-block;
  }
  .main-content {
    position: fixed;
    top: 64px;
    bottom: 54px;
    padding-left: 10%;
    padding-right: 10%;
    overflow: scroll;
  }
  .title {
    vertical-align: top;
    display: inline-block;
    width: 25%;
  }
  .title > h4 {
    margin: 0px;
  }

  .description {
    float: right;
    vertical-align: top;
    display: inline-block;
    width: 75%;
  }
  .description > p {
    margin: 0px;
    padding-bottom: 20px;
  }
  .rule-name > h2 {
    float: left;
    display: inline-block;
    width: 75%;
  }
  .status-sign {
    display: inline-block;
    width: 25%;
    padding-right: 20px;
  }
  .rule-name {
    padding-top: 20px;
    padding-bottom: 20px;
  }
  .bill-text {
    padding-bottom: 20px;
  }
  .map {
    height: 200px;
    width: 100%;
  }
  .md-bottom-bar {
    position: fixed;
    bottom: 0;
    z-index: 4
  }

</style>

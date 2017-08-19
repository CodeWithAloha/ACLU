<template>
  <div class="container">
    <div class="main-content">
      <div class="rule-name">
        <h2>{{rule.name}}</h2>
        <div class="status-sign">
          <md-avatar class="md-avatar-icon md-large">
            <img v-if="rule.status == 0" src="../assets/greenbox.png" alt="Avatar">
            <img v-if="rule.status == 1" src="../assets/greenbox.png" alt="Avatar">
            <img v-if="rule.status == 2" src="../assets/greenbox.png" alt="Avatar">
          </md-avatar>
        </div>
      </div>
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
    </div>
  </div>

</template>

<script>
/* eslint no-new:0 */
import Mapbox from 'mapbox-gl'
import 'mapbox-gl/dist/mapbox-gl.css'
// const locationIcon = require('../assets/location.svg')
// import Vue from 'vue'

Mapbox.accessToken = 'pk.eyJ1IjoicnVzc2VsbHZlYTIiLCJhIjoiY2lmZzVrNWJkOWV2cnNlbTdza2thcGozNSJ9.zw6CcZLxP6lq0x-xfwp6uA'

export default {
  name: 'Rule',
  data () {
    return {
      // static rules *remove when api is created
      rule: {
        name: 'Sit Lie Ban',
        status: 0,
        description: 'No person shall sit or lie on a public mall, or on a tarp, towel, sheet, blanket,' +
          'sleeping bag, bedding, planter, chair, bench, or any other object or material' +
          'placed upon a public mall during the following hours:',
        time: [
          {
            name: 'Fort Street Mall',
            description: 'Monday to Sunday from 5:00 am. to 7:00 p.m.'
          }, {
            name: 'Kekaulike Mall',
            description: 'Monday to Friday from 5:00 a.m. to 7:00 p.m.'
          }, {
            name: 'Sun Yat Sen Mall',
            description: 'Monday to Friday from 5:00 a.m. to 7:00 p.m.'
          }, {
            name: 'Union Mall',
            description: 'Monday to Friday from 5:00 a.m. to 7:00 p.m.'
          }
        ]
      }
    }
  },
  mounted () {
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
    padding-left: 15%;
    padding-right: 15%;
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
    vertical-align: top;
    display: inline-block;
    width: 70%;
  }
  .description > p {
    margin: 0px;
    padding-bottom: 20px;
  }
  .rule-name > h2 {
    display: inline-block;
    width: 75%;
  }
  .status-sign {
    display: inline-block;
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

</style>

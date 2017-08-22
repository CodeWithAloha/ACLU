<template lang='html'>
  <div class="container">
    <div class='map'></div>
    <!--<div class="icon" v-html="locationIcon" v-if="locationDetermined"></div>-->
    <Nav v-if="locationDetermined"></Nav>
  </div>
</template>

<script>
import Mapbox from 'mapbox-gl'
import { mapState } from 'vuex'
import 'mapbox-gl/dist/mapbox-gl.css'

import Axios from 'axios'

Mapbox.accessToken = 'pk.eyJ1IjoicnVzc2VsbHZlYTIiLCJhIjoiY2lmZzVrNWJkOWV2cnNlbTdza2thcGozNSJ9.zw6CcZLxP6lq0x-xfwp6uA'

export default {
  data: function () {
    return {
      featureList: 'asdf'
    }
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
      // this.getDataByLocation(-157.823231, 21.269304, 250).then(data => {
      this.getDataAll().then(data => {
        console.log('ids: ' + data._items.length)
        for (var i = 0; i < data._items.length; i++) {
          console.log(data._items[i])
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
      })
    })
    /* change this to zoom in on bounds of rule */
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
  },
  methods: {
    getDataByLocation (lng, lat, maxDistance) {
      return Axios.get('http://localhost:5000/features/?where={"geojson.geometry":{"$near":{"$geometry":{"type":"Point", "coordinates":[' + lng + ', ' + lat + ']}, "$maxDistance": ' + maxDistance + '}}}')
      .then(response => {
        this.response = response.data
        return this.response
      })
    },
    getDataAll () {
      return Axios.get('http://localhost:5000/features')
        .then(response => {
          this.response = response.data
          return this.response
        })
    }
  },
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

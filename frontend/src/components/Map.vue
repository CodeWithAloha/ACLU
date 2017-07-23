<template lang='html'>
  <div class='map'></div>
</template>

<script>
/* eslint no-new:0 */
import Mapbox from 'mapbox-gl'
import 'mapbox-gl/dist/mapbox-gl.css'
// import Vue from 'vue'

Mapbox.accessToken = 'pk.eyJ1IjoicnVzc2VsbHZlYTIiLCJhIjoiY2lmZzVrNWJkOWV2cnNlbTdza2thcGozNSJ9.zw6CcZLxP6lq0x-xfwp6uA'

export default {
  data: function () {
    return {
      world: 'World'
    }
  },
  mounted () {
    const map = new Mapbox.Map({
      container: document.querySelector('.map'),
      style: 'mapbox://styles/mapbox/streets-v9',
      center: [-158.000072, 21.441922],
      zoom: 9
    })

    import('./parks.geojson').then(data => {
      map.addLayer({
        id: 'parks',
        type: 'fill',
        source: {
          type: 'geojson',
          data
        }
      })

      map.on('click', 'parks', e => {
        const bounds = new Mapbox.LngLatBounds()
        e.features[0].geometry.coordinates.forEach(ll => {
        })
        const center = bounds.getCenter()

        new Mapbox.Popup()
          .setLngLat(center)
          .setHTML(e.features[0].properties.name)
          .addTo(map)
      })
    })
  },
  methods: {
    foo () {
      console.log('click')
    }
  },
  components: {}
}
</script>

<style lang='css'>
  #app {
    height: 100%;
    width: 100%;
  }

  .map {
    height: 100vh;
    width: 100%;
  }
</style>

<style ></style>

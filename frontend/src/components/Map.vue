<template lang='html'>
  <div class="container">
    <topbar name="Map"></topbar>
    <div class='map'></div>
    <div>
      <md-layout md-gutter="8">
        <md-layout class="rules" md-flex-xsmall="100" md-flex-small="50" md-flex-medium="50">
          {{ rules.length }} rules
        </md-layout>

        <md-layout md-flex-xsmall="100" md-flex-small="50" md-flex-medium="50">
          <div class="warning-description">
            <div class="description-item red" :class="{'-active': rules.length > 0}"></div>
            <div class="description-item yellow"></div>
            <div class="description-item green" :class="{'-active': rules.length == 0}"></div>
          </div>
        </md-layout>
      </md-layout>

    </div>
    <Nav v-if="locationDetermined"></Nav>
    <bottombar :longitude="this.location.longitude" :latitude="this.location.latitude"></bottombar>
  </div>
</template>

<script>
import Mapbox from "mapbox-gl";
import { mapState } from "vuex";
import "mapbox-gl/dist/mapbox-gl.css";

import Axios from "axios";
import bottombar from "./BottomBar.vue";
import topbar from "./TopBar.vue";

// import geocode and styles
import MapboxGeocoder from "mapbox-gl-geocoder";
import "mapbox-gl-geocoder/dist/mapbox-gl-geocoder.css";

Mapbox.accessToken =
  "pk.eyJ1IjoicnVzc2VsbHZlYTIiLCJhIjoiY2lmZzVrNWJkOWV2cnNlbTdza2thcGozNSJ9.zw6CcZLxP6lq0x-xfwp6uA";

export default {
  data() {
    return {
      location: {
        longitude: 0,
        latitude: 0
      }
    };
  },
  computed: mapState({
    locationDetermined: state => state.locationDetermined,
    rules: state => state.rules
  }),
  mounted() {
    const map = new Mapbox.Map({
      container: document.querySelector(".map"),
      style: "mapbox://styles/mapbox/streets-v9",
      center: [-158.000072, 21.441922],
      zoom: 9
    });

    var geocoder = new MapboxGeocoder({
      accessToken: Mapbox.accessToken
    });
    map.addControl(geocoder);

    // on geocoder retrieve
    geocoder.on("result", ev => {
      // clear map of layers
      // this.removeAllLayers(map)
      this.setAllLayers(
        ev.result.geometry.coordinates[0],
        ev.result.geometry.coordinates[1],
        map
      );
      this.location.longitude = ev.result.geometry.coordinates[0];
      this.location.latitude = ev.result.geometry.coordinates[1];
    });

    map.on("load", () => {
      /* change this to zoom in on bounds of rule */
      if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(
          pos => {
            this.$store.commit("locationFound", pos.coords);
            map.flyTo({
              center: [pos.coords.longitude, pos.coords.latitude],
              zoom: 13
            });
            this.setAllLayers(pos.coords.longitude, pos.coords.latitude, map);
            this.location.longitude = pos.coords.longitude;
            this.location.latitude = pos.coords.latitude;
          },
          err => {
            console.log(err);
            alert("We can't seem to determine your position");
          }
        );
      }
    });
  },
  methods: {
    setLayers(data, map) {
      /**
       * TODO: check current hours
       */
      const newRules = data._items.map(rule => {
        const { geojson, _id } = rule;
        const id = _id;
        if (!map.getLayer(id)) {
          map.addLayer({
            id,
            type: "fill",
            paint: {
              "fill-color": "#FF4136"
            },
            source: {
              type: "geojson",
              data: geojson
            }
          });
        }
        return rule;
      });
      this.$store.commit("updateRules", newRules);
    },
    setAllLayers(lng, lat, map) {
      var url =
        'http://localhost:50050/features/?where={"geojson.geometry":{"$near":{"$geometry":{"type":"Point", "coordinates":[' +
        lng +
        ", " +
        lat +
        ']}, "$maxDistance": 50}}}';
      this.getLayerData(url, map);
    },
    /**
     * @argument 
     */
    getLayerData(href, map) {
      return Axios.get(href).then(response => {
        this.setLayers(response.data, map);
        if (response.data._items) {
          // parse the hours
          console.log(response.data._items);
        }
        if (response.data._links.next) {
          var url = "http://localhost:50050/" + response.data._links.next.href;
          return this.getLayerData(url, map);
        }
      });
    }
  },
  components: { bottombar, topbar }
};
</script>

<style lang='css' scoped>
.warning-description {
  width: 100%;
  height: 60px;
  text-align: center;
}

.warning-description > div {
  display: inline-block;
  width: 25px;
  height: 25px;
  border-radius: 50%;
}

.red {
  background-color: var(--red);
}

.yellow {
  background-color: var(--yellow);
}

.green {
  background-color: var(--green);
}

.map {
  height: 65vh;
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

.rules {
  text-align: center;
  justify-content: center;
  padding: 10px 0;
}

.icon > svg {
  width: 2rem;
  height: 2rem;
  fill: var(--red);
}

.description-item {
  opacity: 0.5;
}

.description-item.-active {
  opacity: 1;
}
</style>

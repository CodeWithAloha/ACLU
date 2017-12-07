<template lang='html'>
  <div class="container">
    <topbar name="Map" :back-button="false"></topbar>
    <div class='map'></div>
    <div v-if="locationDetermined">
      <md-layout style="position: absolute; bottom: 0; left: 0; right: 0; padding-bottom: 1rem;">
        <md-button @click="showRuleList" :style="{background: buttonColor, color: 'white'}" class="md-raised" style="width: 75%; margin-left: auto; margin-right: auto;">Restrictions</md-button>
      </md-layout>
    </div>
  </div>
</template>

<script>
import Mapbox from "mapbox-gl";
import { mapState } from "vuex";
import "mapbox-gl/dist/mapbox-gl.css";

import Axios from "axios";
import topbar from "./TopBar.vue";

// import geocode and styles
import MapboxGeocoder from "mapbox-gl-geocoder";
import "mapbox-gl-geocoder/dist/mapbox-gl-geocoder.css";

Mapbox.accessToken =
  "pk.eyJ1IjoicnVzc2VsbHZlYTIiLCJhIjoiY2lmZzVrNWJkOWV2cnNlbTdza2thcGozNSJ9.zw6CcZLxP6lq0x-xfwp6uA";

export default {
  computed: mapState({
    location: state => state.location,
    locationDetermined: state => state.locationDetermined,
    userValid: state => state.userValid,
    rules: state => state.rules,
    buttonColor: state => (state.userValid > 0 ? "#ff4136" : "#2ecc40")
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
      const now = new Date();
      const newRules = data._items.map(rule => {
        const { geojson, _id } = rule;
        const hoursStart = rule.restrictions.hours_start;
        const hoursEnd = rule.restrictions.hours_end;
        const currentTime = now.getHours() * 100 + now.getMinutes(); // format time as 2459
        let isOpen, fillColor;

        if (hoursStart && hoursEnd) {
          isOpen = currentTime > hoursStart && currentTime < hoursEnd;
          rule.isValid = isOpen;
          fillColor = isOpen ? "#2ecc40" : "#ff4136";
        } else {
          isOpen = true;
          rule.isValid = true;
          fillColor = "#ff4136";
        }

        const id = _id;
        if (!map.getLayer(id)) {
          map.addLayer({
            id,
            type: "fill",
            paint: {
              "fill-color": fillColor
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
    showRuleList() {
      this.$router.push({
        name: "RuleList",
        params: {
          lat: this.location.latitude,
          lng: this.location.longitude
        }
      });
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
        if (response.data._links.next) {
          var url = "http://localhost:50050/" + response.data._links.next.href;
          return this.getLayerData(url, map);
        }
      });
    }
  },
  components: { topbar }
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
  height: calc(100vh - 64px);
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

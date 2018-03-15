<template lang='html'>
  <div class="container">
    <div class='map'></div>
    <div id='navbar' class='navbar'>
      <div id='geocoder' class='geocoder'></div>
      <div id='my_location'>
        <i class="material-icons">my_location</i>
      </div>
    </div>
    <div>
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
import TopBar from "./TopBar.vue";

// import geocode and styles
import MapboxGeocoder from "mapbox-gl-geocoder";
import "mapbox-gl-geocoder/dist/mapbox-gl-geocoder.css";
import * as turf from "@turf/turf";

Mapbox.accessToken =
  "pk.eyJ1IjoicnVzc2VsbHZlYTIiLCJhIjoiY2lmZzVrNWJkOWV2cnNlbTdza2thcGozNSJ9.zw6CcZLxP6lq0x-xfwp6uA";

export default {
  components: { TopBar },
  data() {
    return {
      maxDistance: 200,
      FeatureFactory: new FeatureFactory()
    };
  },
  computed: mapState({
    location: state => state.location,
    locationDetermined: state => state.locationDetermined,
    userValid: state => state.userValid,
    rules: state => state.rules,
    buttonColor: state =>
      state.userValid > 0 ? "var(--maroon)" : "var(--olive"
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

    document.getElementById('geocoder').appendChild(geocoder.onAdd(map));

    // on geocoder retrieve
    geocoder.on("result", ev => {
      // clear map of layers
      this.removeAllLayers(map);
      this.setAllLayers(
        ev.result.geometry.coordinates[0],
        ev.result.geometry.coordinates[1],
        map
      );

      location.longitude = ev.result.geometry.coordinates[0];
      location.latitude = ev.result.geometry.coordinates[1];

      map.getSource("single-point").setData(ev.result.geometry);
    });

    /**
     *  Calculates the max distance for queries
     */

    map.on("load", () => {
      map.addSource("single-point", {
        type: "geojson",
        data: {
          type: "FeatureCollection",
          features: []
        }
      });

      // Where the user is located
      map.addLayer({
        id: "point",
        source: "single-point",
        type: "circle",
        paint: {
          "circle-radius": 10,
          "circle-color": "#007cbf"
        }
      });

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
    setLayers(features, map) {
      const now = new Date();
      let trackLayer = null;
      const promises = features.map(feature => {
        const id = feature._id;
        trackLayer = id;
        return feature.getRestrictionState().then(restrictionState => {
          if (!map.getLayer(id)) {
            map.addLayer({
              id,
              type: "fill",
              paint: {
                "fill-color": restrictionState.color
              },
              source: {
                type: "geojson",
                data: feature.geojson
              }
            });
          }
        });
      });
      Promise.all(promises).then(features => {
        if (trackLayer && map.getLayer("point")) {
          // set the user marker above the new layers
          map.removeLayer("point");
          map.addLayer({
            id: "point",
            source: "single-point",
            type: "circle",
            paint: {
              "circle-radius": 10,
              "circle-color": "#007cbf"
            }
          });
        }
        // TODO change this (by pipe)
        this.$store.commit("updateRules", features);
      });
    },

    showRuleList() {
      this.$router.push({
        name: "RuleList",
        params: {
          lat: location.latitude,
          lng: location.longitude
        }
      });
    },
    setAllLayers(lng, lat, map) {
      var url =
        'https://api.aclu.codeforhawaii.org/features/?where={"geojson.geometry":{"$near":{"$geometry":{"type":"Point", "coordinates":[' +
        lng +
        ", " +
        lat +
        ']}, "$maxDistance": ' +
        this.maxDistance +
        "}}}";
      this.getLayerData(url, map);
    },
    getLayerData(href, map) {
      return Axios.get(href).then(response => {
        const features = response.data._items.map(item =>
          this.FeatureFactory.createFeature(item)
        );
        this.setLayers(features, map);
        if (response.data._links.next) {
          var url =
            "https://api.aclu.codeforhawaii.org/" +
            response.data._links.next.href;
          return this.getLayerData(url, map);
        }
      });
    },
    removeAllLayers(map) {
      // TODO: Need to fix this  here
      //   map.eachLayer(function (layer) {
      //     map.removeLayer(layer)
      //   })
    }
  }
};
const FeatureTypes = {
  Park: "PARK",
  Tmk: "TMK"
};
const RestrictionStateType = {
  Valid: "VALID",
  Invalid: "INVALID",
  Warning: "WARNING"
};
class RestrictionState {
  constructor(state, description) {
    this.state = state;
    this.color = "#000000";

    switch (this.state) {
      default:
      case RestrictionStateType.Valid:
        this.color = "#2ecc40";
        break;
      case RestrictionStateType.Invalid:
        this.color = "#ff4136";
        break;
      case RestrictionStateType.Warning:
        this.color = "YELLOW";
        break;
    }
  }
}

class FeatureFactory {
  constructor() {}

  createFeature(feature) {
    switch (feature.type.toUpperCase()) {
      case FeatureTypes.Park:
        return new ParkFeature(feature);
      case FeatureTypes.Tmk:
        return new TmkFeature(feature);
      default:
        console.log("Unknown feature type: " + feature.type);
        break;
    }
  }
}
class ParkFeature {
  constructor(feature) {
    // Take all properties from feature
    for (var property in feature) {
      if (!feature.hasOwnProperty(property)) continue;

      this[property] = feature[property];
    }
  }

  getRestrictionState() {
    const href =
      'https://api.aclu.codeforhawaii.org/feature_park_restrictions/?where={"feature_id":"###FEATURE_ID###"}';
    return Axios.get(href.replace("###FEATURE_ID###", this._id))
      .then(response => {
        console.log(response);
        const restrictions = response.data._items[0].restrictions;
        const currentTime = now.getHours() * 100 + now.getMinutes(); // format time as 2359
        if (restrictions.hours_start && restrictions.hours_end) {
          return new RestrictionState(
            RestrictionStateType.Invalid,
            "LOREM IPSUM"
          );
        } else {
          return new RestrictionState(
            RestrictionStateType.Valid,
            "LOREM IPSUM"
          );
        }
      })
      .catch(err => {
        console.log("Unable to parse restrictions for feature: " + this._id);
        return new RestrictionState(
            RestrictionStateType.Valid,
            "LOREM IPSUM"
          );
      });
  }
}
class TmkFeature {
  constructor(feature) {
    // Take all properties from feature
    for (var property in feature) {
      if (!feature.hasOwnProperty(property)) continue;

      this[property] = feature[property];
    }
  }

  getRestrictionState() {
    return Promise.resolve(
      new RestrictionState(RestrictionStateType.Invalid, "LOREM IPSUM")
    );
  }
}
</script>

<style lang='css'>
#geocoder .mapboxgl-ctrl-geocoder { 
  min-width:100%;
  width:100%;
}

#geocoder .mapboxgl-ctrl-geocoder input[type=text] {
  min-width:100%; 
}
</style>

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
  height: calc(100vh);
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

.navbar {
  position:absolute;
  z-index:1;
  width:98%;
  left:50%;
  margin-left:-49%;
  top:20px;
}

#geocoder {
  width:95%;
  float:left;
  margin-right:.5em;
}

#my_location {
  float:left;
  background-color:white;
  border:1px solid #666;
  padding:.275em;
  vertical-align:middle;
}

</style>

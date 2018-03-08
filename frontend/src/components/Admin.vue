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


        <label for="email">Organization Name</label>
        <el-input placeholder="Please input" v-model="organization_name"></el-input>

        <label for="email">Name</label>
        <el-input placeholder="Please input" v-model="name"></el-input>

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

        <label for="email">Effective Datetime Start</label>
        <el-date-picker
          v-model="datetime_start"
          type="datetime"
          placeholder="Select date and time">
        </el-date-picker>

        <label for="email">Effective Datetime End</label>
        <el-date-picker
          v-model="datetime_end"
          type="datetime"
          placeholder="Select date and time">
        </el-date-picker>

        <label for="email">Day Of Week Restrictions</label>
        <el-select v-model="value5" multiple placeholder="Select">
          <el-option
            v-for="item in day_options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>

        <label for="email">Holiday Restrictions</label>
        <el-select v-model="holiday_restrictions" placeholder="Select">
          <el-option
            v-for="item in holiday_restriction_options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>

        <label for="email">Ownership</label>
        <el-select v-model="ownership" placeholder="Select">
          <el-option
            v-for="item in ownership_options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>

        <button v-on:click="submit">Submit</button>

      </md-layout>
    </md-layout>
    
    <md-layout md-flex="65" class="page-content map">      
    </md-layout>   
  </md-layout>
</div>
</template>

<script>
/* eslint no-new:0 */
import Mapbox from "mapbox-gl";
import { mapState } from "vuex";
import "mapbox-gl/dist/mapbox-gl.css";
// import geocode and styles
import MapboxGeocoder from "mapbox-gl-geocoder";
import "mapbox-gl-geocoder/dist/mapbox-gl-geocoder.css";
// const locationIcon = require('../assets/location.svg')
// import Vue from 'vue'
import MapboxDraw from "@mapbox/mapbox-gl-draw/dist/mapbox-gl-draw";
import "@mapbox/mapbox-gl-draw/dist/mapbox-gl-draw.css";

Mapbox.accessToken =
  "pk.eyJ1IjoicnVzc2VsbHZlYTIiLCJhIjoiY2lmZzVrNWJkOWV2cnNlbTdza2thcGozNSJ9.zw6CcZLxP6lq0x-xfwp6uA";

export default {
  data: function() {
    return {
      organization_name: "",
      name: "",
      time_start: "",
      time_end: "",
      datetime_start: "",
      datetime_end: "",
      day_options: [
        {
          value: "1",
          label: "Monday"
        },
        {
          value: "2",
          label: "Tuesday"
        },
        {
          value: "3",
          label: "Wednesday"
        },
        {
          value: "4",
          label: "Thursday"
        },
        {
          value: "5",
          label: "Friday"
        },
        {
          value: "6",
          label: "Saturday"
        },
        {
          value: "7",
          label: "Sunday"
        }
      ],
      ownership_options: [
        {
          value: "1",
          label: "City"
        },
        {
          value: "2",
          label: "State"
        },
        {
          value: "3",
          label: "Private"
        },
        {
          value: "4",
          label: "Federal"
        },
        {
          value: "5",
          label: "Military"
        }
      ],
      holiday_restriction_options: [
        {
          value: "1",
          label: "State"
        },
        {
          value: "2",
          label: "Federal"
        }
      ],
      value5: [],
      holiday_restrictions: [],
      ownership: [],
      items: [],
      draw: new MapboxDraw()
    };
    //   locationIcon
    // }
  },
  computed: mapState({
    locationDetermined: "locationDetermined"
  }),
  mounted() {
    const map = new Mapbox.Map({
      container: document.querySelector(".map"),
      style: "mapbox://styles/mapbox/streets-v9",
      center: [-158.000072, 21.441922],
      zoom: 9
    });
    // add geocode text field
    map.addControl(
      new MapboxGeocoder({
        accessToken: Mapbox.accessToken
      })
    );

    map.addControl(this.draw);
    map.on("load", () => {
      import("./parks.geojson").then(data => {
        map.addLayer({
          id: "parks",
          type: "fill",
          paint: {
            "fill-color": "#ff0000"
          },
          source: {
            type: "geojson",
            data
          }
        });

        if ("geolocation" in navigator) {
          navigator.geolocation.getCurrentPosition(
            pos => {
              this.$store.commit("locationFound", pos.coords);
              map.flyTo({
                center: [pos.coords.longitude, pos.coords.latitude],
                zoom: 13
              });
            },
            err => {
              console.log(err);
              alert("We can't seem to determine your position");
            }
          );
        }
      });
    });
  },
  methods: {
    submit: function() {}
  },
  components: {}
};
</script>

<style lang='css' scoped>
  .map {
    height: calc(100vh - 64px);
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

  .el-date-editor.el-input {
      width: auto;
  }
</style>

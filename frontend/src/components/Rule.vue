<template>
  <div class="container">
    <TopBar name="Rule"></TopBar>

    <div class="main-content">
      <h2 class="big" >RESTRICTION</h2>
      <h2 class="small">DETAILS</h2>
      <div class="category-name">
        <h2 class="category">{{ $route.params.category }}</h2>
      </div>
      <div>
        <div class="rule-item"
          v-for="(rule, index) in rules"
          :key="index"
        >
          <div class="rule-name"> {{rule.name}} </div>
          <span v-if="rule.restrictions.hours_start">
            Open Hours:
            <br/>
            {{ hour12to24(rule.restrictions.hours_start) }} - {{ hour12to24(rule.restrictions.hours_end) }}
          </span>
        </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint no-new:0 */
import Mapbox from "mapbox-gl";
import "mapbox-gl/dist/mapbox-gl.css";

import TopBar from "./TopBar.vue";

import { mapState } from "vuex";
// const locationIcon = require('../assets/location.svg')

Mapbox.accessToken =
  "pk.eyJ1IjoicnVzc2VsbHZlYTIiLCJhIjoiY2lmZzVrNWJkOWV2cnNlbTdza2thcGozNSJ9.zw6CcZLxP6lq0x-xfwp6uA";

export default {
  name: "Rule",

  components: { TopBar },

  computed: mapState({
    rules: state => state.rules,
  }),

  methods: {
    hour12to24(time) {
      let t = parseInt(time);

      if(t < 1200) {
        if(t < 100) {
          t = t + 1200;
        }
        t = t.toString();
        t = t.slice(0, t.length - 2) + ":" + t.slice(t.length - 2, t.length)
        return t + " AM";
      } else {
        t = t - 1200;
        if(t < 100) {
          t + 1200;
        }
        t = t.toString();
        t = t.slice(0, t.length - 2) + ":" + t.slice(t.length - 2, t.length)
        return t + " PM";
      }
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.rule-item {
  border-top: solid rgb(238, 217, 217) 1px;
  padding-top: 10px;
  padding-bottom: 10px;
}
.category {
  margin: 0px;
}
.big {
  margin-bottom: 0px;
  font-size: 24px;
}
.small {
  margin-top: 0px;
  font-size: 16px;
  font-weight: 100;
}
.bill-text {
  display: inline-block;
}

.main-content {
  width: 100%;
  padding-left: 5%;
  padding-right: 5%;
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

.status-sign {
  display: inline-block;
  width: 25%;
  padding-right: 20px;
}
.rule-name {
  font-weight: bold;
}

.category-name {
  padding-top: 10px;
  padding-bottom: 10px;
  text-align: center;
}

.bill-text {
  padding-bottom: 20px;
}

.map {
  height: 200px;
  width: 100%;
}
</style>

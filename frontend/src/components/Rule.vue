<template>
  <div class="container">
    <topbar name="Rule"></topbar>

    <div class="main-content">
      <div class="rule-name">
        <h2>{{ $route.params.category }}</h2>
      </div>
      <div>
        <p 
          v-for="rule in rules"
          :key="rule"
        >
          {{ rule.name }}<br/>
          <span v-if="rule.restrictions.hours_start">
            Open Hours:
            <br/>
            {{ rule.restrictions.hours_start }} - {{ rule.restrictions.hours_end }}
          </span>
        </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint no-new:0 */
import Mapbox from "mapbox-gl";
import "mapbox-gl/dist/mapbox-gl.css";

import topbar from "./TopBar.vue";

import { mapState } from "vuex";
// const locationIcon = require('../assets/location.svg')

Mapbox.accessToken =
  "pk.eyJ1IjoicnVzc2VsbHZlYTIiLCJhIjoiY2lmZzVrNWJkOWV2cnNlbTdza2thcGozNSJ9.zw6CcZLxP6lq0x-xfwp6uA";

export default {
  name: "Rule",
  computed: mapState({
    rules: state => state.rules
  }),
  components: { topbar }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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

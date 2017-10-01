<template>
  <div class="container">
    <topbar name="Rule"></topbar>

    <div class="main-content">
      <div class="rule-name">
        <h2>{{ rule.name }}</h2>
      </div>
    </div>
    <bottombar></bottombar>
  </div>
</template>

<script>
/* eslint no-new:0 */
import Mapbox from 'mapbox-gl'
import 'mapbox-gl/dist/mapbox-gl.css'

import topbar from './TopBar.vue'
import bottombar from './BottomBar.vue'

import Axios from 'axios'
// const locationIcon = require('../assets/location.svg')
// import Vue from 'vue'

Mapbox.accessToken = 'pk.eyJ1IjoicnVzc2VsbHZlYTIiLCJhIjoiY2lmZzVrNWJkOWV2cnNlbTdza2thcGozNSJ9.zw6CcZLxP6lq0x-xfwp6uA'

export default {
  name: 'Rule',
  data() {
    return {
      // static rules *remove when api is created
      rule: {}
    }
  },
  methods: {
    getRule: function(id) {
      var url = 'http://localhost:50050/features/' + this.$route.params.ruleId
      return Axios.get(url)
        .then(function(response) {
          return response.data
        })
    }
  },
  mounted() {
    this.getRule(this.$route.params.id)
      .then(data => {
        this.rule = data
        this.name = data.name
        this.restriction = data.restrictions
      })
    // use API to grab rule and set it here with this.$route.params.ruleId
  },
  components: { bottombar, topbar }
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

.title>h4 {
  margin: 0px;
}

.description {
  float: right;
  vertical-align: top;
  display: inline-block;
  width: 75%;
}

.description>p {
  margin: 0px;
  padding-bottom: 20px;
}

.rule-name>h2 {
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

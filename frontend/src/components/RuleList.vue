<template>
  <div class="container">

    <topbar name="Rule List"></topbar>

    <md-table md-sort="restriction" class="rule-table">
      <md-table-header>
        <md-table-row>
          <md-table-head md-sort-by="dessert">Rule ({{ rules.length }})</md-table-head>
          <md-table-head md-sort-by="protein" md-numeric>Restriction</md-table-head>
        </md-table-row>
      </md-table-header>

      <md-table-body>
        <md-table-row v-for="(row, index) in rules" :key="index" @click.native="rowClick(row._id)">
          <md-table-cell>{{ row.name }}</md-table-cell>
          <md-table-cell class="restriction">
            <div class="red-circle"></div>
          </md-table-cell>
        </md-table-row>
      </md-table-body>
    </md-table>
    <bottombar></bottombar>
  </div>
</template>

<script>
import bottombar from './BottomBar.vue'
import topbar from './TopBar.vue'

import Axios from 'axios'

export default {
  name: 'RuleList',
  data() {
    return {
      rules: []
    }
  },
  beforeRouterEnter() {

  },
  created() {
    this.getAllRules(this.$route.params.lng, this.$route.params.lat)
  },
  mounted() {
    console.log('mounted' + this.rules)
  },
  methods: {
    getRules: function(href) {
      return Axios.get(href)
        .then(function(response) {
          return response.data
        })
    },
    pushRules: function(url) {
      return this.getRules(url).then(data => {
        for (var i = 0; i < data._items.length; i++) {
          this.rules.push(data._items[i])
        }
        return data
      })
    },
    getAllRules: function(lng, lat) {
      var url = 'http://localhost:50050/features/?where={"geojson.geometry":{"$near":{"$geometry":{"type":"Point", "coordinates":[' + lng + ', ' + lat + ']}, "$maxDistance": 250}}}'
      this.pushRules(url).then(data => {
        if (data._links.next) {
          var href = 'http://localhost:50050/' + data._links.next.href
          this.pushRules(href)
        }
      })
    },
    rowClick: function(id) {
      this.$router.push({ name: 'Rule', params: { ruleId: id } })
    }
  },
  components: { bottombar, topbar }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.qwer {
  width: 100px;
  height: 100px;
}

.rule-table {
  width: 100%;
}

.restriction {}

.red-circle {
  background: #f00;
  width: 50px;
  height: 50px;
  border-radius: 50%;
}

.table-row {}

.rule-name-cell {
  height: inherit;
  width: 75vw;
}

.rule-status-cell {
  height: inherit;
  width: 25vw;
}

.md-table-cell {
  font-size: 20px;
}

.md-table {
  position: absolute;
  top: 64px;
  bottom: 64px;
}

.md-toolbar {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 2;
  width: 100% !important;
}

.md-bottom-bar {
  position: fixed;
  bottom: 0;
  z-index: 4
}
</style>

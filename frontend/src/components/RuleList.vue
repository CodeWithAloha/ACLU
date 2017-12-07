<template>
  <div class="container">

    <topbar name="Rule List"></topbar>

    <md-table md-sort="restriction" class="rule-table">
      <md-table-body>
        <md-table-row 
          v-for="category in categories" 
          :key="category"
          @click.native="rowClick(category)"
        >
          <md-table-cell style="text-align: center;">{{ category }}</md-table-cell>
        </md-table-row>
      </md-table-body>
    </md-table>
  </div>
</template>

<script>
import bottombar from "./BottomBar.vue";
import topbar from "./TopBar.vue";

export default {
  name: "RuleList",
  data() {
    return {
      categories: ["Recreation", "Private land", "Activism"]
    };
  },
  methods: {
    rowClick(category) {
      this.$router.push({ name: "Rule", params: { category } });
    }
  },
  components: { bottombar, topbar }
};
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

.restriction {
}

.red-circle {
  background: #f00;
  width: 50px;
  height: 50px;
  border-radius: 50%;
}

.table-row {
}

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
  z-index: 4;
}
</style>

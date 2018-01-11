<template>
  <div class="container">

    <TopBar name="Rule List"></TopBar>

    <md-table md-sort="restriction" class="rule-table">
      <md-table-body>
        <md-table-row 
          v-for="(category, index) in categories" 
          :key="index"
          @click.native="rowClick(category)"
        >
          <md-table-cell style="text-align: center;">{{ category }}</md-table-cell>
        </md-table-row>
      </md-table-body>
    </md-table>
  </div>
</template>

<script>
import TopBar from "./TopBar.vue";

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
  components: { TopBar }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.main-content {
  width: 100%;
  padding-left: 5%;
  padding-right: 5%;
}

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
</style>

<template>
  <md-bottom-bar>
    <md-bottom-bar-item md-icon="subject" :md-active="rules.length > 0" @click="showRules">Rules
      <span v-if="rules.length > 0">( {{ rules.length }} ) </span>
    </md-bottom-bar-item>
  </md-bottom-bar>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "bottombar",
  props: ["longitude", "latitude"],
  data() {
    return {};
  },
  computed: mapState({
    rules: state => state.rules
  }),
  mounted() {},
  methods: {
    showRules() {
      this.$router.push({
        name: "RuleList",
        params: { lat: this.latitude, lng: this.longitude }
      });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.md-bottom-bar {
  position: fixed;
  bottom: 0;
  z-index: 4;
}
</style>

<template>
    <md-toolbar>
      <md-button v-if="backButton != false" class="md-icon-button" @click="goBack">
        <md-icon>arrow_back</md-icon>
      </md-button>

      <h2 class="md-title" style="flex: 1">{{ name }} </h2>
    </md-toolbar>
</template>

<script>
export default {
  name: "topbar",
  props: ["name", "backButton"],
  data() {
    return {};
  },
  mounted() {},
  methods: {
    goBack: function() {
      this.$router.go(-1);
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

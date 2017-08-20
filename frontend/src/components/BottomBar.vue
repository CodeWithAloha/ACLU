<template>
  <md-bottom-bar>
    <md-bottom-bar-item md-icon="subject">Organization</md-bottom-bar-item>
    <md-bottom-bar-item md-icon="subject">Rules</md-bottom-bar-item>
  </md-bottom-bar>
</template>

<script>
export default {
  name: 'bottombar',
  data () {
    return {
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .md-bottom-bar {
    position: fixed;
    bottom: 0;
    z-index: 4
  }
</style>

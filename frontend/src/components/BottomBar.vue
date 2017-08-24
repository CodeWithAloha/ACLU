<template>
  <md-bottom-bar>
    <md-bottom-bar-item md-icon="subject">Organizations</md-bottom-bar-item>
    <md-bottom-bar-item md-icon="subject" @click="rules">Rules</md-bottom-bar-item>
  </md-bottom-bar>
</template>

<script>
export default {
  name: 'bottombar',
  props: ['longitude', 'latitude'],
  data () {
    return {}
  },
  mounted () {
  },
  methods: {
    rules () {
      this.$router.push({name: 'RuleList', params: {lat: this.latitude, lng: this.longitude}})
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

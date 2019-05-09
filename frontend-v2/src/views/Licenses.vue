<template>
  <div id="license-page">
    <div id="license-page-content">
      <h1>Licenses</h1>
      <VueMarkdown>{{licenseText}}</VueMarkdown>
    </div>
  </div>
</template>

<script>
import licenseText from 'raw-loader!../assets/licenses.md'
import VueMarkdown from 'vue-markdown'

export default {
  name: 'Licenses',
  components: {
    VueMarkdown
  },
  data: () => {
    return {
      licenseText
    };
  }
}
</script>

<style scoped>
#license-page-content {
  padding: 2rem 4rem;
  font-size: 1rem;
  line-height: 2rem;
  overflow-x: hidden;
}
</style>

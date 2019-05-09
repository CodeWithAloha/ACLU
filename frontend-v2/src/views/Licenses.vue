<template>
  <div id="license-page">
    <div id="license-page-content">
      <h1>Licenses</h1>
      <VueMarkdown>{{txt}}</VueMarkdown>
    </div>
  </div>
</template>

<script>
import txt from 'raw-loader!../assets/licenses.md'
import VueMarkdown from 'vue-markdown'

export default {
  name: 'Licenses',
  components: {
    VueMarkdown
  },
  data: () => {
    return {
      txt: txt
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

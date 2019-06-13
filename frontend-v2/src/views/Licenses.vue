<template>
  <div id="license-page">
    <div id="license-page-content">
      <h1>Licenses</h1>
      <div v-html="licenseText"></div>
    </div>
  </div>
</template>

<script>
import licenseText from '../assets/licenses.md'

export default {
  name: 'Licenses',
  data: () => {
    return {
      licenseText
    }
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

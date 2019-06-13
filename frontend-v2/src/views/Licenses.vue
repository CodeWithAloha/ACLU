<template>
  <div id="license-page">
    <div class="page-content">
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
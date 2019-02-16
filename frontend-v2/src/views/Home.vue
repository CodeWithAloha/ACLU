<template>
  <div>
    <Splash></Splash>
    <Map></Map>
  </div>
</template>

<script>
import Splash from '@/components/Splash'
import Map from '@/components/Map'

export default {
  name: 'Home',
  components: {
    Map,
    Splash
  },
  data: () => ({}),
  methods: {
  }
}
</script>
<style scoped>
.page-container {
  height: 100vh;
  overflow: hidden;
  position: relative;
  border: 1px solid rgba(#000, 0.12);
}
</style>

<template>
  <div>
    <Splash :show="showSplash"></Splash>
    <Map @mapLoaded="onMapLoaded"></Map>
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
  data: () => ({
    // showSplash: true
  }),
  mounted () {
    // setTimeout(() => {
    //   this.showSplash = false
    // }, 2000);
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

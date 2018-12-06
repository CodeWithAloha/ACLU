<template>
  <div>
    <Splash :show="loading"></Splash>
    <Loading></Loading>
    <Map @mapLoaded="onMapLoaded"></Map>
  </div>
</template>

<script>
import Splash from '@/components/Splash'
import Loading from '@/components/Loading'
import Map from '@/components/Map'

export default {
  name: 'Home',
  components: {
    Map,
    Loading,
    Splash,
  },
  data: () => ({
    loading: true
  }),
  methods: {
    onMapLoaded () {
      this.loading = false
    }
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

<template>
    <div>
        <LoadingComponent :loading="loading"></LoadingComponent>
        <div class="page-container md-layout-column">
            <NavBarComponent></NavBarComponent>
            <md-content>
                <MapComponent @mapLoaded="onMapLoaded"></MapComponent>
            </md-content>
        </div>
    </div>
</template>

<script>
import LoadingComponent from '@/components/LoadingComponent'
import MapComponent from '@/components/MapComponent'
import NavBarComponent from '@/components/NavBarComponent'

export default {
  name: 'Home',
  components: {
    MapComponent,
    NavBarComponent,
    LoadingComponent
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

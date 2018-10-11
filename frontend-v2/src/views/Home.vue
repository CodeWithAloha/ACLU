<template>
	<div>
		<Loading :loading="loading"></Loading>
		<div class="page-container md-layout-column">
			<NavBar></NavBar>
			<md-content>
				<Map @mapLoaded="onMapLoaded"></Map>
			</md-content>
		</div>
	</div>
</template>

<script>
import Loading from '@/components/Loading'
import Map from '@/components/Map'
import NavBar from '@/components/NavBar'

export default {
  name: 'Home',
  components: {
    Map,
    NavBar,
    Loading
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

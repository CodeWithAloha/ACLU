<template>
	<div>
		<Loading :loading="loading"></Loading>
		<div class="page-container md-layout-column">
			<NavBarComponent></NavBarComponent>
			<md-content>
				<MapComponent></MapComponent>
			</md-content>
		</div>
	</div>
</template>

<script>
import Loading from '@/components/Loading.vue'
import MapComponent from '@/components/MapComponent.vue'
import NavBarComponent from '@/components/NavBarComponent.vue'

export default {
  name: 'Home',
  components: {
		MapComponent,
		NavBarComponent,
		Loading
	},
	data: () => ({
		loading: true
	}),
	mounted: function () {
		// Example of how to use "loading" component
		setTimeout(() => {
			this.loading = false
		}, 3000);
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

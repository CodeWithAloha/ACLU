<template>
  <div class="page-container md-layout-column">
    <NavBarComponent></NavBarComponent>
		<md-content>
			<MapComponent></MapComponent>
    </md-content>
  </div>
</template>

<script>
import MapComponent from '@/components/MapComponent.vue'
import NavBarComponent from '@/components/NavBarComponent.vue'
export default {
  name: 'Home',
  components: {
		MapComponent,
		NavBarComponent
	},
	data: () => ({
  })
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

<template>
  <div v-if="loading" class="loading-page">
    <!-- <md-progress-spinner class="md-accent" :md-stroke="6" md-mode="indeterminate"></md-progress-spinner> -->
		<img src="@/assets/spinner-image.svg" class="spinner"/>
  </div>
</template>

<script>
export default {
  props: {
    loading: true
  },
  methods: {
    start () {
      this.loading = true
    },
    finish () {
      this.loading = false
    }
  }
}
</script>

<style scoped>
.loading-page {
	display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  text-align: center;
  font-size: 30px;
  font-family: sans-serif;
  opacity: 0.5;
  background: #000;
  z-index: 10;
}

.spinner {
  max-width: 50%;
}
</style>

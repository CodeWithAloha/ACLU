<template>
  <div class="home">
		<p>Home screen</p>
		<div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/settings">About</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'home',
  components: {
  }
}
</script>

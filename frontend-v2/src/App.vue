<template>
  <div id="app">
    <div class="page-container md-layout-column">
      <NavBar></NavBar>
      <router-view/>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar'
export default {
  name: 'App',
  components: {
    NavBar
  }
}
</script>

<style>
body, html {
  height: 100%;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

#app, .page-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
</style>

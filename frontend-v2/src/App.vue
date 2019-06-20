<template>
  <div id="app">
    <transition name="fade">
      <Splash v-if="splash"/>
    </transition>
    <div class="page-container" v-show="!splash">
      <NavBar/>
      <router-view/>
    </div>
  </div>
</template>

<script>
import Splash from '@/components/Splash'
import NavBar from '@/components/NavBar'
export default {
  name: 'App',
  components: {
    Splash,
    NavBar
  },
  computed: {
    splash () {
      return this.$store.state.splash
    }
  }
}
</script>

<style>
body,
html {
  height: 100%;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
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

#app,
.page-container {
  min-height: 100%;
  display: flex;
  flex-direction: column;
}

.page-content {
  padding: 2rem 4rem;
  font-size: 1rem;
  line-height: 2rem;
  overflow-x: hidden;
}

@media (max-width: 720px) {
  .page-content {
    padding: 1rem 2rem;
  }
}
</style>

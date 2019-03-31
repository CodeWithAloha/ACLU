<template>
  <div id="app">
    <transition name="fade">
      <Splash v-if="showSplash" @hide-splash="hide"></Splash>
    </transition>
    <div v-show="!showSplash">
      <NavBar></NavBar>
      <router-view :splash="showSplash" />
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
  data: () => ({
    showSplash: true
  }),
  mounted () {
    setTimeout(() => {
      this.hide()
    }, 2000)
  },
  methods: {
    hide: function () {
      this.showSplash = false
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
</style>

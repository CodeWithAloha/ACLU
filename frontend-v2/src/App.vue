<template>
  <div id="app">
    <transition name="fade">
      <Splash v-if="splash" @hide-splash="hide"></Splash>
    </transition>
    <div v-show="!splash">
      <NavBar></NavBar>
      <router-view />
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
  },
  mounted () {
    setTimeout(() => {
      this.hide()
    }, 3000)
  },
  methods: {
    hide: function () {
      this.$store.commit('showSplash')
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

#app, .page-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
</style>

<template>
  <div class="splash" :class="[isActive ? 'visible' : 'hidden']" @click="hide">
    <div>
      <img class="logo" src="../assets/holoholo-logo@3x.png" alt="Holo Holo">
    </div>
    <RibbonComponent></RibbonComponent>
  </div>
</template>

<script>
import RibbonComponent from '@/components/Ribbon'

export default {
  name: 'Splash',
  data: () => ({isActive: true}),
  components: {
    RibbonComponent
  },
  mounted: function () {
    setTimeout(() => {
      this.hide()
    }, 3000)
  },
  methods: {
    hide: function () {
      this.isActive = false
    }
  }
}
</script>

<style>
.splash {
  background: url("../assets/splash-desktop.jpg") no-repeat center center fixed;
  background-size: cover;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 99;
  transition: opacity 0.5s ease;
}

.visible {
  opacity: 1;
  pointer-events: all;
}

.hidden {
  opacity: 0;
  pointer-events: none;
}

@media (min-width: 320px) and (max-width: 767px) {
  .splash {
    background: url("../assets/splash-mobile.jpg") no-repeat center center fixed;
  }
}

.logo {
  margin-top: -150px;
}
</style>

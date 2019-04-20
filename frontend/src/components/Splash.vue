<template>
  <div class="splash" @click="$emit('hide-splash')">
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
  components: {
    RibbonComponent
  }
}
</script>

<style scoped>
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
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
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

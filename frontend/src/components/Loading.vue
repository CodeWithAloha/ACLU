<template>
  <div class="loading-component">
    <!-- Spinner derived from: https://blog.usejournal.com/vue-js-gsap-animations-26fc6b1c3c5a -->
    <div ref="spinner" class="spinner">
      <img src="@/assets/spinner-image.svg" class="spinner-image"/>
    </div>
    <div ref="spinnerPulse" class="spinner-pulse"></div>
  </div>
</template>

<script>
import { TimelineLite, Back, Elastic, Expo } from 'gsap'

export default {
  mounted () {
    this.animate()
  },
  methods: {
    animate: function () {
      const { spinner, spinnerPulse } = this.$refs
      const timeline = new TimelineLite({
        onComplete: () => timeline.restart()
      })
      timeline
        .to(spinner, 0.4, {
          scale: 0.8,
          rotation: 16,
          ease: Back.easeOut.config(1.7)
        })
        .to(
          spinnerPulse,
          0.5,
          {
            scale: 0.9,
            opacity: 1
          },
          '-=0.6'
        )
        .to(spinner, 1.2, {
          scale: 1,
          rotation: '-=16',
          ease: Elastic.easeOut.config(2.5, 0.5)
        })
        .to(
          spinnerPulse,
          1.1,
          {
            scale: 3,
            opacity: 0,
            ease: Expo.easeOut
          },
          '-=1.2'
        )
    }
  }
}
</script>

<style scoped>
.loading-component {
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
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid white;
  background: #272727;
  border-radius: 50%;
  height: 100px;
  width: 100px;
}

.spinner-pulse {
  position: absolute;
  z-index: 1;
  height: 120px;
  width: 120px;
  top: 50%;
  left: 50%;
  margin-top: -60px;
  margin-left: -60px;
  background: #272727;
  border-radius: 50%;
  opacity: 0;
  transform: scale(0);
}

.spinner-image {
  height: 50%;
}
</style>

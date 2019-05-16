<template>
<div>
    <Map @featureSelected="onFeatureSelected"></Map>
    <div v-if="selectedFeature" class="wrapper-status-button">
      <StatusButton :status="selectedFeature.properties.condition" size="large" @click="onStatusButtonClick"></StatusButton>
    </div>
      <transition name="slide">
        <RestrictionSlide v-if="restriction"/>
      </transition>
  </div>
</template>

<script>
import Map from '@/components/Map'
import StatusButton from '@/components/StatusButton'
import RestrictionSlide from '@/components/RestrictionSlide'

export default {
  name: 'Home',
  components: {
    Map,
    StatusButton,
    RestrictionSlide
  },
  data () {
    return {
      selectedFeature: null,
      restriction: false
    }
  },
  methods: {
    onFeatureSelected (featureId) {
      this.selectedFeature = this.$store.state.renderedFeatures[featureId]
    },
    onStatusButtonClick () {
      this.restriction = !this.restriction
    }
  }
}
</script>
<style>
.wrapper-status-button {
  position: absolute;
  bottom: 50px;
  z-index: 1;
  width: 250px;
  max-width: 250px;
  min-width: 250px;
  margin-left: -125px;
  left: 50%;
  text-align: center;
}

.slide-enter-active, .slide-leave-active {
  transition: all .3s ease;
}

.slide-enter, .slide-leave-to {
  transform: translateY(50%);
}
</style>

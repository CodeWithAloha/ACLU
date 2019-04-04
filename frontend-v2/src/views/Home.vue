<template>
<div>
    <Map @featureSelected="onFeatureSelected"></Map>
    <div v-if="selectedFeature" class="wrapper-status-button">
      <StatusButton :status="selectedFeature.properties.condition" size="large" @click="onStatusButtonClick"></StatusButton>
    </div>
    <!-- TODO: Integrate with Details component when ready -->
    <!-- <FeatureDetails :feature="selectedFeature"></FeatureDetails> -->
  </div>
</template>

<script>
import Map from '@/components/Map'
import StatusButton from '@/components/StatusButton'
import { OpenStatus } from '@/services/constants'

export default {
  name: 'Home',
  components: {
    Map,
    StatusButton
  },
  data () {
    return {
      selectedFeature: null
    }
  },
  methods: {
    onFeatureSelected (featureId) {
      this.selectedFeature = this.$store.state.renderedFeatures[featureId]
    },
    onStatusButtonClick(){
      // TODO: Show FeatureDetails component when status button is clicked
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
</style>

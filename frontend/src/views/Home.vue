<template>
<div>
    <Map @featureSelected="onFeatureSelected"></Map>
    <div v-if="selectedFeature" class="wrapper-status-button">
      <StatusButton :status="selectedFeature.properties.condition" size="large" @click="onStatusButtonClick"></StatusButton>
    </div>
    <!-- TODO: Integrate with Details component when ready -->
    <RestrictionPopup
      ref="popup"
      :feature="selectedFeature" />
  </div>
</template>

<script>
import Map from '@/components/Map'
import StatusButton from '@/components/StatusButton'
import RestrictionPopup from '@/components/RestrictionPopup'

export default {
  name: 'Home',
  components: {
    Map,
    StatusButton,
    RestrictionPopup
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
    onStatusButtonClick () {
      this.$refs.popup.OpenRestrictionDialog();
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

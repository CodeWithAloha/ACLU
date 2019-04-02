<template>
<div>
    <Map @featureSelected="onFeatureSelected"></Map>
    <div v-if="this.selectedFeature" class="wrapper-status-button">
      <StatusButton :theme="selectedFeatureStatus().theme" :text="selectedFeatureStatus().text" size="large"></StatusButton>
    </div>
  </div>
</template>

<script>
import Map from "@/components/Map";
import StatusButton from "@/components/StatusButton";
import { OpenStatus } from "@/services/constants";

export default {
  name: "Home",
  components: {
    Map,
    StatusButton
  },
  data() {
    return {
      selectedFeature: null
    };
  },
  methods: {
    onFeatureSelected(feature) {
      this.selectedFeature = feature;
    },
    selectedFeatureStatus() {
      if (!this.selectedFeature) return;
      switch (this.selectedFeature.properties.condition) {
        case OpenStatus.Open:
          return {
            theme: "success",
            text: "Permitted"
          };
        case OpenStatus.ClosingSoon:
          return {
            theme: "warning",
            text: "Closing Soon"
          };
        case OpenStatus.Closed:
          return {
            theme: "alert",
            text: "Restricted"
          };
        case OpenStatus.Unknown:
        default:
          return {
            theme: "primary",
            text: "Unknown"
          };
      }
    }
  }
};
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
<template>
  <md-dialog :md-active.sync="showDialog">
    <md-dialog-title>{{feature.properties.condition}}</md-dialog-title>
    <md-dialog-content md-label="General" >
    </md-dialog-content>
    <md-dialog-actions>
      <md-button class="md-accent md-raised" @click="showDialog = false">Close</md-button>
    </md-dialog-actions>
  </md-dialog>
</template>

<script>
export default {
  name: 'RestrictionPopup',
  methods: {
    OpenRestrictionDialog () {
      this.showDialog = true
    },
  },
  props: ['feature'],
  data: () => ({
    showDialog: false,
  }),
}
</script>

<style lang="scss">
    .md-dialog {
        max-width: 768px;
    }
</style>

<template>
  <div>
  <md-dialog ref="RestrictionDialog">
    <md-dialog-title>Open</md-dialog-title>
    <md-dialog-content md-label="General" :md-active.sync="showDialog" ref="RestrictionDialog">
      <md-list class="md-double-line">
        <md-subheader>{{ name }}</md-subheader>
        <md-subheader>Location Information</md-subheader>
        <md-list-item>
          <div class="md-list-item-text">
            <span>{{ address }}</span>
            <span>{{ hours }}</span>
          </div>
        </md-list-item>
      </md-list>
    </md-dialog-content>
    <md-dialog-actions>
      <md-button class="md-accent md-raised" @click="showDialog = false">Close</md-button>
    </md-dialog-actions>
  </md-dialog>
  <md-button class="md-primary md-raised" @click="showDialog = true">Show Restriction</md-button>
  </div>
</template>

<script>
export default {
  name: 'RestrictionPopup',
  methods: {
    OpenRestrictionDialog () {
      this.$refs.RestrictionDialog.open()
    },
    CloseRestrictionDialog () {
      this.$refs.RestrictionDialog.close()
    }
  },
  props: ['feature'],
  data: () => ({
    showRestriction: false,
    showDialog: false,
    dialogRef: 'RestrictionDialog'
  }),
  computed: {
    status: function () {
      return 'Open'
    },
    category: function () {
      return 'Property Category'
    },
    name: function () {
      return 'Property Name'
    },
    address: function () {
      return '123 Street,\nHonolulu, HI 96826'
    },
    hours: function () {
      return 'M-F 5am-8pm, Sat 8am-12pm, Sun, 10am-4pm'
    },
    details: function () {
      return 'details about property restrictions'
    }
  }
}
</script>

<style lang="scss">
    .md-dialog {
        max-width: 768px;
    }
</style>

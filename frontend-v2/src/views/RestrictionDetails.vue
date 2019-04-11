<template>
  <div class="RestrictionDetails">
    <md-toolbar :md-elevation="1">
      <span class="md-title">Restriction Details</span>
    </md-toolbar>
    <md-list class="md-double-line">
      <md-subheader>{{ name }}</md-subheader>
      <md-list-item>
          <div class="md-list-item-text">
            <span>{{ category }}</span>
          </div>
      </md-list-item>
      <md-divider></md-divider>
      <md-subheader>Location Information</md-subheader>
      <md-list-item>
          <div class="md-list-item-text">
            <span>{{ address }}</span>
            <span>{{ hours }}</span>
          </div>
      </md-list-item>
      <md-divider></md-divider>
      <md-subheader>Restriction Notes</md-subheader>
      <md-list-item>
          <div class="md-list-item-text">
            <span>{{ details }}</span>
          </div>
      </md-list-item>
    </md-list>
  </div>
</template>

<script>
export default {
  name: 'restrictiondetails',
  components: {
  }
}
</script>

<script>
module.exports = {
  computed: {
    category: function () {
      return 'Property Category'
    },
    name: function () {
      return 'Property Name'
    },
    address: function () {
      return "123 Street,\nHonolulu, HI 96826"
    },
    hours: function () {
      return "M-F 5am-8pm, Sat 8am-12pm, Sun, 10am-4pm"
    },
    details: function () {
      return "details about property restrictions"
    }
  }
}
</script>

<style lang="scss">
  .RestrictionDetails {
    text-align: center;
    padding: 3rem;
    h1 {
      font-size: 5rem;
      color: var(--md-theme-default-primary, #448aff);
    }
    .RestrictionCategory {
      font-size: 3rem;
      text-align: center;
    }
    .FlexBox {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .LocationName {
      font-size: 3rem;
      text-align: left;
      padding: 1rem;
      color: var(--md-theme-default-primary, #448aff);
    }
    .LocationAddress {
      text-align: left;
      color: var(--md-theme-default-primary, #448aff);
    }
    .LocationHours {
      text-align: left;
    }
    .RestrictionNotes {
      text-align: left;
    }
    .BoxHeader {
      text-align: left;
      font-weight: bold;
      color: var(--md-theme-default-primary, #448aff);
    }
  }
</style>

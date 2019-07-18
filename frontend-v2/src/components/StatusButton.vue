<template>
  <md-button
    class="md-raised status"
    v-bind:class="[renderProperties.theme]"
    @click="$emit('click')"
  >{{ renderProperties.text }}</md-button>
</template>

<script>
import { OpenStatus } from '@/services/constants'
export default {
  name: 'StatusButton',
  props: ['status'],
  computed: {
    renderProperties () {
      switch (this.status) {
        case OpenStatus.Open:
          return {
            theme: 'success',
            text: 'Open to Public'
          }
        case OpenStatus.ClosingSoon:
          return {
            theme: 'warning',
            text: 'Closing Soon'
          }
        case OpenStatus.Closed:
          return {
            theme: 'alert',
            text: 'Closed'
          }
        case OpenStatus.Unknown:
        default:
          return {
            theme: 'primary',
            text: 'Unknown'
          }
      }
    }
  }
}
</script>

<style lang="scss">
.md-button.md-raised.status {
  font-weight: bold;
  padding-left: 1rem;
  padding-right: 1rem;

  &.success {
    color: #50d076;
  }
  &.alert {
    color: #f0404d;
  }
  &.warning {
    color: #f6c95f;
  }
  &.primary {
    color: #699bf9;
  }
}
</style>

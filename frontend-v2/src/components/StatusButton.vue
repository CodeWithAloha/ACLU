<template>
  <!-- <router-link to="/restriction-details" class="chip" v-bind:class="[sizeClass, renderProperties.theme]">
    {{ renderProperties.text }}
  </router-link> -->
  <a href="#" class="chip" v-bind:class="[sizeClass, renderProperties.theme]" @click="onClick">
      {{ renderProperties.text }}
  </a>
</template>

<script>
import { OpenStatus } from '@/services/constants'
export default {
  name: 'StatusButton',
  components: {},
  props: ['status', 'size'],
  computed: {
    renderProperties () {
      switch (this.status) {
        case OpenStatus.Open:
          return {
            theme: 'success',
            text: 'Permitted'
          }
        case OpenStatus.ClosingSoon:
          return {
            theme: 'warning',
            text: 'Closing Soon'
          }
        case OpenStatus.Closed:
          return {
            theme: 'alert',
            text: 'Restricted'
          }
        case OpenStatus.Unknown:
        default:
          return {
            theme: 'primary',
            text: 'Unknown'
          }
      }
    },
    sizeClass () {
      switch (this.size) {
        case 'large':
          return 'large'
        default:
          return 'mini'
      }
    }
  },
  methods: {
    onClick () {
      this.$emit('click')
    }
  }
}
</script>

<style lang="scss">
.chip {
  &.mini {
    width: 45%;
    padding: 0.2rem 1rem;
    &::before {
      height: 10px;
    }
  }

  &.large {
    min-width: 50%;
    padding: 0.5rem 1rem;
    font-size: 1.5rem;
    &::before {
      width: 15px;
      height: 15px;
      margin-right: 0.5rem;
    }
  }

  margin: 0.5rem 0.2rem;
  background-color: #ffffff;
  box-shadow: -0.05rem 0.15rem 0.2rem rgba(0, 0, 0, 0.25);
  border-radius: 0.2rem;
  font-weight: bold;
  text-decoration: none !important;
  &.no-gutter {
    margin: 0rem 0rem;
  }
  &::before {
    content: "";
    border-radius: 100%;
    margin-right: 0.5rem;
    display: inline-block;
  }

  &.success {
    color: #50d076 !important;
    &::before {
      background-color: #50d076;
      width: 15px;
      height: 15px;
    }
  }
  &.alert {
    color: #f0404d !important;
    &::before {
      background-color: #f0404d;
      width: 15px;
      height: 15px;
    }
  }
  &.warning {
    color: #f6c95f !important;
    &::before {
      background-color: #f6c95f;
      width: 15px;
      height: 15px;
    }
  }
  &.primary {
    color: #699bf9 !important;
    &::before {
      background-color: #699bf9;
      width: 15px;
      height: 15px;
    }
  }
}
</style>

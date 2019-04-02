<template>
  <a href="#" class="chip" v-bind:class="[sizeClass, colorClass]">
      {{ text }}
  </a>
</template>

<script>
export default {
  name: 'StatusButton',
  components: {},
  props: ['theme', 'size', 'text'],
  computed: {
    colorClass () {
      switch (this.theme) {
        case 'success':
          return 'success'
        case 'warning':
          return 'warning'
        case 'alert':
          return 'alert'
        case 'primary':
        default:
          return 'unknown'
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
      border-right: 5px solid #50d076;
      border-left: 5px solid #50d076;
    }
  }
  &.alert {
    color: #f0404d !important;
    &::before {
      background-color: #f0404d;
      border-right: 5px solid #f0404d;
      border-left: 5px solid #f0404d;
    }
  }
  &.warning {
    color: #f6c95f !important;
    &::before {
      background-color: #f6c95f;
      border-right: 5px solid #f6c95f;
      border-left: 5px solid #f6c95f;
    }
  }
  &.unknown {
    color: #699bf9 !important;
    &::before {
      background-color: #699bf9;
      border-right: 5px solid #699bf9;
      border-left: 5px solid #699bf9;
    }
  }
}
</style>

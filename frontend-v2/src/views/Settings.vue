<template>
  <SplitTemplate>
    <template slot="title">
      Accessibility Survey
    </template>
    <template slot="subtitle">
      Do you have any of the following conditions?
    </template>
    <template slot="body">
      <div class="checkbox-wrap">
        <md-checkbox v-model="colorblindness">Colorblindness</md-checkbox>
        <md-checkbox v-model="partialSight">Partial Sight</md-checkbox>
      </div>
    </template>
  </SplitTemplate>
</template>

<script>
import SplitTemplate from '@/views/SplitTemplate.vue';

export default {
  name: 'settings',
  data () {
    return {
      colorblindness: false,
      partialSight: false
    }
  },
  components: {
    SplitTemplate,
  }
}
</script>

<style lang="scss">
  .checkbox-wrap {
    display: flex;
    flex-direction: column;
  }
</style>
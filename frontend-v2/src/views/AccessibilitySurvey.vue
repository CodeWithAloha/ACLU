<template>
  <SplitTemplate :next="next">
    <template slot="title">
      Accessibility Survey
    </template>
    <template slot="subtitle">
      Do you have any of the following conditions?
    </template>
    <template slot="body">
      <div class="checkbox-wrap">
        <md-checkbox
          v-model="colorblindness"
          @change="onChangeColorblindness($event)">Colorblindness</md-checkbox>
        <md-checkbox
          v-model="partialSight"
          @change="onChangePartialSight($event)">Partial Sight</md-checkbox>
      </div>
    </template>
  </SplitTemplate>
</template>

<script>
import SplitTemplate from '@/views/SplitTemplate.vue'

export default {
  name: 'settings',
  data () {
    return {
      colorblindness: this.$store.state.accessibility.colorblindness,
      partialSight: this.$store.state.accessibility.partialSight
    }
  },
  components: {
    SplitTemplate
  },
  methods: {
    next () {
      this.$store.commit('completedAccessibilitySurvey')
      this.$router.push('intro')
    },
    onChangeColorblindness (event) {
      this.$store.commit('toggleColorblindness')
    },
    onChangePartialSight (event) {
      this.$store.commit('togglePartialSight')
    }
  }
}
</script>

<style lang="scss">
  .checkbox-wrap {
    display: flex;
    flex-direction: column;
  }
</style>

<template>
  <SplitTemplate v-if="page == 0" :next="next">
    <template slot="title">
      logo
    </template>
    <template slot="body">
      <h1>Go for a walk</h1>
      <p>
        Holoholo in the Hawaiian language means “take a leisure stroll.”
        Our goal is to help you figure out if and when you are allowed to stay in a certain place on the island of O’ahu.
      </p>
    </template>
  </SplitTemplate>
  <SplitTemplate
    v-else-if="page == 1"
    :next="next"
    :back="back"
  >
    <template slot="title">
      logo
    </template>
    <template slot="body">
      <h1>How it works</h1>
      <p>
        We use location information to determine what you are allowed to do there.
        Holoholo is a web application. You can access it anywhere with internet.
      </p>
    </template>
  </SplitTemplate>
  <SplitTemplate
    v-else-if="page == 2"
    :next="next"
    :back="back"
  >
    <template slot="title">
      logo
    </template>
    <template slot="body">
      <h1>How it works</h1>
      <p>
        The initial highlighted polygon will always represent your current location. You can tap on any of the displayed polygons to get information about the restrictions in the area.

        The for states of the locations are the following:
      </p>
      <div class="status-buttons-wrap">
        <StatusButton :status="OpenStatus.Open"></StatusButton>
        <StatusButton :status="OpenStatus.ClosingSoon"></StatusButton>
        <StatusButton :status="OpenStatus.Closed"></StatusButton>
        <StatusButton :status="OpenStatus.Unknown"></StatusButton>
      </div>
    </template>
  </SplitTemplate>
  <SplitTemplate
    v-else-if="page == 3"
    :next="next"
    :back="back"
  >
    <template slot="title">
      logo
    </template>
    <template slot="body">
      <StatusButton :status="OpenStatus.Closed" size="large"></StatusButton>
      <p>
        The color red represents an area that is private or closed to to the public.
      </p>
    </template>
  </SplitTemplate>
  <SplitTemplate
    v-else-if="page == 4"
    :next="next"
    :back="back"
  >
    <template slot="title">
      logo
    </template>
    <template slot="body">
      <StatusButton :status="OpenStatus.ClosingSoon" size="large"></StatusButton>
      <p>
        The yellow polygon represents an area in which the status will change soon.
      </p>
    </template>
  </SplitTemplate>
  <SplitTemplate
    v-else-if="page == 5"
    :next="next"
    :back="back"
  >
    <template slot="title">
      logo
    </template>
    <template slot="body">
      <StatusButton :status="OpenStatus.Open" size="large"></StatusButton>
      <p>
        The green polygon represents an area that is open to the public.
      </p>
    </template>
  </SplitTemplate>
  <SplitTemplate
    v-else-if="page == 6"
    :next="finish"
    :back="back"
  >
    <template slot="title">
      logo
    </template>
    <template slot="body">
      <StatusButton :status="OpenStatus.Unknown" size="large"></StatusButton>
      <p>
        The blue polygon will be displayed when we are unable to identify the location  or restrictions of an area.
      </p>
    </template>
  </SplitTemplate>
</template>

<script>
import SplitTemplate from '@/views/SplitTemplate.vue'
import StatusButton from '@/components/StatusButton.vue'
import { OpenStatus } from '@/services/constants'

export default {
  name: 'intro',
  data () {
    return {
      page: 0,
      OpenStatus: OpenStatus
    }
  },
  methods: {
    next () {
      this.page++
    },

    back () {
      this.page--
    },

    finish () {
      this.$store.commit('completedIntro')
      this.$router.push('/')
    }
  },
  components: {
    SplitTemplate,
    StatusButton
  }
}
</script>

<style lang="scss">
.status-buttons-wrap {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}
</style>

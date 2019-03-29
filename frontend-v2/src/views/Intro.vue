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
      <div class="chip-wrap">
        <div class="chip mini open">
          Open
        </div>
        <div class="chip mini private">
          Private
        </div>
        <div class="chip mini conditional">
          Conditional
        </div>
        <div class="chip mini unknown">
          Unknown
        </div>
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
      <div class="chip large private">
        Private
      </div>
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
      <div class="chip large conditional">
        Conditional
      </div>
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
      <div class="chip large open">
        Open
      </div>
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
      <div class="chip large unknown">
        Unknown
      </div>
      <p>
        The blue polygon will be displayed when we are unable to identify the location  or restrictions of an area.
      </p>
    </template>
  </SplitTemplate>
</template>

<script>
import SplitTemplate from '@/views/SplitTemplate.vue'

export default {
  name: 'intro',
  data () {
    return {
      page: 0
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
    SplitTemplate
  }
}
</script>

<style lang="scss">

.chip-wrap {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

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
      margin-right: 1rem;
    }
  }

  margin: 0.5rem 0.2rem;
  box-shadow: -0.05rem 0.15rem 0.2rem rgba(0, 0, 0, 0.25);
  border-radius: 0.2rem;
  font-weight: bold;

  &::before {
    content: "";
    border-radius: 100%;
    margin-right: 0.5rem;
    display: inline-block;
  }

  &.open {
    color: #50d076;
    &::before {
      background-color: #50d076;
      border-right: 5px solid #50d076;
      border-left: 5px solid #50d076;
    }
  }
  &.private {
    color: #f0404d;
    &::before {
      background-color: #f0404d;
      border-right: 5px solid #f0404d;
      border-left: 5px solid #f0404d;
    }
  }
  &.conditional {
    color: #f6c95f;
    &::before {
      background-color: #f6c95f;
      border-right: 5px solid #f6c95f;
      border-left: 5px solid #f6c95f;
    }
  }
  &.unknown {
    color: #699bf9;
    &::before {
      background-color: #699bf9;
      border-right: 5px solid #699bf9;
      border-left: 5px solid #699bf9;
    }
  }

}

</style>

import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    accessibility: {
      colorblindness: false,
      partialSight: false
    }
  },
  mutations: {
    toggleColorblindness (state) {
      state.accessibility.colorblindness = !state.accessibility.colorblindness
    },
    togglePartialSight (state) {
      state.accessibility.partialSight = !state.accessibility.partialSight
    }
  }
})

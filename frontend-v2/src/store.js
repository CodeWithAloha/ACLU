import storage from 'local-storage-fallback'
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

let defaultState = storage.getItem('state')
if (!defaultState) {
  defaultState = {
    accessibility: {
      colorblindness: false,
      partialSight: false,
      completedInitialSurvey: false
    },
    completedIntro: false,
    renderedFeatures: {}
  }
} else {
  defaultState = JSON.parse(defaultState)
}

const store = new Vuex.Store({
  state: { ...defaultState, splash: true },
  mutations: {
    showSplash (state) {
      state.splash = false
    },
    toggleColorblindness (state) {
      state.accessibility.colorblindness = !state.accessibility.colorblindness
    },
    togglePartialSight (state) {
      state.accessibility.partialSight = !state.accessibility.partialSight
    },
    completedIntro (state) {
      state.completedIntro = true
    },
    completedAccessibilitySurvey (state) {
      state.accessibility.completedInitialSurvey = true
    }
  }
})

store.watch(state => {
  // TODO: In the future this should be a diff update
  // But right now the state is so small it's okay
  storage.setItem('state', JSON.stringify(state))
})

export default store

import Vue from 'vue';
import Vuex from 'vuex';
import { RestrictionStateType } from '../models/RetrictionState'
Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    locationDetermined: false,
    location: null,
    userValid: 0, // 0 = valid, 1 = iffy, 2 = restricted
    rules: []
  },
  mutations: {
    setUserValid (state, valid) {
      state.uservalid = valid
    },
    locationFound (state, coords) {
      state.locationDetermined = true
      state.location = [coords.latitude, coords.longitude]
    },
    updateFeatures (state, rules) {
      if (rules.find(({ restrictionState }) => restrictionState.state === RestrictionStateType.Invalid)) {
        state.userValid = 2
      } else {
        state.userValid = 0
      }
      state.rules = rules
    }
  }
})

export default store

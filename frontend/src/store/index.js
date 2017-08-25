import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    locationDetermined: false,
    location: null
  },
  mutations: {
    locationFound (state, coords) {
      state.locationDetermined = true
      state.location = [coords.latitude, coords.longitude]
    }
  }
})

export default store

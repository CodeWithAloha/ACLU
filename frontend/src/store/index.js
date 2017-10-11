import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    locationDetermined: false,
    location: null,
    rules: []
  },
  mutations: {
    locationFound(state, coords) {
      state.locationDetermined = true;
      state.location = [coords.latitude, coords.longitude];
    },
    updateRules(state, rules) {
      state.rules = rules;
    }
  }
});

export default store;

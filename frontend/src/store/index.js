import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    locationDetermined: false,
    location: null,
    userValid: 0, // 0 = valid, 1 = iffy, 2 = restricted
    rules: []
  },
  mutations: {
    setUserValid(state, valid) {
      state.uservalid = valid;
    },
    locationFound(state, coords) {
      state.locationDetermined = true;
      state.location = [coords.latitude, coords.longitude];
    },
    updateRules(state, rules) {
      if (rules.find(({ isValid }) => isValid === false)) {
        state.userValid = 2;
      } else {
        state.userValid = 0;
      }
      state.rules = rules;
    }
  }
});

export default store;

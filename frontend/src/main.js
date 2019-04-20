import 'mapbox-gl/dist/mapbox-gl.css'
import Vue from 'vue'
import VueMaterial from 'vue-material'
import 'vue-material/dist/theme/default.css'
import 'vue-material/dist/vue-material.min.css'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.use(VueMaterial)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

if (!store.state.renderedFeatures) store.state.renderedFeatures = {}
if (!store.state.accessibility.completedInitialSurvey) {
  router.replace('accessibility')
} else if (!store.state.completedIntro) {
  router.replace('intro')
}

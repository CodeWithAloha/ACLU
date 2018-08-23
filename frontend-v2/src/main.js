import 'mapbox-gl/dist/mapbox-gl.css'
import Vue from 'vue'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import App from './App.vue'
import router from './router'

Vue.use(VueMaterial)
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

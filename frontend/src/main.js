// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'

import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.css'

import MaterialDesignsIcons from 'material-design-icons'
import 'material-design-icons/iconfont/material-icons.css'

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'

import locale from 'element-ui/lib/locale/lang/en'

import App from './App'
import router from './router'
import store from './store'

Vue.config.productionTip = false

Vue.use(VueMaterial)
Vue.use(MaterialDesignsIcons)

/* eslint-disable no-new */

Vue.use(VueMaterial)
Vue.use(ElementUI, { locale })

new Vue({
  el: '#app',
  store,
  router,
  template: '<App/>',
  components: { App }
})

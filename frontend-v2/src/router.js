import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/report-feedback',
      name: 'report-feedback'
    },
    {
      path: '/settings',
      name: 'settings',
      component: () => import(/* webpackChunkName: "about" */ './views/Settings.vue')
    },
    {
      path: '*',
      name: '404',
      component: () => import(/* webpackChunkName: "about" */ './views/404.vue')
    }
  ]
})

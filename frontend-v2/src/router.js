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
      component: () => import(/* webpackChunkName: "settings" */ './views/Settings.vue')
    },
    {
      path: '/accessibility',
      name: 'accessibility',
      component: () => import(/* webpackChunkName: "accessibilitySurvey" */ './views/AccessibilitySurvey.vue')
    },
    {
      path: '/intro',
      name: 'intro',
      component: () => import(/*  webpackChunkName: "intro" */ './views/Intro.vue')
    },
    {
      path: '*',
      name: '404',
      component: () => import(/* webpackChunkName: "about" */ './views/404.vue')
    }
  ]
})

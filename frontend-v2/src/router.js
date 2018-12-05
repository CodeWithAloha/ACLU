import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Splash from './views/Splash.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/splash',
      name: 'splash',
      component: Splash
    },
    {
      path: '/',
      name: 'splash',
      component: Splash
    },
    {
      path: '/home',
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
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/Settings.vue')
    },
       {
      path: '/how-it-works',
      name: 'howitworks',
      component: () => import( './views/HowItWorks.vue'),
           beforeEnter: (to, from, next) => {
          let firstvisit = Vue.cookie.get('first_visit')
            if (firstvisit == '1') {
                 next({ name: 'home' })
                }
             else {
                next()
                Vue.cookie.set('first_visit', '1', 5)
             }
               }
       }
  ]
})

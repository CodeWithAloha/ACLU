import Vue from 'vue'
import Router from 'vue-router'
// import Map from '@/components/Map'
import RuleList from '@/components/RuleList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Rule_List',
      component: RuleList
    }
  ]
})

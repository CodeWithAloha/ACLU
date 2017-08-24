import Vue from 'vue'
import Router from 'vue-router'
import Map from '@/components/Map'
import RuleList from '@/components/RuleList'
import Rule from '@/components/Rule'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/map',
      name: 'Map',
      component: Map
    }, {
      path: '/rule_list/:lat?/:lng?',
      name: 'RuleList',
      component: RuleList
    }, {
      path: '/rule/:ruleId',
      name: 'Rule',
      component: Rule
    }
  ]
})

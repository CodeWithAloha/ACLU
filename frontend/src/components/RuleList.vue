<template>
  <div class="container">

    <md-toolbar>
      <md-button class="md-icon-button">
        <md-icon>menu</md-icon>
      </md-button>

      <h2 class="md-title" style="flex: 1">Rule List</h2>
    </md-toolbar>

    <md-table v-once>
      <md-table-body>
        <md-table-row v-for="(rule, index) in rules" :key="index">
          <router-link :to="{ name: 'Rule', params: { ruleId: rule.id }}">
            <md-table-cell class="rule-name-cell">
              {{ rule.name }}
            </md-table-cell>
            <md-table-cell class="rule-status-cell">
              <md-avatar class="md-avatar-icon md-large">
                <img v-if="rule.status == 0" src="../assets/greenbox.png" alt="Avatar">
                <img v-if="rule.status == 1" src="../assets/greenbox.png" alt="Avatar">
                <img v-if="rule.status == 2" src="../assets/greenbox.png" alt="Avatar">
              </md-avatar>
            </md-table-cell>
          </router-link>
        </md-table-row>
      </md-table-body>
    </md-table>
  </div>
</template>

<script>
export default {
  name: 'RuleList',
  data () {
    return {
      rules: [
        {
          id: 1,
          name: 'Foo',
          status: 0
        }, {
          id: 2,
          name: 'Bar',
          status: 1
        }
      ]
    }
  },
  methods: {
    clicked: function () {
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .table-row {
  }
  .rule-name-cell {
    height: inherit;
    width: 75vw;
  }
  .rule-status-cell {
    height: inherit;
    width: 25vw;
  }
</style>

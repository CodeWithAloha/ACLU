<template>
  <md-table v-once>
  <md-table-body>
    <md-table-row v-for="rule in rules" :key="index">
      <md-table-cell>{{rule.name}}</md-table-cell>
      <md-table-cell>
        <md-avatar class="md-avatar-icon md-large">
          <img v-if="rule.status == 0" src="../assets/greenbox.png" alt="Avatar">
          <img v-if="rule.status == 1" src="../assets/greenbox.png" alt="Avatar">
          <img v-if="rule.status == 2" src="../assets/greenbox.png" alt="Avatar">
        </md-avatar>
      </md-table-cell>
    </md-table-row>
  </md-table-body>
</md-table>
</template>

<script>
export default {
  name: 'RuleList',
  data () {
    return {
      rules: [
        {
          name: 'Foo',
          status: 0
        }, {
          name: 'Bar',
          status: 1
        }
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

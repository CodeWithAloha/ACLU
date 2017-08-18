<template>
  <div class="container">
    <md-toolbar>
      <md-button class="md-icon-button">
        <md-icon></md-icon>
      </md-button>

      <h2 class="md-title" style="flex: 1">{{rule.name}}</h2>
    </md-toolbar>
    <div class="main-content">
      <div class="rule-name">
        <h2>{{rule.name}}</h2>
      </div>
      <div class="bill-text">
        <div class="title">
          <h4>Bill Text</h4>
        </div>
        <div class="description">
          <p>
          No person shall sit or lie on a public mall, or on a tarp, towel, sheet, blanket,
          sleeping bag, bedding, planter, chair, bench, or any other object or material
          placed upon a public mall during the following hours:
          </p>
          <p>
          (1) <b>Fort Street Mall</b>. Monday to Friday from 5:00 a.m. to 7:00 p.m.<br>
          (2) <b>Kekaulike Mall</b>. Monday to Sunday from 5:00 am. to 7:00 p.m.<br>
          (3) <b>Sun Yat Sen Mall</b>. Monday to Friday from 5:00 a.m. to 7:00 p.m.<br>
          (4) <b>Union Mall</b>. Monday to Friday from 5:00 a.m. to 7:00 p.m.<br>
          </p>
        </div>
      </div>
      <div class="ordiance">
        <div class="title">
          <h4>Ordiance</h4>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: 'Rule',
  data () {
    return {
      rule: {
        name: 'Sit Lie Ban'
      }
    }
  },
  mounted () {
    console.log(this.$route.params.ruleId)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .bill-text {
    display: inline-block;
  }
  .main-content {
    padding-left: 15%;
    padding-right: 15%;
  }
  .title {
    vertical-align: top;
    display: inline-block;
    width: 25%;
  }
  .title > h4 {
    margin: 0px;
  }
  .description {
    vertical-align: top;
    display: inline-block;
    width: 70%;
  }
  .description > p {
    margin: 0px;
    padding-bottom: 20px;
  }

</style>

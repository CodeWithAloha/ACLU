var merge = require('webpack-merge')
var devEnv = require('./dev.env')

module.exports = merge(devEnv, {
  NODE_ENV: '"testing"',
  ACLU_API_BASE_URL: '"http://localhost:50050"'
})

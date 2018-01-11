// All possible configs for different environments
const config = {
  development: {
    API_URL: "http://localhost:50050"
  },
  production: {
    API_URL: "http://localhost:50050"
  },
  default: {
    API_URL: "http://localhost:50050",
    API_TOKEN: `
pk.eyJ1IjoicnVzc2VsbHZlYTIiLCJhIjoiY2lmZzVrNWJkOWV2cnNlbTdza2thcGozNSJ9.zw6CcZLxP6lq0x-xfwp6uA`
  }
};

// The selected config (defaults to config.default)
let selected = config[process.env.NODE_ENV] || config.default;

// Exports the config, filling the possible gaps with config.default
export default {
  ...config.default,
  ...selected
};

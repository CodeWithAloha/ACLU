export default {
  Map: {
    Defaults: {
      Latitude: 21.441922,
      Longitude: -158.000072,
      Zoom: 10,
      Style: 'mapbox://styles/mapbox/streets-v9' // 'mapbox://styles/mapbox/light-v9'
    }
  },
  Settings: {
    MapBoxToken: process.env.VUE_APP_MAPBOX_TOKEN,
    ApiBasePath: process.env.VUE_APP_BASE_PATH
  }
}

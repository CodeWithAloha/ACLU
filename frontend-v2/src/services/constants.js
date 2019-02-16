export const Map = {
  Defaults: {
    Latitude: 21.441922,
    Longitude: -158.000072,
    Zoom: 10,
    Style: 'mapbox://styles/mapbox/streets-v9' // 'mapbox://styles/mapbox/light-v9'
  }
}
export const Settings = {
  MapBoxToken: process.env.VUE_APP_MAPBOX_TOKEN,
  ApiBasePath: process.env.VUE_APP_BASE_PATH
}

export const FeatureType = {
  Park: 'PARK',
  Tmk: 'TMK'
}

export const OpenStatus = {
  Open: 'OPEN',
  ClosingSoon: 'CLOSING_SOON',
  Closed: 'CLOSED',
  Unknown: 'UNKNOWN'
}

export const Colors = {
  Restricted: '#ff4136',
  Permitted: '#2ecc40',
  Unknown: 'GREY',
  Warning: '#ffff00',
  LayerBorder: '#ffffff'
}

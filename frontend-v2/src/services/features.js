import Feature from '@/models/Feature'
import { Settings } from '@/services/constants'
import Axios from 'axios'

export default {
  /**
   * Returns features near to the given position.
   */
  getFeaturesNearBy: async (lat, lon, radius = 500) => {
    const geoQuery = {
      'geojson.geometry': {
        $near: {
          $geometry: {
            type: 'Point',
            coordinates: [lon, lat]
          },
          $maxDistance: radius
        }
      }
    }
    const url = `${Settings.ApiBasePath}/features/?where=${JSON.stringify(
      geoQuery
    )}`
    let response = await Axios.get(url)
    let features = parseFeatures(response.data._items)
    while (response.data._links.next) {
      response = await Axios.get(`${Settings.ApiBasePath}/${response.data._links.next.href}`)
      features = features.concat(parseFeatures(response.data._items))
    }
    return features
  }
}

function parseFeatures (features) {
  return features.map(item => new Feature(item))
}

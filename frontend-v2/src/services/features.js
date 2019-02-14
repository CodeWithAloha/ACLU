import Feature from '@/models/Feature';
import { Settings } from '@/services/constants';
import Axios from 'axios';

export default {
  /**
   * Returns features near to the given position.
   */
  getFeaturesNearBy: async (pos, radius = 10000) => {
    const geoQuery = {
      'geojson.geometry': {
        $near: {
          $geometry: {
            type: 'Point',
            coordinates: [pos.longitude, pos.latitude]
          },
          $maxDistance: radius
        }
      }
    }
    const url = `${Settings.ApiBasePath}/features/?where=${JSON.stringify(
      geoQuery
    )}`
    let response = await Axios.get(url)
    const features = parseFeatures(response.data._items)
    while (response.data._links.next) {
      response = await Axios.get(`${Settings.ApiBasePath}/${response.data._links.next.href}`)
      features.concat(parseFeatures(response.data._items))
    }
    return features
    // if () {
    //   return this.getLayerData(url, map);
    // }
  }
}

function parseFeatures (features) {
  console.log(features)
  return features.map(item => new Feature(item))
}

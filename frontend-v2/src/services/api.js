import axios from 'axios'
const API_BASE = process.env.ACLU_API_BASE_URL

export default {
  getFeaturesNearBy: getFeaturesNearBy
}

/**
 * Returns a list of features near by a given geo point
 * @param {number} lat Latitude
 * @param {number} long Longitude
 * @param {number} distance Radius to find features in
 */
function getFeaturesNearBy (lat, long, distance) {
  const query = {
    'geojson.geometry': {
      $near: {
        $geometry: {
          type: 'Point',
          coordinates: [long, lat]
        },
        $maxDistance: distance
      }
    }
  }
  const url = `${API_BASE}//features/?where=${JSON.stringify(query)}`
  axios.get(url)
}

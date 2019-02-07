import Constants from '@/services/constants'
import Axios from 'axios'

export default {
  getFeaturesNearBy: (pos, radius) => {
    const geoQuery = {
      'geojson.geometry': {
        $near: {
          $geometry: {
            type: 'Point',
            coordinates: [pos.longitude, pos.latitude]
          },
          $maxDistance: this.maxDistance
        }
      }
    }
    const url = `${Constants.Settings.ApiBasePath}/features/?where=` + JSON.stringify(geoQuery)
    return Axios.get(url).then(response => {
      const features = response.data._items.map(item =>
        this.FeatureFactory.createFeature(item)
      )
      this.setLayers(features, map)
      if (response.data._links.next) {
        var url =
          process.env.ACLU_API_BASE_URL + '/' + response.data._links.next.href
        return this.getLayerData(url, map)
      }
    })
  }
}

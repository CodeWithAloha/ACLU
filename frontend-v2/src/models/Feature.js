import { getFeatureStatus } from './FeatureStatus'

export default class {
  constructor (feature) {
    // Take all properties from feature
    for (let property in feature) {
      if (!feature.hasOwnProperty(property)) continue
      this[property] = feature[property]
    }
  }

  async getStatus () {
    if (this.status) return this.status
    return getFeatureStatus(this)
  }
}

import Axios from 'axios'
import { RestrictionState, RestrictionStateType } from './RetrictionState'

export const FeatureTypes = {
  Park: 'PARK',
  Tmk: 'TMK'
}

export class FeatureFactory {
  createFeature (feature) {
    switch (feature.type.toUpperCase()) {
      case FeatureTypes.Park:
        return new ParkFeature(feature)
      case FeatureTypes.Tmk:
        return new TmkFeature(feature)
      default:
        console.log('Unknown feature type: ' + feature.type)
        break
    }
  }
}

export class ParkFeature {
  constructor (feature) {
    // Take all properties from feature
    for (var property in feature) {
      if (!feature.hasOwnProperty(property)) continue

      this[property] = feature[property]
    }
  }
  getRestrictionState () {
    if (this.restrictionState) return this.restrictionState
    const href =
      'https://api.aclu.codeforhawaii.org/feature_park_restrictions/?where={"feature_id":"###FEATURE_ID###"}'
    return Axios.get(href.replace('###FEATURE_ID###', this._id))
      .then(response => {
        const restrictions = response.data._items.length > 0 ? response.data._items[0].restrictions : undefined
        const now = new Date()
        const currentTime = now.getHours() * 100 + now.getMinutes() // format time as 2359
        if (restrictions &&
          currentTime > restrictions.hours_start &&
          currentTime < restrictions.hours_end) {
          this.restrictionState = new RestrictionState(
            RestrictionStateType.Invalid,
            'LOREM IPSUM'
          )
        } else {
          this.restrictionState = new RestrictionState(
            RestrictionStateType.Valid,
            'LOREM IPSUM'
          )
        }
        return this.restrictionState
      })
      .catch(err => {
        console.log('Unable to parse restrictions for feature: ' + this._id)
        console.log(err)
        return new RestrictionState(
          RestrictionStateType.Valid,
          'LOREM IPSUM'
        )
      })
  }
}

export class TmkFeature {
  constructor (feature) {
    // Take all properties from feature
    for (var property in feature) {
      if (!feature.hasOwnProperty(property)) continue

      this[property] = feature[property]
    }
  }

  getRestrictionState () {
    this.restrictionState = new RestrictionState(RestrictionStateType.Invalid, 'LOREM IPSUM')
    return Promise.resolve(this.restrictionState)
  }
}

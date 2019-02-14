import { FeatureType, OpenStatus, Settings } from '@/services/constants';
import Axios from 'axios';
import moment from 'moment';

export const getFeatureStatus = async feature => {
  switch (feature.type.toUpperCase()) {
    case FeatureType.Park:
      return getParkStatus(feature)
    case FeatureType.Tmk:
      return getTmkStatus(feature)
    default:
      console.log(
        `Can't get restriction state for feature type: ${feature.type}`
      )
      return OpenStatus.Unknown
  }
}

async function getTmkStatus (tmkFeature) {
  return OpenStatus.Closed
}
async function getParkStatus (parkFeature) {
  const query = {
    feature_id: parkFeature._id
  }
  const url = `${Settings.ApiBasePath}
  /feature_park_restrictions/?where=${JSON.stringify(query)}`
  try {
    const response = await Axios.get(url)
    const restrictions =
      response.data._items.length > 0
        ? response.data._items[0].restrictions
        : undefined

    // Check if park is opened
    return getOpenStatus(restrictions)
  } catch (error) {
    console.log('Unable to parse open status for feature: ' + parkFeature._id)
    console.log(error)
    return OpenStatus.Unknown
  }
}

/**
 * Indicates if a feature is Open, Closed, or ClosingSoon
 * @param {object} restrictions Restrictions object containing hours start and end
 * @param {number} closingWindow [OPTIONAL] Indicates what is the threshold for ClosingSoon state. Defaults to 15
 */
function getOpenStatus (restrictions, closingWindow = 15) {
  /*
    Open hours come in HHmm format (ie. 2359).
    Need to extract it and convert it to an actual date
  */
  const startHour = restrictions.hours_start.substring(0, 2)
  const startMin = restrictions.hours_start.substring(2, 2)
  const endHour = restrictions.hours_end.substring(0, 2)
  const endMin = restrictions.hours_end.substring(2, 2)
  const now = moment()
  const openedAt = now.setHours(startHour, startMin)
  // here it gets complicated with the time going after midnight (ie. 01:30 AM)
  // since that falls into tomorrow's day
  let closesAt = now.setHours(endHour, endMin)
  if (closesAt < openedAt) closesAt = moment(closesAt).add(1, 'days')
  // Check if park is opened
  if (restrictions && now > openedAt && now < closesAt) {
    // Check to see if park is closing soon
    if (closesAt.diff(now, 'minutes') <= closingWindow) {
      return OpenStatus.ClosingSoon
    } else {
      return OpenStatus.Open
    }
  } else {
    return OpenStatus.Closed
  }
}

export default {
  getCurrentPosition: options => {
    return new Promise((resolve, reject) => {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(resolve, reject, options)
      } else {
        reject(new Error('Your device does not support Geo Locations'))
      }
    })
  }
}

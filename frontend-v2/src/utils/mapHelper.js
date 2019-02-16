import { Colors, OpenStatus } from '@/services/constants'
export default {
  getFeatureLayer: async (feature) => {
    return {
      id: feature._id,
      type: 'fill',
      paint: {
        'fill-color': getLayerColor(await feature.getStatus()),
        'fill-opacity': 0.5,
        'fill-outline-color': Colors.LayerBorder
      },
      source: {
        type: 'geojson',
        data: feature.geojson
      }
    }
  }
}

function getLayerColor (status) {
  switch (status) {
    case OpenStatus.Open:
      return Colors.Permitted
    case OpenStatus.ClosingSoon:
      return Colors.Warning
    case OpenStatus.Closed:
      return Colors.Restricted
    default:
      return Colors.Unknown
  }
}

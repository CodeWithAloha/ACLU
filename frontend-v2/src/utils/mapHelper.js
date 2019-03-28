import { Colors, OpenStatus } from '@/services/constants'

/*
  MapBox uses expressions to conditional color/render features.
  See the following url for an example of working expressions
  https://docs.mapbox.com/mapbox-gl-js/example/data-join/
*/
export const MapBoxColorExpression = [
  'match',
  ['get', 'condition'],
  OpenStatus.Open,
  Colors.Permitted,
  OpenStatus.ClosingSoon,
  Colors.Warning,
  OpenStatus.Closed,
  Colors.Restricted,
  /* defaulr color */ Colors.Unknown
]

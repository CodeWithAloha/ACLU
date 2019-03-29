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

export const Patterns = {
  GreenPattern: require('@/assets/pattern-square-8-8.png'),
  RedPattern: require('@/assets/pattern-circle-4-4.png'),
  YellowPattern: require('@/assets/pattern-diagonal-8-8.png')
}

export const MapBoxPatternExpression = [
  'match',
  ['get', 'condition'],
  OpenStatus.Open,
  'GreenPattern',
  OpenStatus.ClosingSoon,
  'YellowPattern',
  OpenStatus.Closed,
  'RedPattern',
  /* defaulr color */ Colors.Unknown
]

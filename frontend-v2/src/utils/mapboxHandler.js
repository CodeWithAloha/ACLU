import { Colors, Settings } from '@/services/constants'
import FeatureService from '@/services/features'
import { MapBoxColorExpression, MapBoxPatternExpression, Patterns } from '@/utils/mapHelper'
import EventEmitter from 'events'
import MapboxGeocoder from 'mapbox-gl-geocoder'
export const MapboxHandlerEvents = {
  MapLoading: 'MAPBOX_HANDLER_MAP_LOADING',
  MapLoaded: 'MAPBOX_HANDLER_MAP_LOADED',
  FeaturesLoading: 'MAPBOX_HANDLER_FEATURES_LOADING',
  FeaturesLoaded: 'MAPBOX_HANDLER_FEATURES_LOADED',
  FeatureSelected: 'MAPBOX_HANDLER_FEATURE_SELECTED'
}
export class MapboxHandler extends EventEmitter {
  constructor (mapRef, vuexStore) {
    super()
    this.mapRef = mapRef
    this.storeRef = vuexStore
    // A unique id for current map state
    this.id = Date.now().toString()
    this.geocoder = null
    this.selectedFeature = null
    this.loading = false
  }

  async loadMapboxWidgets () {
    this.emit(MapboxHandlerEvents.MapLoading)
    // Geocoder (Search Bar)
    // TODO: It'd be nice if we can make this its own controller
    // Limit results to hawaii only
    const bboxHawaii = [-160.3, 16.7, -151.8, 23.3]
    this.geocoder = new MapboxGeocoder({
      accessToken: Settings.MapBoxToken,
      bbox: bboxHawaii
    })
    this.geocoder.on('result', async ev => {
      const [lon, lat] = ev.result.geometry.coordinates
      await this.loadFeatures(lat, lon)
    })
    document
      .getElementById('geocoder')
      .appendChild(this.geocoder.onAdd(this.mapRef))

    // Load patterns for layers
    await Promise.all([
      new Promise((resolve, reject) => {
        this.mapRef.loadImage(Patterns.GreenPattern, (err, img) => {
          if (err) reject(err)
          this.mapRef.addImage('GreenPattern', img)
          resolve()
        })
      }),
      new Promise((resolve, reject) => {
        this.mapRef.loadImage(Patterns.RedPattern, (err, img) => {
          if (err) reject(err)
          this.mapRef.addImage('RedPattern', img)
          resolve()
        })
      }),
      new Promise((resolve, reject) => {
        this.mapRef.loadImage(Patterns.YellowPattern, (err, img) => {
          if (err) reject(err)
          this.mapRef.addImage('YellowPattern', img)
          resolve()
        })
      })
    ])
    this.emit(MapboxHandlerEvents.MapLoaded)
  }

  async loadFeatures (lat, lon) {
    this.emit(MapboxHandlerEvents.FeaturesLoading)
    // TODO: Yield features instead of return whole array (since it requires multiple requests)
    const features = await FeatureService.getFeaturesNearBy(lat, lon)
    for (const f of features) {
      if (!this.storeRef.state.renderedFeatures[f._id]) {
        const geo = f.geojson
        geo.properties.condition = await f.getStatus()
        geo.properties.id = f._id
        // Keep a "set" of all distinct rendered features so we don't render them twice
        this.storeRef.state.renderedFeatures[f._id] = geo
      }
    }
    // Render all features
    this.renderFeatures(Object.values(this.storeRef.state.renderedFeatures))

    this.emit(MapboxHandlerEvents.FeaturesLoaded)
  }

  renderFeatures (features) {
    if (this.mapRef.getSource(this.id)) {
      try {
        // If we have sources and layers loaded remove them
        this.mapRef.removeSource(this.id)
        this.mapRef.removeLayer(`${this.id}-pattern`)
        this.mapRef.removeLayer(`${this.id}-color`)
        this.mapRef.removeLayer(`${this.id}-selected`)
      } catch (error) {
        // swallow
        console.log(error)
      }
    }

    // Create a new id
    // When we remove a source and add it again with the same id it won't refresh
    this.id = Date.now().toString()
    this.mapRef.addSource(this.id, {
      type: 'geojson',
      data: {
        type: 'FeatureCollection',
        features: features
      }
    })

    this.mapRef.addLayer({
      id: `${this.id}-pattern`,
      type: 'fill',
      source: this.id,
      minzoom: 14,
      paint: {
        'fill-pattern': MapBoxPatternExpression
      },
      filter: ['==', '$type', 'Polygon']
    })

    this.mapRef.addLayer({
      id: `${this.id}-color`,
      type: 'fill',
      source: this.id,
      paint: {
        'fill-color': MapBoxColorExpression,
        'fill-opacity': 0.3,
        'fill-outline-color': Colors.LayerBorder
      },
      filter: ['!in', 'id']
    })

    this.mapRef.addLayer({
      id: `${this.id}-selected`,
      type: 'fill',
      source: this.id,
      paint: {
        'fill-color': MapBoxColorExpression,
        'fill-opacity': 0.8
      },
      filter: ['in', 'id']
    })

    const selectFeatureClick = e => {
      this.selectedFeature = e.features[0]
      this.mapRef.setFilter(`${this.id}-selected`, [
        'in',
        'id',
        this.selectedFeature.properties.id
      ])
      this.mapRef.setFilter(`${this.id}-color`, [
        '!in',
        'id',
        this.selectedFeature.properties.id
      ])
      this.emit(MapboxHandlerEvents.FeatureSelected, this.selectedFeature.properties.id)
    }
    // Select feature on click
    this.mapRef.on('click', `${this.id}-color`, selectFeatureClick)
    // this.mapRef.on("click", `${this.id}-pattern`, selectFeatureClick);
  }
}

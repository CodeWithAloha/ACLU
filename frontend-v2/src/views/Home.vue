<template>
  <Map :splash="splash"></Map>
</template>

<script>
import Map from '@/components/Map'

export default {
  name: 'Home',
  components: {
    Map
  },
  props: ['splash']
}
</script>

<template>
  <div class="restriction">
    <div @click="$emit('close')" class="toggle">
      <md-icon class="md-size-2x">arrow_drop_down</md-icon>
    </div>
  </div>
</template>

<script>
export default {
  name: "RestrictionSlide"
};
</script>

<style scoped>
.restriction {
  background: white;
  position: fixed;
  height: 50vh;
  width: 100%;
  z-index: 3;
  top: 50vh;
}

.toggle {
  background: var(--md-theme-default-primary);
  display: flex;
  align-items: center;
}
</style>

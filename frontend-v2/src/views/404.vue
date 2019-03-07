<template>
  <div class="NotFound">
    <h1>404</h1>
    <p class="subtitle">
      Page not found.
    </p>
    <p class="info">
      The page doesn't exist. Please double check the URL.
    </p>
  </div>
</template>

<script>
export default {
  name: '404'
}
</script>

<style lang="scss">
  .NotFound {
    h1 {
      font-size: 5rem;
    }
    .subtitle {
      font-size: 2rem;
    }
    .info {
      font-size: 3rem;
    }
  }
</style>

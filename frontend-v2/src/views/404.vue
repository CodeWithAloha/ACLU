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
    text-align: center;
    padding: 3rem;
    h1 {
      font-size: 10rem;
      color: var(--md-theme-default-primary, #448aff);
    }
    .subtitle {
      font-size: 1.5rem;
      line-height: 1.5rem;
    }
    .info {
      font-size: 1.75rem;
      line-height: 1.75rem;
    }
  }
</style>

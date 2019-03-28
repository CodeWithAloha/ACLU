<template>
  <div class="SplitTemplate">
    <div class="Header">
      <div class="Title">
        <slot name="title" />
      </div>
      <div class="Subtitle">
        <slot name="subtitle" />
      </div>
    </div>
    <div class="Body">
      <slot name="body" />
    </div>
    <div class="Footer">
      <md-button v-if="back" @click="back()">Back</md-button>
      <span style="flex: 1" />
      <md-button @click="next()">{{ nextText || "Next" }}</md-button>
    </div>
  </div>
</template>

<script>
export default {
  props: ['next', 'back', 'nextText']
}
</script>

<style lang="scss">
  .Title {
    color: white;
    text-align: center;
    font-weight: heavy;
    font-size: 3rem;
    line-height: 3rem;
    margin-bottom: 3rem;
  }

  .Subtitle {
    color: white;
    text-align: center;
    font-size: 1.5rem;
    line-height: 1.5rem;
    font-weight: 100;
  }

  .SplitTemplate {
    display: flex;
    flex-direction: column;
    flex: 1;
  }

  .Header {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 35vh;
    padding: 0.5rem;
    background-image: linear-gradient(130deg, #30a5e8, #3067e8);
  }

  .Body {
    display: flex;
    flex-direction: column;
    align-items: center;
    flex: 1;
    padding: 1.5rem;
    font-size: 1rem;
  }

  .Footer {
    display: flex;
  }
</style>

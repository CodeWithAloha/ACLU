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
      <md-button>Next</md-button>
    </div>
  </div>
</template>


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
    height: 40vh;
    padding: 0.5rem;
    background-image: linear-gradient(130deg, #30a5e8, #3067e8);
  }

  .Body {
    display: flex;
    flex-direction: column;
    align-items: center;
    flex: 1;
  }

  .Footer {
    display: flex;
    justify-content: flex-end;
  }

</style>
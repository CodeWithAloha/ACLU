<template>
<carousel :per-page="1" :navigate-to="someLocalProperty" mouse-drag="false">
    <slide>
      <img src="../assets/walk.png" class="red">
    </slide>
    <slide>
      <img src="../assets/howitworks.png" class="red">
    </slide>
    <slide>
      <img src="../assets/howitworks2.png" class="red">
    </slide>
    <slide>
      <img src="../assets/restricted.png" class="red">
    </slide>
    <slide>
      <img src="../assets/conditional.png" class="red">
    </slide>
    <slide>
      <img src="../assets/permitted.png" class="red">
    </slide>
    <slide>
      <img src="../assets/unknown.png" class="red">
    </slide>
    <slide>
      <img src="../assets/moredetails.png" class="red">
    </slide>
    <slide>
      <img src="../assets/goodtogo.png" class="red">
    </slide>
  </carousel>
</template>
<style>
.red {
  width: 187.5px;
  height: 157.5px;
  object-fit: contain;
}
</style>
<template>
	<div class="splash" @click="hide">
		<div>
			<img class="logo" src="../assets/holoholo-logo@3x.png" alt="Holo Holo">
		</div>
		<div class="ribbon">
			<img src="../assets/brand-ribbon.svg" alt="ACLU | Code for Hawaii">
		</div>
	</div>
</template>

<script>
export default {
  name: "splash",
  components: {},
  mounted: function() {
    setTimeout(() => {
      this.hide();
    }, 5000);
  },
  methods: {
    hide: function() {
      this.$router.push("/");
    }
  }
};
</script>

<style>
.splash {
  background: url("../assets/splash-desktop.jpg") no-repeat center center fixed;
  background-size: cover;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}
@media (min-width: 320px) and (max-width: 767px) {
  .splash {
    background: url("../assets/splash-mobile.jpg") no-repeat center center fixed;
  }
}

.logo {
  margin-top: -150px;
}
.ribbon {
  position: absolute;
  bottom: 50px;
  background-color: #4e82ed;
  width: 100%;
}
</style>

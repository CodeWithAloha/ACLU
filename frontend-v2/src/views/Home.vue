<template>
  <div class="page-container md-layout-column">
    <md-toolbar class="md-primary">
      <md-button class="md-icon-button" @click="showNavigation = true">
        <md-icon>menu</md-icon>
      </md-button>
      <span class="md-title">My Title</span>

      <div class="md-toolbar-section-end">
        <md-button @click="showSidepanel = true">Favorites</md-button>
      </div>
    </md-toolbar>

    <md-drawer :md-active.sync="showNavigation">
      <md-toolbar class="md-transparent" md-elevation="0">
        <span class="md-title">MENU</span>
      </md-toolbar>

      <md-list>
        <md-list-item>
					<router-link to="/about">
						<md-icon>bookmarks</md-icon>
						<span class="md-list-item-text">about holo holo</span>
					</router-link>
        </md-list-item>

        <md-list-item>
					<a href="https://acluhi.org/" target="_blank">
						<md-icon>bookmarks</md-icon>
						<span class="md-list-item-text">aclu initiatives</span>
					</a>
        </md-list-item>

        <md-list-item>
					<a href="https://www.codeforhawaii.org/" target="_blank">
						<md-icon>bookmarks</md-icon>
						<span class="md-list-item-text">code for hawaii</span>
					</a>
        </md-list-item>

        <md-list-item>
					<router-link to="/report_feedback">
						<md-icon>feedback</md-icon>
						<span class="md-list-item-text">report feedback</span>
					</router-link>
        </md-list-item>

        <md-list-item>
					<router-link to="/settings">
						<md-icon>build</md-icon>
						<span class="md-list-item-text">settings</span>
					</router-link>
        </md-list-item>
      </md-list>
    </md-drawer>

    <md-content>
    </md-content>
  </div>
</template>

<script>
export default {
  name: "Temporary",
  data: () => ({
    showNavigation: false,
    showSidepanel: false
  })
};
</script>

<style lang="scss" scoped>
.page-container {
  height: 100vh;
  overflow: hidden;
  position: relative;
  border: 1px solid rgba(#000, 0.12);
}

.md-drawer,
.md-drawer .md-list {
  background-color: #ef5269;
}
.md-drawer .md-list-item {
  margin-top: 20px;
}
.md-drawer .md-title {
  font-size: 30px;
  font-weight: 800;
  margin-top: 50px;
  margin-left: 30px;
}
.md-drawer .md-list {
  margin-left: 30px;
  margin-top: 30px;
}
.md-drawer .md-icon,
.md-drawer .md-title,
.md-drawer .md-list-item-text {
  color: #eaeaea !important;
}
.md-drawer .md-icon {
  margin-right: 15px !important;
}
.md-drawer .md-list-item-text {
  font-family: Roboto;
  font-size: 22px;
  font-weight: 300;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: 2px;
}
.md-list-item a {
	text-decoration: none;
	display: flex;
}
.md-content {
  padding: 16px;
}
</style>
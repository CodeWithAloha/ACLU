<template>
  <div>
    <md-toolbar class="md-primary">
      <div class="md-layout md-alignment-center-center">
        <div class="md-layout-item menu">
          <md-button class="md-icon-button" @click="showNavigation=true">
            <md-icon>menu</md-icon>
          </md-button>
        </div>
        <div class="md-layout-item title">
          <span class="md-title">Holo Holo</span>
        </div>
        <div class="md-layout-item search">
          <md-button class="md-icon-button" @click="showSearch=true">
            <md-icon>search</md-icon>
          </md-button>
        </div>
      </div>
    </md-toolbar>
    <md-drawer :md-active.sync="showNavigation">
      <md-toolbar class="md-transparent" md-elevation="0">
        <span class="md-title">MENU</span>
      </md-toolbar>

      <md-list>
        <md-list-item @click="showNavigation=false">
          <router-link to="/">
            <md-icon>map</md-icon>
            <span class="md-list-item-text">home</span>
          </router-link>
        </md-list-item>

        <md-list-item @click="showNavigation=false">
          <router-link to="/about">
            <md-icon>info</md-icon>
            <span class="md-list-item-text">about holo holo</span>
          </router-link>
        </md-list-item>

        <md-list-item @click="showNavigation=false">
          <a href="https://acluhi.org/" target="_blank">
            <md-icon>launch</md-icon>
            <span class="md-list-item-text">aclu initiatives</span>
          </a>
        </md-list-item>

        <md-list-item @click="showNavigation=false">
          <a href="https://www.codeforhawaii.org/" target="_blank">
            <md-icon>launch</md-icon>
            <span class="md-list-item-text">code for hawaii</span>
          </a>
        </md-list-item>

        <md-list-item @click="showNavigation=false">
          <router-link to="/report-feedback">
            <md-icon>feedback</md-icon>
            <span class="md-list-item-text">report feedback</span>
          </router-link>
        </md-list-item>

        <md-list-item @click="showNavigation=false">
          <router-link to="/settings">
            <md-icon>build</md-icon>
            <span class="md-list-item-text">settings</span>
          </router-link>
        </md-list-item>
      </md-list>

      <Ribbon/>
    </md-drawer>
  </div>
</template>

<script>
import Ribbon from '@/components/Ribbon'

export default {
  name: 'NavBar',
  components: {
    Ribbon
  },
  data: () => ({
    showNavigation: false,
    showSidepanel: false
  })
}
</script>

<style lang="scss" scoped>
.md-toolbar .md-layout {
  width: 100%;
}
.menu {
  text-align: left;
}

.title {
  text-align: center;
}

.search {
  text-align: right;
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
</style>

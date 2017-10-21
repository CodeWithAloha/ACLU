import Vue from "vue";
import Router from "vue-router";
import Admin from "@/components/Admin";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/admin",
      name: "Admin",
      component: Admin
    }
  ]
});

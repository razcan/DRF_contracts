<template>
  <div>
    <b-navbar toggleable="md" type="dark" variant="dark">
      <div class="container">
        <b-navbar-brand to="/">CMS</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <!-- <b-navbar-nav>
            <b-button size="sm" v-if="isLoggedIn" to="/create" class="btn btn-success">
              <i class="fa fa-plus" aria-hidden="true"></i> Ask Question
            </b-button>
            <b-button size="sm" v-else to="/login" class="btn btn-success">
              <i class="fa fa-plus" aria-hidden="true"></i> Ask Question
            </b-button>
          </b-navbar-nav> -->

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-item to="/contracts">Contracts </b-nav-item>
            <!-- <b-nav-item to="/categories">Categories</b-nav-item>
            <b-nav-item to="/questions">Questions</b-nav-item> -->
            <b-nav-item to="/login" v-if="!isLoggedIn">Login</b-nav-item>
            <b-nav-item to="/register" v-if="!isLoggedIn">Register</b-nav-item>

            <b-nav-item-dropdown v-if="isLoggedIn" right>
              <!-- Using 'button-content' slot -->
              <template v-slot:button-content>
                <b>{{ authUser.username }}</b>
              </template>
              <b-dropdown-item :to="{ name: 'profile', params: { name: authUser.username }}">Profile</b-dropdown-item>
              <b-dropdown-item @click="logout">Logout</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </div>
    </b-navbar>
    <router-view></router-view>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  data() {
    return {
      get token() {
        return localStorage.getItem("token") || 0;
      }
    };
  },
  computed: {
    ...mapGetters(["isLoggedIn", "authUser"])
  },
  methods: {
    logout: function() {
      this.$store.dispatch("logout").then(() => {
        this.$router.push("/");
      });
    }
  }
};
</script>

<style lang="css">
.bg-dark {
  margin-top: -30px;
}
.ml-auto li {
  display: inline-block;
  margin: 2px;
}
</style>

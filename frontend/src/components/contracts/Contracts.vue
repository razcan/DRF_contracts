<template>
  <div class="container">
    <div class="col-md-8 offset-md-2">
          <p>Contracts List</p>
    </div>
    <div class="vld-parent">
      <loading :active.sync="isLoading" :is-full-page="fullPage" :opacity="1"></loading>
    </div>
  </div>
</template>

<script>
import axios from "axios";
// Import component
import Loading from "vue-loading-overlay";
// Import stylesheet
import "vue-loading-overlay/dist/vue-loading.css";

export default {
  data() {
    return {
      isLoading: true,
      fullPage: true,
      tags: []
    };
  },
  components: {
    Loading
  },
  methods: {
    getTags() {
      axios
        .get("/api/categories")
        .then(res => {
          this.tags = res.data;
          this.isLoading = false;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
          this.isLoading = false;
        });
    }
  },
  created() {
    this.getTags();
  }
};
</script>

<style lang="css">
.btn {
  margin: 5px 5px;
}
</style>
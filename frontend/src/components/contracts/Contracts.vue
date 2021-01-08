<template>
  <div class="container">
    <div class="col-md-8 offset-md-2">
          <p>Contracts List</p>     
          <p>{{ auth }}</p>
          <p>{{ contracts }}</p>
          <ul id="example-1">
            <li v-for="item in contracts" :key="item.id">
              {{ item.id }}
            </li>
          </ul>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import axios from "axios";
// Import component
// import Loading from "vue-loading-overlay";
// Import stylesheet
// import "vue-loading-overlay/dist/vue-loading.css";

export default {
  data() {
    return {
      contracts: [],
      isLoading: true,
      fullPage: true,
      tags: [],      
      token2: [],
      prefix: [],
      auth: []
    };
  },
   computed: {
    ...mapGetters(["isLoggedIn", "authUser"])
  },
  methods: {    
    getContracts() {
      this.token2 = this.$store.state.token;
      this.prefix = 'Token ';
      this.auth = `${this.prefix}${this.token2.auth_token}`;
      // console.log(this.auth);
      axios
        .get("/api/contracts", 
        { headers: { 
          'Authorization': this.auth
                   } 
        })
        .then(res => {
          this.contracts = res.data.results;
          this.isLoading = false;
        })
        .catch(error => {
          console.error(error);
          this.isLoading = false;
        });
    }
  },
  created() {
    this.getContracts();
  }
};
</script>

<style lang="css">
.btn {
  margin: 5px 5px;
}
</style>



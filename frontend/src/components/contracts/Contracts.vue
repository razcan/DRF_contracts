<template>
  <div class="container">
    <div class="col-md-8 offset-md-2">
          <p>Contracts List</p>     
          <p>{{ auth }}</p>
          <p>{{ contracts }}</p>
          <ul id="example-1">
            <li v-for="item in items" :key="item.message">
              {{ item.message }}
            </li>
          </ul>
          <div class="col-md-12" v-for="(item, index) in list_contracts" :key="index">
            <span>
              <i>{{ item.id }}</i> 
              <b>{{ item.number }}</b>
              <b>{{ item.code }}</b>
              <b></b>
            </span>
          </div>
           <!-- <button class="btn btn-link" @click="getContracts">Afiseaza</button> -->
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
      isLoading: true,
      fullPage: true,
      tags: [],      
      token2: [],
      prefix: [],
      auth: [],    
      list_contracts: []
    };
  },
   computed: {
    ...mapGetters(["isLoggedIn", "authUser"])
  },
  methods: {    
    getContracts() {
      this.isLoading = false;
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
          this.list_contracts = res.data;
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



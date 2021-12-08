<template>
    <div class="columns">
      <div class="column">
        <form v-on:submit.prevent="search_room" method="get">
          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">
              {{ error }}
            </p>
          </div>
          <hr v-if="errors.length" />
          <div class="field">
            <div class="control">
              <input
                type="text"
                city="city"
                id="city"
                class="input is-success"
                v-model="city"
                placeholder="City"
                autocapitalize="off"
                autocomplete="off"
              />
            </div>
          </div>
        </form>
      </div>
    </div>
</template>

<style>
@import "../assets/fontawesome/css/all.min.css";
</style>

<script>
export default {
  name: "SearchComponent",
  data() {
    return {
      errors: [],
      city: "",
    };
  },
  mounted() {},
  methods: {
    search_room() {
      this.errors = [];
      if (this.city === "" || this.city.length < 3) {
        this.errors.push("آخه از کجا بدونم چی بگردم؟");
      }
      if (!this.errors.length) {
        this.$store.commit("start_search", this.city);
        this.$router.push({
          name: "SearchResult",
        });
      }
    },
    view_compare() {
      this.$router.push({
        name: "Compare",
      });
    },
  },
};
</script>

<template>
  <section class="section is-large has-text-centered">
    <h1 class="title is-1">Title</h1>
    <div class="container">
      <div class="columns">
        <div class="column is-4 is-offset-4">
          <SearchComponent />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
// import SearchComponent from "@/components/SearchComponent.vue";
export default {
  // layout: "default",
  head() {
    return {
      title: "Homepage",
    };
  },
  name: "Home",
  // components: {
  //   SearchComponent,
  // },
};
</script>

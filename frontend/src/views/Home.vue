<template>
  <div class="home">
    <section class="section is-large has-text-centered">
      <h1 class="title is-1 pr-5">Title<i class="fas fa-2x fa-home"></i></h1>
      <div class="columns">
        <div class="column is-4"></div>
        <div class="column is-4">
          <SearchComponent />
        </div>
        <div class="column is-4"></div>
      </div>
    </section>
    <!-- <div class="sliding-background"></div> -->
  </div>
</template>

<style scoped>
body {
  height: 100vh;
  background-image: linear-gradient(-45deg, #f93d66, #6d47d9, #ec2f7e, #44ffff);
  background-size: 400% 400%;
  position: relative;
  animation: backslide 30s ease-in-out infinite;
}

.sliding-background {
  position: absolute;
  background: url("../assets/images/background.png") repeat-x;
  background-size: contain;
  height: 20%;
  width: 100%;
  -webkit-animation: slide 60s linear infinite;
  animation: slide 60s linear infinite;
}

@-webkit-keyframes slide {
  0% {
    transform: translate3d(0, 0, 0);
  }
  100% {
    transform: translate3d(-1692px, 0, 0);
  }
}

@keyframes slide {
  0% {
    transform: translate3d(0, 0, 0);
  }
  100% {
    transform: translate3d(-100%, 0, 0);
  }
}

@keyframes backslide {
  0% {
    background-position: 0 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0 50%;
  }
}
</style>

<script>
import SearchComponent from "@/components/SearchComponent.vue";
export default {
  name: "Home",
  components: {
    SearchComponent,
  },
};
</script>

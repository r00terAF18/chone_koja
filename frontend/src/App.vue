<template>
  <router-view />
</template>

<style>
@import "../node_modules/bulma/css/bulma-rtl.min.css";
@font-face {
  font-family: 'Vazir';
  src: url("../src/assets/fonts/Vazir.ttf") format("truetype");
}
html {
  direction: rtl;
}
body {
  font-family: 'Vazir', Helvetica, Georgia, 'Times New Roman', Times, serif;
}
</style>

<script>
export default {
  name: "App",
};
</script>

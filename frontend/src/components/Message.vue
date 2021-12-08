<template>
  <div v-if="messageActive" class="columns mt-3 mr-3" style="z-index: 9999999">
    <div class="column is-3 is-offset-9">
      <div class="notification">
        <button @click="closeMessage" class="delete"></button>
        {{ message }}
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
export default defineComponent({
  name: "Message",
  data() {
    return {
      messageActive: true,
    };
  },
  props: {
    type: String,
    message: String,
  },
  methods: {
    closeMessage() {
      this.messageActive = !this.messageActive;
      this.$store.commit("removeMessage");
    },
  },
  mounted() {
    document.querySelector(".notification").classList.toggle(this.type);
  },
});
</script>

<template>
  <div class="room_card">
    <div class="box">
      <div class="room_card_image">
        <img
          width="200"
          src="https://randomwordgenerator.com/img/picture-generator/57e6d34b4a50b10ff3d8992cc12c30771037dbf85254794177277ddd924f_640.jpg"
          alt=""
        />
      </div>
      <h3>{{ room.title }}</h3>
      <div class="columns mt-2">
        <div class="column">
          <a :href="room.link_to_site" class="button is-small is-link is-outlined"
            >مشاهده</a
          >
        </div>
        <div class="column">
          <p>{{ room.rating }}</p>
          <p>{{ room.price_per_night }}</p>
        </div>
        <div class="column">
          <button
            @click="add_to_compare(room.id)"
            class="button is-small is-info is-outlined"
          >
            مقایسه
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RoomCard",
  props: {
    room: {
      type: Object,
      required: true,
    },
  },
  methods: {
    add_to_compare(id) {
      this.$store.commit("add_compare_id", id);
      this.$store.commit("addMessage", {
        type: "is-success",
        message: "به لیست مقایسه اضافه شد",
      });
    },
  },
};
</script>

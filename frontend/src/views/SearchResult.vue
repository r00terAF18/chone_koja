<template>
  <div class="container-fluid pl-6 pr-6 home mt-4">
    <div v-if="this.$store.state.messages">
      <div v-for="msg in this.$store.state.messages" v-bind:key="msg.id">
        <Message :type="msg.type" :message="msg.message" />
      </div>
    </div>
    <SearchComponent />
    <div class="columns">
      <div class="column is-2">
        <aside class="menu">
          <p class="menu-label">General</p>
          <ul class="menu-list">
            <li>
              <a>
                <button
                  @click="view_compare"
                  class="button is-outlined is-primary has-icons-left"
                >
                  <i class="fas fa-eye ml-1"></i>
                  {{ this.$store.state.compare_count }}
                </button>
              </a>
            </li>
            <li><a>Customers</a></li>
          </ul>
          <p class="menu-label">Administration</p>
          <ul class="menu-list">
            <li><a>Team Settings</a></li>
            <li>
              <a class="is-active">Manage Your Team</a>
              <ul>
                <li><a>Members</a></li>
                <li><a>Plugins</a></li>
                <li><a>Add a member</a></li>
              </ul>
            </li>
            <li><a>Invitations</a></li>
            <li><a>Cloud Storage Environment Settings</a></li>
            <li><a>Authentication</a></li>
          </ul>
          <p class="menu-label">Transactions</p>
          <ul class="menu-list">
            <li><a>Payments</a></li>
            <li><a>Transfers</a></li>
            <li><a>Balance</a></li>
          </ul>
        </aside>
      </div>
      <div class="column is-10">
        <div class="columns is-multiline">
          <div
            v-for="room in this.$store.state.list_rooms"
            v-bind:key="room.id"
            class="column is-3"
          >
            <RoomCard :room="room" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SearchComponent from "@/components/SearchComponent.vue";
import Message from "@/components/Message.vue";
import RoomCard from "@/components/RoomCard.vue";
export default {
  name: "SearchResult",
  components: {
    SearchComponent,
    Message,
    RoomCard,
  },
};
</script>

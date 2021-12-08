import axios from "axios";
axios.defaults.baseURL = "http://localhost:3000";

export const state = () => ({
  list_compare_rooms: [],
  list_rooms: [],
  compare_count: 0,
  messages: [],
})

export const mutations = {
  async add_compare_id(state, id) {
    await axios
      .get(`/api/v1/detail/${id}`)
      .then((res) => {
        let room = res.data.room;
        state.list_compare_rooms.push(room);
        state.compare_count++;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  remove_compare_id(state, id) {
    for (let i = 0; i < state.list_compare_rooms.length; i++) {
      if (state.list_compare_rooms[i].id == id) {
        state.list_compare_rooms.splice(i, 1);
        state.compare_count--;
      }
    }
  },
  addMessage(state, message) {
    state.messages.push(message);
  },
  removeMessage(state) {
    state.messages = [];
  },
  async start_search(state, city) {
    state.list_rooms = [];
    await axios
      .get(`/api/v1/search/?city=${city}`)
      .then((res) => {
        for (let room of res.data) {
          state.list_rooms.push(room);
        }
      })
      .catch((err) => {
        state.messages.push({
          type: "error",
          message: err.response.data.message,
        });
      });
  },

}

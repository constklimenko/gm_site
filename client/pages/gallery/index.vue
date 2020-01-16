<template>
  <div class="gallery">
    <div v-for="painting in paintings" v-bind:key="painting.id">
      <h1 class="gallery__item__h1">{{ painting.title }}</h1>
      <img class="gallery__item__img" v-bind:src="painting.photo" />
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  components: {},
  data() {
    return {
      paintings: [],
      currentPage: 1,
      perPage: 10
    };
  },
  async mounted() {
    await axios
      .get(`http://127.0.0.1:8000/api/v1/paintings/`)
      .then(response => {
        this.paintings = response.data;
      });
  }
};
</script>

<style lang="less"></style>

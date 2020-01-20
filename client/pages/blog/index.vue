<template>
  <div class="blog">
    
    <articleBlock
      v-for="(addr, index) in articleAddrs"
      v-bind:key="addr.id"
      v-bind:apiAddr="addr"
      v-bind:id="index + 1"
    />
  </div>
</template>

<script>
import articleBlock from "~/components/articleBlock";

export default {
  components: {
    articleBlock
  },
  data() {
    return {
      articleAddrs: [],
      currentPage: 1,
      perPage: 10
    };
  },
  mounted() {
    for (
      let i = 1 + (this.currentPage - 1) * this.perPage;
      i <= this.perPage + (this.currentPage - 1) * this.perPage;
      i++
    ) {
      this.articleAddrs.push(`http://127.0.0.1:8000/api/v1/articles/${i}`);
    }
  }
};
</script>

<style lang="less"></style>

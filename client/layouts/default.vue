<template>
  <div>
    <link rel="stylesheet" href="http://127.0.0.1:8000/static/css/index.css" />
    <navi />
    <nuxt />
  </div>
</template>

<style lang="less"></style>



<script>
import navi from "~/components/navi";

export default {
  components: {
    navi
  }
};
</script>

<template>
  <div class="main">
    <textBlock api-addr="http://127.0.0.1:8000/api/v1/main/1" />
  </div>
</template>

<script>
import textBlock from "~/components/textBlock";

export default {
  components: {
    textBlock
  }
};
</script>

<style lang="less"></style>

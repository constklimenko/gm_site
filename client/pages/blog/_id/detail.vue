<template>
  <div>
    <articleBlock v-bind:apiAddr="apiAddr" />
  </div>
</template>

<script>
import articleBlock from '~/components/articleBlock'

export default {
  components: {
    articleBlock
  },
  data () {
    return {
      apiAddr: `http://127.0.0.1:8000/api/v1/articles/${this.$route.params.id}`
    }
  }
}
</script>

<style lang="less">

</style>

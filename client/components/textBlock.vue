<template>
  <article>
    <h1>{{ title }} </h1>
    <div v-html="contentBlock" />
  </article>
</template>

<style lang='less' scoped>

</style>

<script>
import axios from 'axios'

export default {
  props: ['apiAddr'],
  data () {
    return {
      title: null,
      contentBlock: null
    }
  },
  async mounted () {
    await axios
      .get(this.apiAddr)
      .then((response) => {
        this.title = response.data.title_about
        this.contentBlock = response.data.content_about
      })
  }
}
</script>

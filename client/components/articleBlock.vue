<template>
  <article>
    <nuxt-link v-bind:to="path">
      <h1>{{ title }} </h1>
    </nuxt-link>
    <div v-html="contentBlock" />
  </article>
</template>

<style lang='less' scoped>

</style>

<script>
import axios from 'axios'

export default {
  props: ['apiAddr', 'id'],
  data () {
    return {
      title: null,
      contentBlock: null,
      path: `/blog/${this.id}/detail`
    }
  },
  async mounted () {
    await axios
      .get(this.apiAddr)
      .then((response) => {
        this.title = response.data.title
        this.contentBlock = response.data.content
      })
      .catch(console.log)
  }
}
</script>

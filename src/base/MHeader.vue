<template>
    <div class="header">
      <slot></slot>
    </div>
</template>

<script>
    export default {
        name: "",
        data() {
            return {}
        },
        methods: {},
        computed: {},
        components: {}
    }
</script>

<style scoped lang="less">
  .header{
    position: fixed;
    top: 0;
    left:0;
    width:100%;
    background: aquamarine;
    height: 40px;
    line-height: 40px;
    text-align: center;
    font-weight: bold;
    border-bottom: 1px solid #cccccc;
  }
</style>

<template>
    <div class="header">
      <slot></slot>
      <i @click="goBack"></i>
      <!--//下面要实现点击后退图标，后退到上面的一个操作-->
    </div>
</template>

<script>
    export default {
        name: "",
        props:{
          back:{//通过传值得方式，来控制界面按钮显示是否有没有
            type:Boolean,
            default:false
          }
        },
        data() {
            return {}
        },
        methods: {
          goBack(){
            this.$router.go(-1)
          }
        },
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

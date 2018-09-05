<template>
    <div class="footer">
      <router-link to="/home">
        <span>首页</span>
      </router-link>
      <router-link to="/list">
        <span>列表</span>
      </router-link>
      <router-link to="/collect">
        <span>收藏</span>
      </router-link>
      <router-link to="/add">
        <span>添加</span>
      </router-link>
      <router-link to="/detail">
        <span>删除</span>
      </router-link>
    </div>
</template>

<style scoped lang="less">
  .footer{
    position: fixed;
    left:0;
    bottom:0;
    width:100%;
    height: 50px;
    display:flex;
    border-top:1px solid #ccc;
    a{
      display: flex;
      color:fuchsia;
      flex-direction: column;
      flex: 1;
      align-items: center;
      justify-content: center;
    }
    a.router-link-active{
      color:red;
    }
  }
</style>

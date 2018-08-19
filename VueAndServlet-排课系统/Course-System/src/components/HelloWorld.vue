<template>
  <div class="">
    <div id="nav">
      <div id="section">
        <button class="select" to="login">登录</button>
        <button class="select" to="manage-teacher">教师管理</button>
        <router-link class="select" to="manage-computer-room">机房管理</router-link>
        <router-link class="select" to="manage-course">课程管理</router-link>
      </div>
      <div id="function">
        <h4>{{ msg }}</h4>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #nav {
    position: fixed;
    left: 0px;
    top: 60px;
    display: flex;
  }

  #section {
    flex: 2;
    text-align: center;
    border: cadetblue solid 3px;
    border-radius: 3px;
    padding: 15px;
  }

  .select {
    display: block;
    border-bottom: cadetblue solid 1px;
    color: grey;
  }

    #function {
      flex: 8;
      margin-left: 30px;
    }
</style>

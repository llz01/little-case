<template>
  <div id="app">
    <nav class="navbar navbar-expand-sm bg-light navbar-light fixed-top">
      <router-link to="/" class="navbar-brand">
        <img src="./assets/logo.png" style="width: 25px">Course-System
      </router-link>
      <ul class="nav navbar-nav justify-content-center">
        <li class="nav-item">
          <a class="nav-link" href="#">2018春</a>
        </li>
      </ul>
    </nav>
    <div id="nav" v-if="login==true">
      <div id="select" class="btn-group-vertical">
        <button class="btn btn-secondary" @click="select('Search')">排课查询</button>
        <button class="btn btn-secondary" @click="select('AdminInfo')">信息维护</button>
        <button class="btn btn-secondary" @click="select('ManageTeacher')">教师管理</button>
        <button class="btn btn-secondary" @click="select('ManageComputerRoom')">机房管理</button>
        <button class="btn btn-secondary" @click="select('ManageCourse')">课程管理</button>
        <button class="btn btn-secondary" @click="select('ManageGrade')">教学班</button>
        <button class="btn btn-secondary"
                @click="loginOut()"
        >退出
        </button>
      </div>
      <div id="function">
        <component :is="componentsName"></component>
      </div>
    </div>
    <div v-else>
      <Login></Login>
    </div>
    <div id="footer">
      <a href="#">Powered by @K</a><br>
      <a href="#">桃李春风一杯酒，江湖夜雨十年灯。</a>
    </div>
  </div>
</template>

<script>
  import Login from './components/Login'
  import ManageTeacher from './components/ManageTeacher'
  import ManageComputerRoom from './components/ManageComputerRoom'
  import ManageCourse from './components/ManageCourse'
  import ManageGrade from './components/ManageGrade'
  import AdminInfo from './components/AdminInfo'
  import Search from './components/Search'

  export default {
    name: 'App',
    data() {
      return {
        componentsName: 'Search',
        login: false
      }
    },
    components: {
      Login, ManageTeacher, ManageComputerRoom,
      ManageCourse, ManageGrade, AdminInfo,
      Search
    },
    methods: {
      select(name) {
        this.componentsName = name
      },
      isLogin() {
        console.log('acpt')
        if (sessionStorage.getItem('info') == true) {
          this.login = true
        } else {
          this.login = false
        }
      },
      loginOut() {
        sessionStorage['info'] = null;
        this.login = false
        console.log(sessionStorage['info'], this.login)
      }
    },
    mounted: function () {
      //this.select('Search')
      console.log(sessionStorage['info'], this.login)
      this.isLogin()
      console.log(sessionStorage['info'], this.login)
    }
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    margin-top: 60px;
  }

  .title {
    border: aqua solid 4px;
    font-size: 30px;
    padding: 2px;
    border-radius: 5px;
  }

  #nav {
    width: 100%;
    left: 0px;
    top: 60px;
    display: flex;
  }

  #select {
    flex: 2;
    text-align: center;
    border: greenyellow solid 3px;
    border-radius: 3px;
    padding: 15px;
    height: 100%;
  }

  #function {
    flex: 8;
    margin-left: 30px;
    margin-right: 30px;
    margin-top: 30px;
  }

  #footer {
    position: fixed;
    text-align: center;
    opacity: 0.4;
    pointer-events: none;
    left: calc(50% - 100px);
    bottom: 0px;
  }

  #footer > a {
    color: blueviolet;
  }
</style>

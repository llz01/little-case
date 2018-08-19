<template>
  <div id="login">
    <div class="container">
      <div style="text-align: center">
        <img src="../assets/logo.png">
      </div>
      <form>
        <div class="from-group">
          <label for="usr">Username:</label>
          <input type="text"
                 v-model="username"
                 class="form-control" placeholder="用户名" id="usr">
        </div>
        <div class="form-group">
          <label for="pwd">Password:</label>
          <input type="password"
                 v-model="password"
                 class="form-control" placeholder="密码" id="pwd">
        </div>
        <button type="button" class="btn btn-primary"
                @click="login()">登录
        </button>
      </form>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Login",
    data() {
      return {
        username: '',
        password: ''
      }
    },
    methods: {
      login() {
        console.log(this.username, this.password)
        if (this.username == null || this.password == null ||
          this.username == '' || this.password == ''
        ) {
          alert('Error:用户名或密码为空！')
          document.getElementById('usr').focus()
        } else {
          $.ajax({
            url: this.url_pre + '/loginServlet',
            type: 'POST',
            //contentType: 'application/json; charset=utf-8',
            data: {
              data: JSON.stringify({
                user: this.username,
                password: this.password
              })
            },
            dataType: 'json',
            success: function (res, state) {
              console.log(res, state)
              console.log(res['message'])
              if (res['message'] == 1 || res['message'] == 2) {
                sessionStorage['info'] = 1
                console.log(sessionStorage['info'])
              } else {
                alert('用户名或密码错误！')
              }
              console.log('Login Finish')
              window.location.reload()
            }
          });
        }
      }
    }
  }
</script>

<style scoped>
  img {
    width: 200px;
  }

  #login {
  }
</style>

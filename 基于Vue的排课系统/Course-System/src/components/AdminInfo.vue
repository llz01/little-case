<template>
  <div id="login">
    <div style="text-align: center">
      <img src="../assets/logo.png">
    </div>
    <form>
      <div class="from-group">
        <label for="usr">Username:</label>
        <input type="text" class="form-control" value="sa" id="usr" disabled>
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input v-model="email"
          type="email" class="form-control" placeholder="邮箱" id="email">
      </div>
      <div class="form-group">
        <label for="tel">Tel:</label>
        <input v-model="tel"
          type="text" class="form-control" placeholder="联系方式" id="tel">
      </div>
      <div class="form-group">
        <label for="pwd1">Password:</label>{{psw1}}
        <input v-model="psw1"
          type="password" class="form-control" placeholder="密码" id="pwd1">
      </div>
      <div class="form-group">
        <label for="pwd2">Confirm:</label>{{psw2}}
        <input v-model="psw2"
          type="password" class="form-control" placeholder="密码" id="pwd2">
      </div>
    </form>
    <button @click="send" class="btn btn-warning btn-sm">修改</button>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        email: null,
        tel: null,
        psw1: null,
        psw2: null
      }
    },
    methods: {
      send() {
        if (this.psw1 == this.psw2) {
          $.ajax({
            url: this.url_pre + '/adminManageServlet',
            type: 'POST',
            data: {
              data: JSON.stringify({
                state: 1,
                message: {
                  adUserName: 'sa',
                  adUserPwd: this.psw1,
                  adTell: this.tel,
                  adEmail: this.email
                },
              })
            },
            async: false,
            success: function (res) {
              //console.log(JSON.parse(decodeURIComponent(res)))
              var data = JSON.parse(decodeURIComponent(res))
              tempData = data['message']
              console.log(tempData);
            }
          })
        }else {
          alert('密码不一致，请检查！')
        }
      }
    },
    mounted: function () {
      //this.loading()
    }
  }
</script>

<style scoped>
  img {
    width: 50px;
  }
</style>

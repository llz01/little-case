<template>
  <div id="manage-teacher">
    <span class="title">教师管理</span>
    <button class="btn btn-sm btn-success" @click="addTeacher">添加</button>
    <table class="table table-hover">
      <tr>
        <th>姓名</th>
        <th>工号</th>
        <th>电话</th>
        <th>密码</th>
        <th>邮箱</th>
        <th></th>
      </tr>
      <tr v-for="value in data">
        <td>{{value.teacherName}}</td>
        <td>{{value.teacherNo}}</td>
        <td>{{value.teacherTell}}</td>
        <td>{{value.teacherPwd}}</td>
        <td>{{value.teacherEmail}}</td>
        <td>
          <button class="btn btn-sm btn-warning" @click="edit(value)">修改</button>
          <button @click="deleteTeacher(value.teacherNo)" class="btn btn-sm btn-danger">删除</button>
        </td>
      </tr>
    </table>
    <div id="add-teacher">
      <form>
        <input placeholder="教师姓名" v-model="teacherName">
        <input placeholder="工号" v-model="teacherNo">
        <input placeholder="电话" v-model="teacherTell">
        <input placeholder="设置登录密码" v-model="teacherPwd"/>
        <input placeholder="邮箱" v-model="teacherEmail"/>
      </form>
      <button class="btn btn-sm btn-info" @click="submit">提交</button>
      <button @click="close" class="btn btn-danger btn-sm">取消</button>
    </div>
  </div>
</template>

<script>
  export default {
    name: "ManageTeacher",
    data() {
      return {
        data: 'default',
        teacherName: null,
        teacherNo: null,
        teacherTell: null,
        teacherPwd: null,
        teacherEmail: null,
        type: 3
      }
    },
    methods: {
      loading() {
        var tempData = {}
        $.ajax({
          url: this.url_pre + '/teacherServlet',
          type: 'GET',
          async: false,
          //dataType: 'json',
          success: function (res) {
            var data = decodeURIComponent(res)
            tempData = JSON.parse(data)
            //this.data = JSON.parse(data)
            //console.log(this.data['message'])
            this.data = '12312'
          }
        });
        this.data = tempData['message']
        console.log(this.data, tempData)
      },
      submit() {
        $.ajax({
          url: this.url_pre + '/teacherManagement',
          type: 'POST',
          async: false,
          data: {
            data: JSON.stringify({
              state: this.type,
              message: {
                teacherName: this.teacherName,
                teacherNo: this.teacherNo,
                teacherTell: this.teacherTell,
                teacherPwd: this.teacherPwd,
                teacherEmail: this.teacherEmail
              }
            })
          },
          dataType: 'json',
          success: function (res) {
            console.log(res);
          }
        })
        this.loading()
        $('#add-teacher').hide('slow')
        alert('已提交！')
      },
      addTeacher() {
        $('#add-teacher').show('slow')
        this.type = 3
        this.teacherName = null
        this.teacherNo = null
        this.teacherTell = null
        this.teacherPwd = null
        this.teacherEmail = null
      },
      close() {
        $('#add-teacher').hide('slow');
      },
      deleteTeacher(id) {
        $.ajax({
          url: this.url_pre + '/teacherManagement',
          type: 'GET',
          data: {
            data: JSON.stringify({
              state: 1,
              message: id
            })
          },
          async: false,
          //dataType: 'json',
          success: function (res) {
            var data = decodeURIComponent(res)
            tempData = JSON.parse(data)
          }
        });
        this.loading()
      },
      edit(value) {
        $('#add-teacher').show('slow')
        this.teacherName = value.teacherName
        this.teacherNo = value.teacherNo
        this.teacherEmail = value.teacherEmail
        this.teacherPwd = value.teacherPwd
        this.teacherTell = value.teacherTell
        this.type = 2
      }
    },
    mounted: function () {
      this.loading()
      //this.data = 'sadas'
    }
  }
</script>

<style scoped>
  #add-teacher {
    position: fixed;
    top: 20%;
    left: calc(50% - 200px);
    background-color: burlywood;
    padding: 50px;
    border-radius: 20px;
    display: none;
  }
</style>

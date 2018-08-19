<template>
  <div id="manage-teacher">
    <span class="title">课程管理</span>
    <button @click="addCourse"
            class="btn btn-sm btn-success">添加
    </button>
    <table class="table table-hover">
      <tr>
        <th>课程名称</th>
        <th>课程号</th>
        <th>学分</th>
        <th>总学时</th>
        <th>实验学时</th>
        <th></th>
      </tr>
      <tr v-for="value in data">
        <td>{{value['courseName']}}</td>
        <td>{{value['courseNo']}}</td>
        <td>{{value['courseCredit']}}</td>
        <td>{{value['courseHour']}}</td>
        <td>{{value['courseExpHour']}}</td>
        <td>
          <button @mouseover="showMsg"
                  @mouseout="hideMsg"
                  class="btn btn-sm btn-info">实验信息
          </button>
          <button @click="showSchedule"
                  class="btn btn-sm btn-success">排课
          </button>
          <button class="btn btn-sm btn-warning" @click='edit(value)'>修改</button>
          <button class="btn btn-sm btn-danger" @click="deleteCourse(value.courseNo)">删除</button>
        </td>
      </tr>
    </table>
    <div id="add-course">
      <form>
        <input placeholder="课程名" v-model="courseName">
        <input placeholder="课程号" v-model="courseNo">
        <input placeholder="学分" v-model="courseCredit">
        <input placeholder="总学时" v-model="courseHour"/>
        <input placeholder="实验学时" v-model="courseExpHour"/>
      </form>
      <button class="btn btn-sm btn-info" @click="submit">提交</button>
      <button @click="close" class="btn btn-danger btn-sm">取消</button>
    </div>
    <div>
      <component :is="componentName"></component>
    </div>
  </div>
</template>

<script>
  import ExpInfo from './ExpInfo'
  import ArrangeCourse from './ArrangeCourse'

  export default {
    name: "ManageCourse",
    components: {ArrangeCourse, ExpInfo},
    data() {
      return {
        componentName: null,
        data: null,
        type: 3,
        courseName: null,
        courseHour: null,
        courseExpHour: null,
        courseNo: null,
        courseCredit: null
      }
    },
    methods: {
      showMsg() {
        this.componentName = 'ExpInfo'
      },
      hideMsg() {
        this.componentName = null
      },
      loading() {
        var tempData = null
        $.ajax({
          url: this.url_pre + '/courseServlet',
          type: 'GET',
          async: false,
          success: function (res) {
            //console.log(JSON.parse(decodeURIComponent(res)))
            var data = JSON.parse(decodeURIComponent(res))
            tempData = data['message']
            console.log(tempData);
          }
        })
        this.data = tempData
      },
      showSchedule() {
        //$('#arrange-course').show()
        this.componentName = 'ArrangeCourse'
      },
      submit() {
        var tempData = null
        $.ajax({
          url: this.url_pre + '/courseManageServlet',
          type: 'POST',
          data: {
            data: JSON.stringify({
              state: this.type,
              message: {
                courseCredit: this.courseCredit,
                courseName: this.courseName,
                courseHour: this.courseHour,
                courseNo: this.courseNo,
                courseExpHour: this.courseExpHour
              }
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
        this.loading()
        $('#add-course').hide('slow')
        alert('已提交！')
      },
      close() {
        $('#add-course').hide('slow')
      },
      addCourse() {
        $('#add-course').show('slow')
        this.type = 3
        this.courseName = null,
          this.courseHour = null,
          this.courseExpHour = null,
          this.courseNo = null,
          this.courseCredit = null
      },
      edit(value) {
        $('#add-course').show('slow')
        this.courseName = value.courseName
        this.courseNo = value.courseNo
        this.courseCredit = value.courseCredit
        this.courseHour = value.courseHour
        this.courseExpHour = value.courseExpHour
        this.type = 2
        this.loading()
      },
      deleteCourse(id) {
        $.ajax({
          url: this.url_pre + '/courseManageServlet',
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
      }
    },
    mounted: function () {
      this.loading()
    }
  }
</script>

<style scoped>
  table {
    margin-top: 10px;
  }

  #add-course {
    position: fixed;
    top: 20%;
    left: calc(50% - 200px);
    background-color: burlywood;
    padding: 50px;
    border-radius: 20px;
    display: none;
  }
</style>

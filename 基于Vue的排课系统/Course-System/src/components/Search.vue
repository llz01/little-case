<template>
  <div id="search">
    <h3>排课查询</h3>
    <form class="form-inline">
      <select name="condition" class="form-control" v-model="type">
        <option value="1">按教师查询</option>
        <option value="2">按班级查询</option>
      </select>
      <input class="form-control" type="text" placeholder="Search" v-model="value">
    </form>
    <button class="btn btn-success" @click="search">条件查询</button>
    <button class="btn btn-warning" @click="searchAll">总表查询</button>
    <div>
      <table class="table table-hover table-bordered" id="condition">
        <tr>
          <th>课序代号</th>
          <th>课程序号</th>
          <th>上机人数</th>
          <th>班级编号</th>
          <th>教师工号</th>
          <th>学期</th>
          <th>排课编号</th>
          <th>实验编号</th>
          <th>机房地址</th>
          <th>机房人数</th>
          <th>周次</th>
          <th>星期</th>
          <th>节次</th>
        </tr>
        <tr v-for="value in message">
          <td>{{value.courseNo}}</td>
          <td>{{value.courseIdx}}</td>
          <td>{{value.stuNum}}</td>
          <td>{{value.classNo}}</td>
          <td>{{value.teacherNo}}</td>
          <td>{{value.appTeam}}</td>
          <td>{{value.arraneNo}}</td>
          <td>{{value.expItemNo}}</td>
          <td>{{value.computerSTuNum}}</td>
          <td>{{value.roomNo}}</td>
          <td>{{value.arrangeWeek}}</td>
          <td>{{value.arrangeDay}}</td>
          <td>{{value.arrangeInterval}}</td>
        </tr>
      </table>
      <table id="all" class="table table-hover table-bordered">
        <tr>
          <th>排课编号</th>
          <th>申请序号</th>
          <th>项目编号</th>
          <th>上机人数</th>
          <th>机房编号</th>
          <th>周次</th>
          <th>星期</th>
          <th>节次</th>
        </tr>
        <tr v-for="value in message">
          <td>{{value.arrangeNo}}</td>
          <td>{{value.fkappNo}}</td>
          <td>{{value.fkExpitemNo}}</td>
          <td>{{value.stuNum}}</td>
          <td>{{value.fkRoomNo}}</td>
          <td>{{value.arrangeWeek}}</td>
          <td>{{value.arrangeDay}}</td>
          <td>{{value.arrangeInterval}}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Search",
    data() {
      return {
        value: null,
        type: 1,
        message: null
      }
    },
    methods: {
      search() {
        this.hide()
        var tempData = null
        $.ajax({
          url: this.url_pre + '/QueryServlet',
          type: 'GET',
          async: false,
          data: {
            data: JSON.stringify(
              {
                state: this.type,
                message: this.value
              }
            )
          },
          success: function (res) {
            tempData = JSON.parse(decodeURIComponent(res))
          }
        })
        this.message = tempData['message']
        $('#condition').show('slow')
      },
      searchAll() {
        this.hide()
        var tempData = null
        $.ajax({
          url: this.url_pre + '/computerServlet',
          type: 'GET',
          async: false,
          //dataType: 'json',
          data: {
            data: JSON.stringify(
              {
                state: 6,
              }
            )
          },
          success: function (res) {
            tempData = JSON.parse(decodeURIComponent(res))
          }
        })
        this.message = tempData['message']
        $('#all').show('slow')
      },
      hide() {
        $('table').hide()
      }
    },
    mounted: function () {
      //this.loading()
    }
  }
</script>

<style scoped>
  #search {
    margin-top: 30px;
  }

  form {
    margin-top: 15px;
  }

  table {
    display: none;
  }
</style>

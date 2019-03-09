<template>
  <div id="manage-computer-room">
    <span class="title">机房管理</span>
    <button @click="addRoom"
            class="btn btn-sm btn-success">添加
    </button>
    <table class="table table-hover">
      <tr>
        <th>机房名称</th>
        <th>机房编号</th>
        <th>设备套数</th>
        <th>容纳人数</th>
        <th>备注</th>
        <th></th>
      </tr>
      <tr v-for="value in data">
        <td>{{value.roomName}}</td>
        <td>{{value.roomNo}}</td>
        <td>{{value.deviceNum}}</td>
        <td>{{value.deviceCapacity}}</td>
        <td>{{value.deviceDescribe}}</td>
        <td>
          <button class="btn btn-sm btn-primary" @click="showArrangeCourse"><span>排课查询</span></button>
          <button class="btn btn-sm btn-warning" @click="edit(value)">修改</button>
          <button @click="deleteRoom(value.roomNo)" class="btn btn-sm btn-danger">删除</button>
        </td>
      </tr>
    </table>
    <div id="add-room">
      <form>
        <input placeholder="机房名" v-model="roomName">
        <input placeholder="机房号" v-model="roomNo"  type="number">
        <input placeholder="设备套数" v-model="deviceNum" type="number">
        <input placeholder="容纳人数" v-model="deviceCapacity" type="number"/>
        <input placeholder="备注" v-model="deviceDescribe"/>
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
  import ArrangeCourse from './ArrangeCourse'

  export default {
    name: "ManageComputerRoom",
    components: {ArrangeCourse},
    data() {
      return {
        componentName: null,
        data: null,
        roomName: null,
        roomNo: null,
        deviceNum: null,
        deviceCapacity: null,
        deviceDescribe: null
      }
    },
    methods: {
      showArrangeCourse() {
        $('#arrange-course').show('slow');
        this.componentName = 'ArrangeCourse'
      },
      loading() {
        var tempData = null
        $.ajax({
          url: this.url_pre + '/computerServlet',
          type: 'GET',
          data: {
            data: JSON.stringify({
              state: 1
            })
          },
          async: false,
          success: function (res) {
            //console.log(JSON.parse(decodeURIComponent(res)))
            var data = JSON.parse(decodeURIComponent(res))
            tempData = data['message']
            //console.log(tempData);
          }
        })
        this.data = tempData
        console.log(this.data);
      },
      addRoom() {
        $('#add-room').show('slow')
        this.type = 3
        this.roomName = null,
        this.roomNo = null,
        this.deviceNum = null,
        this.deviceCapacity = null,
        this.deviceDescribe = null
      },
      submit() {
        var tempData = null
        $.ajax({
          url: this.url_pre + '/computerServlet',
          type: 'POST',
          data: {
            data: JSON.stringify({
              state: this.type,
              message: {
                roomName: this.roomName,
                roomNo: this.roomNo,
                deviceNum: this.deviceNum,
                deviceCapacity: this.deviceCapacity,
                deviceDescribe: this.deviceDescribe
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
        $('#add-room').hide('slow')
        alert('已提交！')
      },
      close() {
        $('#add-room').hide('slow')
      },
      addRoom() {
        $('#add-room').show('slow')
        this.type = 4
        this.roomName = null,
          this.roomNo = null,
          this.deviceNum = null,
          this.deviceCapacity = null,
          this.deviceDescribe = null
      },
      edit(value) {
        $('#add-room').show('slow')
        this.roomName = value.roomName
        this.roomNo = value.roomNo
        this.deviceNum = value.deviceNum
        this.deviceCapacity = value.deviceCapacity
        this.deviceDescribe = value.deviceDescribe
        this.type = 3
        this.loading()
      },
      deleteRoom(id) {
        $.ajax({
          url: this.url_pre + '/computerServlet',
          type: 'GET',
          data: {
            data: JSON.stringify({
              state: 2,
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
  #add-room {
    position: fixed;
    top: 20%;
    left: calc(50% - 200px);
    background-color: burlywood;
    padding: 50px;
    border-radius: 20px;
    display: none;
  }
</style>

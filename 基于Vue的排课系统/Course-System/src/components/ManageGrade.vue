<template>
  <div id="manage-class">
    <span class="title">教学班管理</span>
    <button @click="addClass"
            class="btn btn-sm btn-success">添加
    </button>
    <table class="table table-hover">
      <tr>
        <th>班级编号</th>
        <th>班级名称</th>
        <th>专业名称</th>
        <th>专业年级</th>
        <th></th>
      </tr>
      <tr v-for="value in data">
        <td>{{value.classNo}}</td>
        <td>{{value.majorName}}</td>
        <td>{{value.className}}</td>
        <td>{{value.classGrade}}</td>
        <td>
          <button class="btn btn-sm btn-warning" @click="edit(value)">修改</button>
          <button @click="deleteClass(value.classNo)" class="btn btn-sm btn-danger">删除</button>
        </td>
      </tr>
    </table>
    <div id="add-class">
      <form>
        <input placeholder="班级编号" v-model="classNo" type="number">
        <input placeholder="班级名称" v-model="majorName">
        <input placeholder="专业名称" v-model="className">
        <input placeholder="专业年级" v-model="classGrade"/>
      </form>
      <button class="btn btn-sm btn-info" @click="submit">提交</button>
      <button @click="close" class="btn btn-danger btn-sm">取消</button>
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
        data: null,
        type: null,
        classNo: null,
        majorName: null,
        className: null,
        classGrade: null
      }
    },
    methods: {
      loading() {
        var tempData = null
        $.ajax({
          url: this.url_pre + '/classServlet',
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
      },
      submit() {
        $.ajax({
          url: this.url_pre + '/classManageServlet',
          type: 'POST',
          async: false,
          data: {
            data: JSON.stringify({
              state: this.type,
              message: {
                classNo: this.classNo,
                majorName: this.majorName,
                className: this.className,
                classGrade: this.classGrade,
              }
            })
          },
          dataType: 'json',
          success: function (res) {
            console.log(res);
          }
        })
        this.loading()
        $('#add-class').hide('slow')
        alert('已提交！')
      },
      addClass() {
        $('#add-class').show('slow')
        this.type = 3
        this.classNo = null
        this.majorName = null
        this.className = null
        this.classGrade = null
      },
      close() {
        $('#add-class').hide('slow');
      },
      deleteClass(id) {
        $.ajax({
          url: this.url_pre + '/classManageServlet',
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
        $('#add-class').show('slow')
        this.classNo = value.classNo
        this.majorName = value.majorName
        this.className = value.className
        this.classGrade = value.classGrade
        this.type = 2
      }
    },
    mounted: function () {
      this.loading()
    }
  }

</script>

<style scoped>
  #add-class {
    position: fixed;
    top: 20%;
    left: calc(50% - 200px);
    background-color: burlywood;
    padding: 50px;
    border-radius: 20px;
    display: none;
  }
</style>

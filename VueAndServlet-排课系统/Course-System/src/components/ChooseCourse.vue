<template>
  <div class="choose-course">
    <button @click="show"
      class="">排课</button>
    <div id="choose-course-form">
      当前选中：{{test}}<br>
      第{{arrangeWeek}}周，
      星期{{arrangeDay}}，
      第{{arrangeInterval}}节
      <form>
        <input v-model="appNo" type="text" placeholder="排课序号"/>
        <input v-model="courseNo" type="text" placeholder="课程代号"/>
        <input v-model="courseIdx" type="text" placeholder="课程序号"/>
        <input v-model="appStuNum" type="text" placeholder="上课人数"/>
        <input v-model="classNo" type="text" placeholder="班级编号"/>
        <input v-model="teacherNo" type="text" placeholder="教工号"/>
        <input v-model="appTeam" type="text" placeholder="学期"/>
        <input v-model="expItemNo" type="text" placeholder="项目编号"/>
        <input v-model="stuNum" type="text" placeholder="上机人数"/>
        <input v-model="roomNo" type="text" placeholder="实验室编号"/>
      </form>
      <button @click="send">提交</button>
      <button @click="cancel">取消</button>
    </div>
  </div>
</template>

<script>
  export default {
    name: "ChooseCourse",
    data() {
      return {
        appNo: null,
        courseNo: null,
        courseIdx: null,
        appStuNum: null,
        classNo: null,
        teacherNo: null,
        appTeam: null,
        expItemNo: null,
        stuNum: null,
        roomNo: null,
        test: this.arrangeDay
      }
    },
    props: ['arrangeWeek', 'arrangeDay', 'arrangeInterval'],
    methods: {
      show() {
        $('#choose-course-form').show()
        console.log(this.arrangeWeek, this.arrangeDay, this.arrangeInterval)
      },
      cancel() {
        $('#choose-course-form').hide()
        console.log(this.arrangeWeek, this.arrangeDay, this.arrangeInterval)
      },
      send() {
        console.log(this.arrangeWeek, this.arrangeDay, this.arrangeInterval)
        $.ajax({
          url: this.url_pre + '/beforeServlet',
          type: 'POST',
          async: false,
          data: {
            data: JSON.stringify({
              state: 1,
              message: {
                appNo: this.appNo,
                courseNo: this.courseNo,
                courseIdx: this.courseIdx,
                appStuNum: this.appStuNum,
                classNo: this.classNo,
                teacherNo: this.teacherNo,
                appTeam: this.appTeam,
                expItemNo: this.expItemNo,
                stuNum: this.stuNum,
                roomNo: this.roomNo,
                arrangeWeek: this.arrangeWeek,
                arrangeDay: this.arrangeDay,
                arrangeInterval: this.arrangeInterval
              }
            })
          },
          success: function (res) {
            console.log(JSON.parse(decodeURIComponent(res)))
            alert('提交成功')
            this.hide()
          }
        })
      }
    }
  }
</script>

<style scoped>
  #choose-course-form {
    display: none;
    position: fixed;
    top: 25%;
    background-color: aqua;
    padding: 20px;
    border-radius: 20px;
  }
</style>

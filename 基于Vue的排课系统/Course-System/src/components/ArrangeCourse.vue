<template>
  <div id="arrange-course">
    <div>
      <button @click="close" class="btn btn-danger btn-sm">X</button>
      周次
      <select v-model="week">
        <option v-for="n in 10">{{n}}</option>
      </select>
      <select v-model="roomID">
        <option v-for="value in computerInfo">
          {{value.roomNo}}
        </option>
      </select>{{roomID}}
      <button @click="submit" class="btn btn-info btn-sm">查询</button>
      <div style="display: flex">
        <div class="self-th">周一</div>
        <div class="self-th">周二</div>
        <div class="self-th">周三</div>
        <div class="self-th">周四</div>
        <div class="self-th">周五</div>
        <div class="self-th">周六</div>
        <div class="self-th">周日</div>
      </div>
      <div class="self-table">
        <div class="self-tr" v-for="(value, index) in data">
          <div class="self-td">
            {{value['1']}}
            <ChooseCourse v-bind:arrangeDay="index + 1"
                          v-bind:arrangeWeek="week"
                          v-bind:arrangeInterval="1"></ChooseCourse>
          </div>
          <div class="self-td">{{value['2']}}
            <ChooseCourse v-bind:arrangeDay="index + 1"
                          v-bind:arrangeWeek="week"
                          v-bind:arrangeInterval="2"></ChooseCourse>
          </div>
          <div class="self-td">{{value['3']}}
            <ChooseCourse v-bind:arrangeDay="index + 1"
                          v-bind:arrangeWeek="week"
                          v-bind:arrangeInterval="3"></ChooseCourse>
          </div>
          <div class="self-td">{{value['4']}}
            <ChooseCourse v-bind:arrangeDay="index + 1"
                          v-bind:arrangeWeek="week"
                          v-bind:arrangeInterval="4"></ChooseCourse>
          </div>
          <div class="self-td">{{value['5']}}
            <ChooseCourse v-bind:arrangeDay="index + 1"
                          v-bind:arrangeWeek="week"
                          v-bind:arrangeInterval="5"></ChooseCourse>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import ChooseCourse from './ChooseCourse'

  export default {
    name: "ArrangeCourse",
    components: {ChooseCourse},
    data() {
      return {
        data: null,
        count: 1,
        week: 1,
        computerInfo: null,
        roomID: null,
        day: null,
        interval: null
      }
    },
    methods: {
      close() {
        $('#arrange-course').hide('slow');
      },
      arrangeCourse() {
        var tempData = null
        $.ajax({
          url: this.url_pre + '/choiceServlet',
          type: 'GET',
          async: false,
          data: {
            data: JSON.stringify({
              message: {
                week: this.week,
                num: this.roomID
              }
            })
          },
          success: function (res) {
            //console.log(JSON.parse(decodeURIComponent(res)))
            var data = JSON.parse(decodeURIComponent(res))
            tempData = data['message']
            console.log(tempData);
            this.count = 0
          }
        })
        this.data = tempData
      },
      submit() {
        this.arrangeCourse()
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
        this.computerInfo = tempData
      }
    },
    mounted() {
      this.arrangeCourse()
      this.loading()
    }
  }
</script>

<style scoped>
  #arrange-course {
    position: fixed;
    top: 100px;
    width: 70%;
    height: 70%;
    left: auto;
    right: auto;
    background-color: burlywood;
    padding: 20px;
    border-radius: 10px;
  }

  .self-table {
    background-color: aliceblue;
    display: flex;
  }

  .self-tr {
    flex: 1;
    font-size: 10px;
    border: green solid 2px;
    padding: 3px;
  }

  .self-th {
    flex: 1;
    font-size: 15px;
  }

  .self-td {
    border-bottom: green solid 2px;
    height: 60px;
  }
</style>

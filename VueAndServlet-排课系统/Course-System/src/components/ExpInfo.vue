<template>
  <div class="exp-info">
    <p><b>项目编号：</b>2111</p>
    <p><b>实验名称：</b>冒泡算法</p>
    <p><b>实验类型：</b>上机</p>
    <p><b>学时：</b>3</p>
  </div>
</template>

<script>
  export default {
    name: "ExpInfo",
  methods: {
    loading() {
      $.ajax({
        url: this.url_pre + '/expItemServlet',
        type: 'GET',
        dataType: 'json',
        success: function (res) {
          console.log(res)
        }
      })
    }
  },
  mounted: function () {
    //this.loading()
  }
  }
</script>

<style scoped>
  p {
    line-height: 0.5;
    font-size: 10px;
  }

  .exp-info {
    position: fixed;
    left: calc(50% - 50px);
    right: auto;
    top: 25%;
    background: antiquewhite;
    border-radius: 10px;
    padding: 10px;
    border: red solid 1px;
  }
</style>

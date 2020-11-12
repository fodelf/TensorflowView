<!--
 * @Description: 描述
 * @Author: pym
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-30 23:29:01
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-12 12:35:27
 -->
<template>
  <div class="header">
    <span class="menuIcon iconfont icon-zhankai" @click="changeMenu()"></span>
    <div class="headerTit clearfix">
      <i class="headerIcon"></i>吴文周
      <span class="iconfont icon-shezhi"></span>
      <!-- <el-switch
  v-model="value"
  active-color="#13ce66"
  inactive-color="#ff4949">
</el-switch> -->
    </div>
  </div>
</template>

<script>
// import io from 'socket.io-client';
export default {
  name: 'headerModule',
  data() {
    return {
      isCollapse: false,
      value: '',
    }
  },
  methods: {
    changeMenu() {
      this.$emit('changeCollapse')
    },
  },
  created(){
    let namespace = '/mes';
    // require('socket.io-client')(location.protocol + '//' + document.domain + ':' + location.port + namespace);
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);
    // var socket = require('socket.io-client')(location.protocol + '//' + document.domain + ':' + location.port + namespace);
    socket.on('connect', function() {
        socket.emit('mes', {data: 'I\'m connected!'});
    });
    socket.on('train', function(msg) {
      console.log(msg)
    });

  }
}
</script>

<style lang="less" scoped>
.header {
  width: 100%;
  height: 65px;
  line-height: 65px;
  padding: 0 15px;
  background: #3c4452;
  box-sizing: border-box;
  display: flex;
  justify-content: space-between;
  .menuIcon {
    font-size: 18px;
    color: rgba(255, 255, 255, 0.5);
    cursor: pointer;
  }
  .headerTit {
    height: 65px;
    line-height: 65px;
    display: flex;
    align-items: center;
    color: rgba(255, 255, 255, 0.5);
    .iconfont {
      margin-left: 30px;
    }
  }
  .headerIcon {
    background: url('../../assets/img/headerBg.svg') no-repeat center;
    display: inline-block;
    width: 31px;
    height: 31px;
    margin-right: 10px;
    background-size: 100% 100%;
  }
}
</style>

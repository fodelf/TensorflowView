<!--
 * @Description: 描述
 * @Author: pym
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-30 23:29:01
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-13 19:41:09
 -->
<template>
  <div class="header">
    <span class="menuIcon iconfont icon-zhankai" @click="changeMenu()"></span>
    <div class="headerTit clearfix">
      <i class="headerIcon"></i>吴文周
      <i class="el-icon-bell" style="margin-left:20px;font-size:20px" @click="queryMes()"></i>
      <i class="tips" v-if="count>0">{{countMes}}</i>
      <span class="iconfont icon-shezhi" style="margin-left:20px;"></span>
      <!-- <el-switch
  v-model="value"
  active-color="#13ce66"
  inactive-color="#ff4949">
</el-switch> -->
    </div>
    <el-drawer
      :visible.sync="drawer"
       size="20%"
      >
      <template slot="title" >
        <div class="title">
          系统消息
        </div>
      </template>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>卡片名称</span>
        </div>
        <div v-for="o in 4" :key="o" class="text item">
          {{'列表内容 ' + o }}
        </div>
      </el-card>
    </el-drawer>
  </div>
</template>

<script>
// import io from 'socket.io-client';
export default {
  name: 'headerModule',
  data() {
    return {
      isCollapse: false,
      drawer:false,
      value: '',
      count:0,
      countMes:0
    }
  },
  methods: {
    changeMenu() {
      this.$emit('changeCollapse')
    },
    queryMes(){
      this.drawer = !this.drawer
    }
  },
  created(){
    let namespace = '/mes';
    // require('socket.io-client')(location.protocol + '//' + document.domain + ':' + location.port + namespace);
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);
    // var socket = require('socket.io-client')(location.protocol + '//' + document.domain + ':' + location.port + namespace);
    socket.on('connect', function() {
        socket.emit('mes', {data: 'I\'m connected!'});
    });
    socket.on('train', (msg)=>{
      // console.log(msg)
      //  this.$message({
      //     message: '训练成功，请在消息中查看！',
      //     type: 'success'
      //   });
      this.count++
      if(this.count>99){
        this.countMes = '99+'
      }else{
        this.countMes = this.count
      }
      this.$notify({
        title: '成功',
        message: '训练成功，请在消息中查看！',
        type: 'success'
      });
    });

  }
}
</script>

<style lang="less" scoped>
@border-color: #4f5467;
@bg-color: #353c48;
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
  .tips{
    cursor: pointer;
    width: 12px;
    height: 16px;
    padding: 0 5px;
    color: rgba(255, 255, 255, 0.5);
    font-size: 12px;
    line-height: 16px;
    white-space: nowrap;
    text-align: center;
    background: #fb9678;
    border-radius: 10px;
    position: absolute;
    margin-left: 118px;
    margin-top: -10px;
  }
}
/deep/.el-tabs__nav-wrap::after {
  height:0px;
  background-color:#4F5467;
}
.title{
  height: 40px;
  line-height:40px;
  color:#fb9678;
  font-size:14px;
  border-bottom: 2px solid;
}

/deep/.el-drawer__header{
  height: 40px;
}
/deep/.el-drawer{
  background: #3c4452;
}
/deep/.el-drawer:focus{
 outline: none;
}
/deep/.el-drawer__close-btn{
 outline: none;
}
/deep/.el-drawer__body{
  padding:20px 20px 0px;
  box-sizing: border-box;
}
</style>

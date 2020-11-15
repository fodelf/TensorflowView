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
      <span @click="queryMes()">
        <i class="el-icon-bell" style="margin-left:20px;font-size:20px"></i>
        <i class="tips" v-show = "count>0" >{{countMes}}</i>
      </span>
      <span class="iconfont icon-shezhi" style="margin-left:20px;"></span>
      <!-- <el-switch
  v-model="value"
  active-color="#13ce66"
  inactive-color="#ff4949">
</el-switch> -->
    </div>
    <el-drawer
      :visible.sync="drawer"
      >
      <template slot="title" >
        <div class="title">
          系统消息
        </div>
      </template>
      <el-card class="box-card" v-for="(item,key) in cardList" :key='key'>
        <div slot="header">
          <span>{{item.trainConfig.form.trainName}}</span>
        </div>
        <div class="text line">
          <span>
            <span class="m-20">预测准确率: </span>
            <span>{{item.trainConfig.trainMes.test.accuracy.toFixed(4)}}</span>
          </span>
          <span>
            <span class="m-20">预测准确率: </span>
            <span>{{item.trainConfig.trainMes.test.loss.toFixed(4)}}</span>
          </span>
        </div>
        <div class='img'  style="height: 100px">
          <span class='label m-20'>训练预览: </span>
          <el-image 
              style="width: 100px; height: 100px"
              :src="item.trainConfig.trainMes.imgUrl" 
              :preview-src-list="[item.trainConfig.trainMes.imgUrl]">
            </el-image>
        </div>  
        <div class="text item">
          <el-link style='margin-right:10px' type="primary" :underline="false" icon='el-icon-folder-add' @click="save(item)" >保存</el-link>
          <el-link  type="primary" :underline="false" icon="el-icon-edit">编辑</el-link>
        </div>
      </el-card>
    </el-drawer>
  </div>
</template>

<script>
import {queryMessage ,updateMessage,queryMessageCount} from '@/api/index/home.js';
import {saveModel} from '@/api/index/modelManage.js';
export default {
  name: 'headerModule',
  data() {
    return {
      isCollapse: false,
      drawer:false,
      value: '',
      count:0,
      countMes:0,
      cardList:[]
    }
  },
  methods: {
    changeMenu() {
      this.$emit('changeCollapse')
    },
    queryMes(){
      this.drawer = true
      this.count = 0
      this.countMes = 0
      if(this.drawer){
        queryMessage().then((res)=>{
          this.cardList = res
          updateMessage().then(() =>{})
        })
      }
    },
    queryMessageCount(){
      queryMessageCount().then((res)=>{
        this.count = res
        this.countMes = res
      })
    },
    // 模型保存
    save(item){
      let params = {
        form:item.trainConfig.form,
        trainData:item.trainConfig.trainMes
      }
      saveModel(params).then((res)=>{
        this.$message({
          message: '保存成功！',
          type: 'success'
        })
      })
    }
  },
  mounted(){
    this.queryMessageCount();
    let namespace = '/mes';
    // require('socket.io-client')(location.protocol + '//' + document.domain + ':' + location.port + namespace);
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);
    // var socket = require('socket.io-client')(location.protocol + '//' + document.domain + ':' + location.port + namespace);
    socket.on('connect', function() {
        socket.emit('mes', {data: 'I\'m connected!'});
    });
    var that = this
    socket.on('train', (msg)=>{
      // console.log(msg)
      //  this.$message({
      //     message: '训练成功，请在消息中查看！',
      //     type: 'success'
      //   });
      that.count = that.count?that.count:0 + 1
      if(that.count>99){
        that.countMes = '99+'
      }else{
        that.countMes = that.count
      }
      that.$notify({
        title: '成功',
        message: '训练成功，请在消息中查看！',
        type: 'success',
        position: 'top-left'
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
    margin-left: -10px;
    margin-top: 16px;
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
  padding:0px 20px 0px;
  box-sizing: border-box;
}
/deep/.el-card{
  background:#353c48;
  border: 1px solid #353c48;
  .text{
    color:white;
    font-size:12px;
    height: 40px;
    line-height: 40px;
  }
  .line{
    display:flex;
    justify-content: space-between;
  }
  .item{
    display: flex;
    justify-content:flex-end;
  }
  .m-20{
    margin-right:20px;
  }
  .img{
    display: flex;
    height: 100px;
    color: white;
    font-size: 12px;
    .label{
      height: 20px;
      line-height: 20px;
    }
  }
  /deep/.el-card__header{
    color:#fb9678;
    height: 40px;
    padding: 0px 18px;
    font-size:14px;
    div{
      height: 40px;
      line-height: 40px;
    }
  }
  /deep/.el-card__body{
    padding:20px 20px 0px 20px;
  }
}
</style>

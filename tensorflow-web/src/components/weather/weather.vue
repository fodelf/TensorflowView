<!--
 * @Description: 描述
 * @Author: pym
 * @Github: https://github.com/fodelf
 * @Date: 2020-04-06 16:39:24
 * @LastEditors: pym
 * @LastEditTime: 2020-09-06 19:48:37
 -->
<template>
  <div class="weather">
    <div class="temperature">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>总数</el-breadcrumb-item>
        <el-breadcrumb-item>正常</el-breadcrumb-item>
        <el-breadcrumb-item>错误</el-breadcrumb-item>
      </el-breadcrumb>
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>{{systemStatus.dataSum.total}}</el-breadcrumb-item>
        <el-breadcrumb-item class='success-item'>{{systemStatus.dataSum.success}}</el-breadcrumb-item>
        <el-breadcrumb-item class='fail-item'>{{systemStatus.dataSum.fail}}</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <p class='title'>系统状态{{systemStatus.todayState==='good' ? '优': systemStatus.todayState==='normal' ? '中等' : '差'}}</p>
    <div class="weatherBg">
      <div class="iconfont" :class="systemStatus.todayState==='good' ? 'icon-taiyang-copy': systemStatus.todayState==='normal' ? 'icon-ziyuan' : 'icon-ziyuan1'"></div>
      <div class="weatherDate">{{systemStatus.realTime}}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'weather',
  props:['systemStatus'],
  data() {
    return {}
  },
  methods: {},
  created() {
    
  }
}
</script>

<style lang="less" scoped>
.weather {
  width: 100%;
  height: 100%;
  background: #01c0c8;
  padding: 20px;
  // display: flex;
  position: relative;
  .temperature {
    // flex: 0 0 50%;
    width: 50%;
    position: absolute;
    left: 20px;
    bottom: 10px;
    color: #fff;
    /deep/.el-breadcrumb {
      margin-bottom:8px;
      .el-breadcrumb__item {
        .el-breadcrumb__inner {
          color:#fff;
        }
      }
      .success-item {
        .el-breadcrumb__inner {
           color:green;
        }
      }
      .fail-item {
        .el-breadcrumb__inner {
           color:red;
        }
      }
    }
  }
  .title {
    position:absolute;
    left:50%;
    top:50%;
    margin-top:-20px;
    margin-left:-60px;
    height:40px;
    width:120px;
    color:#fff;
    font-size:20px;
  }
  .weatherBg {
    flex: 0 0 50%;

    .iconfont {
      font-size: 26px;
      color: #fff;
      display: flex;
      width: 100%;
      justify-content: flex-end;
      margin-bottom: 10px;
    }
    .weatherDec {
      color: #fff;
      font-size: 14px;
      display: flex;
      width: 100%;
      margin-bottom: 8px;
      justify-content: flex-end;
    }
    .weatherDate {
      font-size: 14px;
      display: flex;
      width: 100%;
      justify-content: flex-end;
      color: #fff;
      opacity: 0.5;
    }
  }
}
</style>

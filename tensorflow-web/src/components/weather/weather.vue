<!--
 * @Description: 描述
 * @Author: pym
 * @Github: https://github.com/fodelf
 * @Date: 2020-04-06 16:39:24
 * @LastEditors: pym
 * @LastEditTime: 2020-09-06 19:48:37
 -->
<template>
  <div class="weather" :style="{background:isgood?'#01c0c8':'#fb9678'}">
    <div class="temperature">
      <div class="value"><span>准确率：</span><span>{{systemStatus.accuracy.toFixed(4)}}</span></div>
      <div class="value"><span>损失值：</span><span>{{systemStatus.loss.toFixed(4)}}</span></div>
      <!-- <el-breadcrumb separator="/">
        <el-breadcrumb-item>总数</el-breadcrumb-item>
        <el-breadcrumb-item>正常</el-breadcrumb-item>
        <el-breadcrumb-item>错误</el-breadcrumb-item>
      </el-breadcrumb>
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>{{systemStatus.dataSum.total}}</el-breadcrumb-item>
        <el-breadcrumb-item class='success-item'>{{systemStatus.dataSum.success}}</el-breadcrumb-item>
        <el-breadcrumb-item class='fail-item'>{{systemStatus.dataSum.fail}}</el-breadcrumb-item>
      </el-breadcrumb> -->
    </div>
    <p v-if='isgood' class='title'>最优模型  {{systemStatus.modelName}}</p>
    <p v-if='!isgood' class='title'>最差模型  {{systemStatus.modelName}}</p>
    <div class="weatherBg">
      <div class="iconfont" :class="isgood ? 'icon-taiyang-copy':'icon-ziyuan1'"></div>
      <div class="weatherDate">{{dateFormat("YYYY/mm/dd",systemStatus.time)}}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'weather',
  props:['systemStatus','isgood'],
  data() {
    return {}
  },
  methods: {
    dateFormat(fmt, date) {
      date = new Date(date);
      let ret;
      const opt = {
          "Y+": date.getFullYear().toString(),        // 年
          "m+": (date.getMonth() + 1).toString(),     // 月
          "d+": date.getDate().toString(),            // 日
          "H+": date.getHours().toString(),           // 时
          "M+": date.getMinutes().toString(),         // 分
          "S+": date.getSeconds().toString()          // 秒
          // 有其他格式化字符需求可以继续添加，必须转化成字符串
      };
      for (let k in opt) {
          ret = new RegExp("(" + k + ")").exec(fmt);
          if (ret) {
              fmt = fmt.replace(ret[1], (ret[1].length == 1) ? (opt[k]) : (opt[k].padStart(ret[1].length, "0")))
          };
      };
      return fmt;
    }
  },
  created() {
    
  }
}
</script>

<style lang="less" scoped>
.weather {
  width: 100%;
  height: 100%;
  // background: #01c0c8;
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
  .value{
    font-size: 12px;
  }
}
</style>

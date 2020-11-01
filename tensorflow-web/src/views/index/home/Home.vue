<!--
 * @Author: 吴文周
 * @Date: 2020-04-12 16:16:34
 * @LastEditTime: 2020-09-22 09:00:58
 * @LastEditors: 吴文周
 * @Description: 首页模块
 * @FilePath: /workespacemanger/src/views/home/Home.vue
 -->
<template>
  <div class="home">
    <div class="cardGroup">
      <div v-for="(item, index) in cardList" :key="index" class="cardItem">
        <!--卡片组件-->
        <cardNum :card="item"></cardNum>
      </div>
    </div>
    <div class="row chartRow">
      <div class="chartBox">
        <div class="realChart">
          <el-row :gutter="20" class='titleRow'>
            <el-col :span='20' class='title'>
              日常请求记录
            </el-col>
            <el-col :span='4'>
              <el-select v-model="serviceType" @change="queryChart">
                <!-- <el-option label='全部' value='all'></el-option> -->
                <el-option v-for="(item,index) in serviceList" :key="index" :label='item.serviceName' :value='item.serverId'></el-option>
              </el-select>
            </el-col>
          </el-row>
          <!--折线图组件-->
          <barLinesChart :chartData ='chartData'></barLinesChart>
        </div>
      </div>
      <div class="rightRow">
        <div class="realRight">
          <div class="weather">
            <div class="realWeather">
              <!--播报状态组件-->
              <weather :systemStatus='systemStatus'></weather>
            </div>
          </div>
          <div class="advertisement rowBox">
            <!--轮播图广告招租组件-->
            <carousel :carouselList="carouselList" v-if='carouselList.length > 0'></carousel>
            <div v-else class='noData'>暂无异常</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import home from './home.js'
export default {
  ...home
}
</script>

<style lang="less" scoped>
@import './home.less';
</style>

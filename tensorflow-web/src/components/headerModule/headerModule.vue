<!--
 * @Description: 描述
 * @Author: pym
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-30 23:29:01
 * @LastEditors: pym
 * @LastEditTime: 2020-04-06 18:22:28
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

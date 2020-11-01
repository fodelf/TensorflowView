<!--
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-09-06 15:27:04
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-09-09 19:15:05
-->
<template>
  <div class="projectManage">
    <div class="leftMenu">
      <!--左侧列表组件-->
      <menuList :menuObj="menuObj" @clickMenu="selectMenu"></menuList>
    </div>
    <div class="rightList">
      <p class="rightTit clearfix">
        <el-button type="primary" icon="el-icon-plus" @click="addPro"
          >新增</el-button
        >
      </p>
      <!--表格组件-->
      <div class="tableCon">
        <tableBox
          ref="table"
          :dataList="dataList"
          :headerList="headerList"
          :actionType ="'project'"
          @editRow="editRow"
          @deleteRow="deleteRow"
          @checkRow="checkRow"
        ></tableBox>
      </div>
    </div>
  </div>
</template>

<script>
import dataManage from './dataManage.js'
export default {
  ...dataManage
}
</script>

<style rel="stylesheet/less" lang="less" scoped>
@import './dataManage.less';
</style>

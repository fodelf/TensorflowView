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
        <!-- <el-input
          v-model="keyword"
          class="keyInpt"
          placeholder="请输入关键字"
        ></el-input> -->
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
      <!-- <div class="tableCon">
        <compCard
            :compCardList="dataList"
            @edit="editRow"
            @delete='deleteRow'
            :getList="getList"
            :tablePag="tablePag"
            @changePageNo="getPageNo"
            @action ="action"
          ></compCard>
      </div> -->
    </div>
    <!--弹窗组件-->
    <!-- <proDialog
      ref="proDialog"
      :itemObj="itemObj"
      :type="type"
      @getList="getList"
    ></proDialog> -->
  </div>
</template>

<script>
import projectManage from './projectManage.js'
export default {
  ...projectManage
}
</script>

<style rel="stylesheet/less" lang="less" scoped>
@import './projectManage.less';
</style>

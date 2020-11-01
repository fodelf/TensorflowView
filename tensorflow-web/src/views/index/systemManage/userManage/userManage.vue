<!--
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-08-11 14:26:07
 * @LastEditors: pym
 * @LastEditTime: 2020-08-11 14:57:50
-->
<template>
  <div class='userManage'>
    <p class='title'>
      <el-button type='primary'>同步钉钉</el-button> 
    </p>
    <el-table :data="tableData" border>
      <el-table-column v-for="(item,index) in headerList" :key='index' :label="item.name">
        <template slot-scope="scope">
          <span>{{ scope.row[item.code] ? scope.row[item.code] : '--' }}<i class='el-icon-edit'></i></span>
        </template>
      </el-table-column>
    </el-table>
    <div class="pageBox clearfix">
      <el-pagination
        background
        @current-change="handleCurrentChange"
        :current-page="tablePag.pageNo"
        :page-size="tablePag.pageSize"
        layout="total, prev, pager, next, jumper"
        :total="tablePag.totalRecord">
      </el-pagination>
    </div>
  </div>
</template>

<script>
import userManage from './userManage.js'
export default {
  ...userManage
}
</script>

<style lang="less" scoped>
@import './userManage.less';
</style>
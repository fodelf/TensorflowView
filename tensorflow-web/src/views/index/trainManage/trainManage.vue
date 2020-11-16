<!--
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-09-06 15:27:04
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-16 09:14:49
-->
<template>
  <div class="projectManage">
    <div class="rightList">
      <p class="rightTit clearfix">
        <el-button type="primary" icon="el-icon-plus" @click="addPro"
          >新增</el-button
        >
      </p>
      <!--表格组件-->
      <div class="tableBox">
        <el-table
          :data="tableData"
          style="width: 100%">
          <el-table-column
            prop="trainName"
            label="训练名称"
           >
          </el-table-column>
          <el-table-column
            prop="dataName"
            label="数据源名称"
            >
          </el-table-column>
          <el-table-column
            prop="accuracy"
            label="准确率">
          </el-table-column>
          <el-table-column
            prop="loss"
            label="损失值">
          </el-table-column>
          <el-table-column
            prop="time"
            label="创建时间">
          </el-table-column>
            <el-table-column label="操作" width="250">
            <template slot-scope="scope">
              <el-button type="primary" @click="handleCheck(scope.row)">查看</el-button>
              <el-button type="primary" @click="handleEdit(scope.row)">编辑</el-button>
              <el-button type="primary" @click="saveModel(scope.row)">保存</el-button>
              <el-button type="danger" @click="handleDelete(scope.row)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
    <el-dialog :title="itemObj.modelName" :visible.sync="dialogTableVisible">
      <scriptCard :itemObj='itemObj' @cancle ='cancle()'></scriptCard>
    </el-dialog>
  </div>
</template>

<script>
import trainManage from './trainManage.js'
export default {
  ...trainManage
}
</script>

<style rel="stylesheet/less" lang="less" scoped>
@import './trainManage.less';
</style>

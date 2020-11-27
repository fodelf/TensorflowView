<!--
 * @Descripttion:
 * @version:
 * @Author: pym
 * @Date: 2020-09-06 15:56:41
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-25 09:15:34
-->
<template>
  <div class='projectAdd'>
  <el-form ref="form" :model="form"  :inline="true"  label-width='150px' label-position="left">
    <div @click='cancel' style="width:80px"><i class="el-icon-d-arrow-left" style="color:white;font-size:14px;cursor: pointer;margin-bottom: 20px;"   >返回</i></div>
    <el-tabs>
      <el-tab-pane label="基本信息"></el-tab-pane>
    </el-tabs>
    <el-row>
      <el-col :span='8'>
        <el-form-item label="调用路径">
         <span style='color:white'>{{url}}</span>
        </el-form-item>
      </el-col>
      <el-col :span='8'>
        <el-form-item label="请求头">
         <span style='color:white'>content-type:application/json</span>
        </el-form-item>
      </el-col>
      <el-col :span='8'>
        <el-form-item label="请求方式">
         <span style='color:white'>POST</span>
        </el-form-item>
      </el-col>
    </el-row>
    <el-row >
      <el-col :span='16'>
        <el-form-item label="调用参数" >
           <el-input
              type="textarea"
              v-model="param"
              :rows="15"
              resize="none"
            ></el-input>
        </el-form-item>
      </el-col>
    </el-row>
    <el-row >
      <el-col :span='24'>
        <span style='color:white;font-size:14px'>按照以上方式即可完成你的调用，来试试吧！预测一下！</span>
      </el-col>
    </el-row>
    <el-tabs>
      <el-tab-pane label="数据预览"></el-tab-pane>
    </el-tabs>
    <el-row >
      <el-form-item label="原始结果">
          <span style='color:white'>{{org}}</span>
        </el-form-item>
    </el-row>
    <el-row>
      <el-form-item>
          <el-button type="primary" @click="test">调用</el-button>
      </el-form-item>
    </el-row>
    <el-row>
      <el-col :span='16'>
        <el-form-item label="返回预览">
           <el-input
              type="textarea"
              v-model="res"
              :rows="15"
              resize="none"
            ></el-input>
        </el-form-item>
      </el-col>
    </el-row>
  </el-form>
  </div>
</template>

<script>
import modelAction from './modelAction.js'
export default {
  ...modelAction
}
</script>

<style lang="less" scoped>
@import './modelAction.less';
@border-color: #4f5467;
@bg-color: #353c48;
.tableBox {
  // height: 100%;
  margin-bottom:20px;
  /deep/.el-table {
    background: @bg-color;
    border-color: @border-color;
    tr {
      color: #ced4da;

      th {
        background: @bg-color;
        border-color: @border-color;
      }
      td {
        background: @bg-color;
        border-color: @border-color;
        /deep/.el-button {
          height: 25px;
          line-height: 25px;
          padding: 0 10px;
        }
      }
    }
  }
  .el-table::before {
    background: @border-color;
  }
  .el-table::after {
    background: @border-color;
  }
  .pageBox {
    width: 100%;
    margin-top: 5px;
    /deep/.el-pagination {
      float: right;
      .btn-prev {
        background: #303641;
      }
      .btn-next {
        background: #303641;
      }
      .el-input__inner {
        background: #303641;
      }
    }
  }
}
</style>
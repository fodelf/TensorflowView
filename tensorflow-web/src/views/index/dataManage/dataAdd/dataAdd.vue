<!--
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-09-06 15:56:41
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-02 09:23:08
-->
<template>
  <el-form ref="ruleForm" :model="ruleForm" :rules='serviceRules' :inline="true" class='projectAdd' label-width='150px' label-position="left" :disabled="$route.query.type=='check'">
    <div @click='cancel' style="width:80px"><i class="el-icon-d-arrow-left" style="color:white;font-size:14px;cursor: pointer;margin-bottom: 20px;"   >返回</i></div>
    <el-tabs v-model="baseInfo">
      <el-tab-pane label="基本信息" name="baseInfo"></el-tab-pane>
    </el-tabs>
    <el-row :gutter=20>
      <el-col :span='8'>
        <el-form-item label="数据源名称" prop='serviceName'>
          <el-input type='text' v-model="ruleForm.serviceName" placeholder="请输入英文或者数字"></el-input>
        </el-form-item>
      </el-col>
      <el-col :span='8'>
        <el-form-item label="数据源类型" prop='serviceType'>
          <el-select v-model="ruleForm.serviceType" placeholder="请选择服务类型">
            <el-option v-for="item in serverList" :key='item.value' :label='item.label' :value='item.value'></el-option>
          </el-select>
        </el-form-item>
      </el-col>
    </el-row>
    <el-row :gutter=20>
      <el-col :span='8'>
        <el-form-item label="上传文件">
          <el-upload
            class="upload-demo"
            action="/api/v1/data/upload"
            accept="csv"
            :limit="1"
            :multiple="false"
            :on-success="getFile"
            >
            <el-button size="small" type="primary" class="el-icon-plus"
              >点击上传</el-button
            >
          </el-upload>
        </el-form-item>
      </el-col>
    </el-row>
     <el-form-item>
        <el-button type="primary" @click="saveRule" v-if="$route.query.type === 'add'">保存</el-button>
        <el-button type="primary" @click="updateRule" v-if="$route.query.type === 'edit'">保存</el-button>
        <el-button type='default' @click='cancel' v-if="$route.query.type != 'check'">取消</el-button>
     </el-form-item>
  </el-form>
</template>

<script>
import dataAdd from './dataAdd.js'
export default {
  ...dataAdd
}
</script>

<style lang="less" scoped>
@import './dataAdd.less';
</style>
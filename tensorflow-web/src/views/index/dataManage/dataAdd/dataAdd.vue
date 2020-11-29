<!--
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-09-06 15:56:41
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-25 08:40:07
-->
<template>
  <el-form ref="form" :model="form" :rules='dataRules' :inline="true" class='projectAdd' label-width='150px' label-position="left" :disabled="$route.query.type=='check'">
    <div @click='cancel' style="width:80px"><i class="el-icon-d-arrow-left" style="color:white;font-size:14px;cursor: pointer;margin-bottom: 20px;"   >返回</i></div>
    <el-tabs>
      <el-tab-pane label="基本信息"></el-tab-pane>
    </el-tabs>
    <el-row :gutter=20>
      <el-col :span='8'>
        <el-form-item label="数据源名称" prop='dataName'>
          <el-input type='text' v-model="form.dataName" placeholder="请输入英文或者数字"></el-input>
        </el-form-item>
      </el-col>
      <el-col :span='8'>
        <el-form-item label="数据源类型" prop='dataType'>
          <el-select v-model="form.dataType" placeholder="请选择服务类型">
            <el-option v-for="item in serverList" :key='item.dataId' :label='item.dataName' :value='item.dataId'></el-option>
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
            :before-upload="beforeAvatarUpload"
            accept="csv"
            :limit="1"
            :multiple="false"
            :on-success="getFile"
            >
            <el-button size="small" type="primary" class="el-icon-plus"
              >点击上传</el-button
            >
            <div slot="tip" class="el-upload__tip">只能上传csv文件，且不超过500kb</div>
          </el-upload>
        </el-form-item>
      </el-col>
    </el-row>
     <el-form-item>
        <el-button type="primary" @click="save" v-if="$route.query.type === 'add'">保存</el-button>
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
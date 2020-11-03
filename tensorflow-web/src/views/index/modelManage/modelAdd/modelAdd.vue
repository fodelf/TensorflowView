<!--
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-09-06 15:56:41
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-03 20:44:21
-->
<template>
  <el-form ref="form" :model="form" :rules='dataRules' :inline="true" class='projectAdd' label-width='150px' label-position="left" :disabled="$route.query.type=='check'">
    <div @click='cancel' style="width:80px"><i class="el-icon-d-arrow-left" style="color:white;font-size:14px;cursor: pointer;margin-bottom: 20px;"   >返回</i></div>
    <el-tabs v-model="baseInfo">
      <el-tab-pane label="基本信息"></el-tab-pane>
    </el-tabs>
    <el-row :gutter=20>
      <el-col :span='8'>
        <el-form-item label="模型名称" prop='dataName'>
          <el-input type='text' v-model="form.dataName" placeholder="请输入英文或者数字"></el-input>
        </el-form-item>
      </el-col>
      <el-col :span='8'>
        <el-form-item label="数据源" prop='dataType'>
          <el-select v-model="form.dataType" placeholder="数据源">
            <el-option v-for="item in serverList" :key='item.dataId' :label='item.dataName' :value='item.dataId'></el-option>
          </el-select>
        </el-form-item>
      </el-col>
    </el-row>
     <el-form-item>
        <el-button type="primary" @click="train" v-if="$route.query.type === 'add'">训练</el-button>
        <el-button type="primary" @click="save" v-if="$route.query.type === 'add'">保存</el-button>
        <el-button type="primary" @click="updateRule" v-if="$route.query.type === 'edit'">保存</el-button>
        <el-button type='default' @click='cancel' v-if="$route.query.type != 'check'">取消</el-button>
     </el-form-item>
    <el-row :gutter=20>
      <el-image :src="src" v-if="src"></el-image>
    </el-row>
  </el-form>
</template>

<script>
import modelAdd from './modelAdd.js'
export default {
  ...modelAdd
}
</script>

<style lang="less" scoped>
@import './modelAdd.less';
</style>
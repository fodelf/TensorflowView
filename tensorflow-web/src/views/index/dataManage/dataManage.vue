<!--
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-09-06 15:27:04
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-16 09:20:48
-->
<template>
  <div class="projectManage">
    <div class="leftMenu">
      <!--左侧列表组件-->
      <menuList :menuObj="menuObj" @clickMenu="selectMenu"></menuList>
    </div>
    <div class="rightList">
      <p class="rightTit clearfix">
        <el-button size="small" style="margin-right:20px" type="primary" icon="el-icon-plus" @click="addPro">新增数据源</el-button>
        <el-button size="small"  type="primary" icon="el-icon-plus" @click="addTrain" v-if="menuObj.total >0">新增训练</el-button>
      </p>
      <!--表格组件-->
      <div class="tableBox">
      <el-table
        :data="tableData"
        row-key="id"
        style="width: 100%">
        <!-- <el-table-column type="expand">
          <template slot-scope="props">
             <div v-loading="expandTableLoding" style="height:60px;">
                <div v-if=" props.row.children.length == 0" style="text-align: center;">暂无数据</div>
                <div v-else v-for="(item, key) in props.row.children" :key="key" style="height:20px">
                   <el-form>
                     <el-row :gutter="20">
                      <el-col :span="6">
                        <el-form-item label="训练名称">
                          {{item.trainName}}
                        </el-form-item>
                      </el-col>
                      <el-col :span="6">
                        <el-form-item label="训练准确率">
                           {{item.accuracy.toFixed(4)}}
                        </el-form-item>
                      </el-col>
                      <el-col :span="6">
                        <el-form-item label="训练损失值">
                           {{item.loss.toFixed(4)}}
                        </el-form-item>
                      </el-col>
                      <el-col :span="6">
                        <el-link style='margin-right:10px' type="primary" :underline="false" icon='el-icon-folder-add' @click="save(item)" >保存</el-link>
                        <el-link  type="primary" :underline="false" icon="el-icon-edit">编辑</el-link>
                        <el-link  type="primary" :underline="false" icon="el-icon-edit">删除</el-link>
                      </el-col>
                    </el-row>
                    </el-form>
                </div>
            </div>
          </template>
        </el-table-column> -->
        <el-table-column
          label="数据源名称"
          prop="dataName">
        </el-table-column>
        <el-table-column
          label="文件名称"
          prop="fileName">
        </el-table-column>
        <el-table-column
          label="文件大小"
          prop="fileSize">
        </el-table-column>
        <el-table-column
          label="上传时间"
          prop="time">
        </el-table-column>
       </el-table>
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

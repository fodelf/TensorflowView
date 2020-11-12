<!--
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-09-06 15:56:41
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-11 08:50:29
-->
<template>
  <el-form ref="form" :model="form" :rules='dataRules' :inline="true" class='projectAdd' label-width='150px' label-position="left" :disabled="$route.query.type=='check'">
    <div @click='cancel' style="width:80px"><i class="el-icon-d-arrow-left" style="color:white;font-size:14px;cursor: pointer;margin-bottom: 20px;"   >返回</i></div>
    <el-tabs>
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
          <el-select v-model="form.dataType" placeholder="数据源"  @change="handleChangeDataType()">
            <el-option v-for="item in serverList" :key='item.id' :label='item.dataName' :value='item.id'></el-option>
          </el-select>
        </el-form-item>
      </el-col>
    </el-row>
     <el-row :gutter=20>
      <el-col :span='8'>
        <el-form-item label="神经网络层数" prop='number'>
          <el-input-number v-model="form.number"  :min="2" :max="100000"></el-input-number>
        </el-form-item>
      </el-col>
      <el-col :span='8'>
        <el-form-item label="激活函数" prop='activeFuns'>
          <el-select v-model="form.activeFunction" placeholder="激活函数">
            <el-option v-for="item in activeFuns" :key='item.label' :label='item.label' :value='item.value'></el-option>
          </el-select>
        </el-form-item>
      </el-col>
      <el-col :span='8'>
        <el-form-item label="训练次数" prop='times'>
           <el-input-number v-model="form.times"  :min="2" :max="100000"></el-input-number>
        </el-form-item>
      </el-col>
    </el-row>
    <el-tabs>
      <el-tab-pane label="数据预览"></el-tab-pane>
    </el-tabs>
      <el-row>
        <el-form-item label="设置输出列">
        </el-form-item>
      </el-row>
    <div  class="tableBox" ref="tableBox">
        <el-table :data="dataList"  style="width:100%" ref="mainTable">
          <el-table-column
            v-for="(item) in headerList"
            :key="item.code"
            :label="item.name"
          >
            <template slot="header" slot-scope="scope">
              <span>{{item.name}}</span>
              <span style="margin-left: 10px;">
                <el-radio v-model="form.target" :label='item.name' v-if ="item.name !='首列'" @change="changeTarget()">{{item.radio}}</el-radio>
              </span>
            </template>
            <template slot-scope="scope">
              <!-- {{item.showValue}} -->
              {{ scope.row[item.code] || scope.row[item.code] ==0 ? scope.row[item.code] : '--' }}
            </template>
          </el-table-column>
        </el-table>
      </div>
      <el-tabs>
        <el-tab-pane label="评估模型"></el-tab-pane>
      </el-tabs>
      <el-row :gutter=20>
         <el-col :span='8'>
          <el-form-item label="预测准确率">
            <span class='labelText'>{{trainData.test.accuracy}}</span>
          </el-form-item>
         </el-col>
         <el-col :span='8'>
          <el-form-item label="损失值">
             <span class='labelText'>{{trainData.test.loss}}</span>
          </el-form-item>
         </el-col>
      </el-row>
      <el-tabs>
      <el-tab-pane label="预测试数据"></el-tab-pane>
      </el-tabs>
      <el-row :gutter=20>
          <div class='tableBox'>
            <el-table :data="preDataList"  style="width:100%" ref="mainTable">
              <el-table-column
                v-for="(item) in preHeadList"
                :key="item.code"
                :label="item.name"
              >
                <template slot-scope="scope">
                  <el-input v-model="scope.row[item.code]"></el-input>
                </template>
              </el-table-column>
            </el-table>
          </div>
      </el-row>
      <el-row :gutter=20>
         <el-col :span='8'>
          <el-form-item label="预测值">
            <span class='labelText'>{{prData}}</span>
          </el-form-item>
         </el-col>
     </el-row>
     <el-form-item>
        <el-button type="primary" v-loading.fullscreen.lock="fullscreenLoading"  @click="train" v-if="$route.query.type === 'add'">训练</el-button>
        <!-- <el-button type="primary" ></el-button> -->
        <el-button type="primary" @click="preTrain" v-if="isTrain">预测试</el-button>
        <el-button type="primary" @click="save" v-if="$route.query.type === 'add'">保存</el-button>
        <el-button type="primary" @click="updateRule" v-if="$route.query.type === 'edit'">保存</el-button>
        <el-button type='default' @click='cancel' v-if="$route.query.type != 'check'">取消</el-button>
     </el-form-item>
    <el-row :gutter=20>
      <el-image :src="trainData.imgUrl" v-if="trainData.imgUrl"></el-image>
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
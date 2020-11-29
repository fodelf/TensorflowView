<!--
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-09-06 15:56:41
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-24 09:41:42
-->
<template>
  <div class='projectAdd'>
  <el-form ref="form" :model="form" :rules='dataRules' :inline="true"  label-width='150px' label-position="left" :disabled="$route.query.type=='check'">
    <div @click='cancel' style="width:80px"><i class="el-icon-d-arrow-left" style="color:white;font-size:14px;cursor: pointer;margin-bottom: 20px;"   >返回</i></div>
    <el-tabs>
      <el-tab-pane label="基本信息"></el-tab-pane>
    </el-tabs>
    <el-row :gutter=20>
      <el-col :span='8'>
        <el-form-item label="模型名称" prop='dataName'>
          <el-input type='text' v-model="form.trainName" placeholder="请输入英文或者数字"></el-input>
        </el-form-item>
      </el-col>
      <el-col :span='8'>
        <el-form-item label="数据源" prop='dataType'>
          <el-select v-model="form.dataId" placeholder="数据源"  @change="handleChangeDataType()">
            <el-option v-for="item in serverList" :key='item.dataId' :label='item.dataName' :value='item.dataId'></el-option>
          </el-select>
        </el-form-item>
      </el-col>
       <el-col :span='8'>
        <el-form-item label="训练次数" prop='times'>
           <el-input-number v-model="form.times"  :min="100" :max="100000"></el-input-number>
        </el-form-item>
      </el-col>
    </el-row>
     <el-row :gutter=20>
      <!-- <el-col :span='8'>
        <el-form-item label="神经网络层数" prop='number'>
          <el-input-number v-model="form.number"  :min="1" :max="100000"></el-input-number>
        </el-form-item>
      </el-col> -->
      <!-- <el-col :span='8'>
        <el-form-item label="激活函数" prop='activeFuns'>
          <el-select v-model="form.activeFunction" placeholder="激活函数">
            <el-option v-for="item in activeFuns" :key='item.label' :label='item.label' :value='item.value'></el-option>
          </el-select>
        </el-form-item>
      </el-col> -->
      <!-- <el-col :span='8'>
        <el-form-item label="训练次数" prop='times'>
           <el-input-number v-model="form.times"  :min="100" :max="100000"></el-input-number>
        </el-form-item>
      </el-col> -->
    </el-row>
    <el-row :gutter=20>
      <el-col :span='8'>
        <el-form-item label="模型类型" prop='learnType'>
          <el-select v-model="form.learnType" placeholder="模型类型">
            <el-option v-for="(item1,index) in typeList" :key='index' :label='item1.label' :value='item1.value'></el-option>
          </el-select>
        </el-form-item>
      </el-col>
      <el-col :span='16' style="color:#ced4da;font-size:12px;line-height: 40px;">
        <span v-if="form.learnType=='regression'">预测出如价格或概率这样连续值的输出（如，预测房价趋势）</span>
        <span v-else>从一系列的分类出选择出一个分类（如，给出包含苹果或橘子数据，识别出是哪种水果）</span>
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
      </el-form>
      <el-form ref="trainForm">
      <el-tabs v-if="isTrain">
        <el-tab-pane label="评估模型"></el-tab-pane>
      </el-tabs>
      <el-row :gutter=20 v-if="isTrain">
         <el-col :span='8'>
          <el-form-item label="预测准确率" v-if="form.learnType=='classification'">
            <span class='labelText'>{{trainData.test.accuracy}}</span>
          </el-form-item>
          <el-form-item label="平均误差" v-else>
            <span class='labelText'>{{trainData.test.mae}}</span>
          </el-form-item>
         </el-col>
         <el-col :span='8'>
          <el-form-item label="损失值">
             <span class='labelText'>{{trainData.test.loss}}</span>
          </el-form-item>
         </el-col>
      </el-row>
      <el-tabs v-if="isTrain">
      <el-tab-pane label="预测试数据"></el-tab-pane>
      </el-tabs>
      <el-row :gutter=20 v-if="isTrain">
          <div class='tableBox'>
            <el-table :data="preDataList"  style="width:100%" ref="mainTable">
              <el-table-column
                v-for="(item) in preHeadList"
                :key="item.code"
                :label="item.name"
              >
                <template slot-scope="scope">
                  <el-input v-model="scope.row[item.code]"></el-input>
                   <!-- {{ scope.row[item.code] || scope.row[item.code] ==0 ? scope.row[item.code] : '--' }}  -->
                </template>
              </el-table-column>
            </el-table>
          </div>
      </el-row>
      <el-row :gutter=20 v-if="isTrain && form.learnType=='classification'">
         <el-col :span='8'>
          <el-form-item label="问题类型">
            <span class='labelText' v-if="trainData.group.length ==2">二元分类</span>
            <span class='labelText' v-if="trainData.group.length >2">多元分类</span>
          </el-form-item>
         </el-col>
         <el-col :span='16'>
          <el-form-item label="类型明细">
            <span class='labelText'>{{trainData.group.join(',')}}</span>
          </el-form-item>
         </el-col>
      </el-row>
      <el-row :gutter=20 v-if="isTrain && isShowPre && form.learnType =='classification' && trainData.group.length > 2">
         <el-col :span='24'>
          <el-form-item label="预测结果">
            <span class='labelText'>最大概率分类: {{max}}</span>
          </el-form-item>
         </el-col>
     </el-row>
      <el-row :gutter=20 v-if="isTrain && isShowPre && form.learnType =='classification'">
         <el-col :span='24'>
          <el-form-item label="预测明细">
            <span class='labelText' v-if="trainData.group.length ==2">类型为{{trainData.group[1]}}的概率是{{prData}}</span>
            <span class='labelText' v-if="trainData.group.length > 2">各个类型概率分布如下: {{prData}}</span>
          </el-form-item>
         </el-col>
     </el-row>
     <el-row :gutter=20 v-if="isTrain && form.learnType=='regression'">
         <el-col :span='6'>
          <el-form-item label="问题类型">
            <span class='labelText' v-if="trainData.group.length == 1">一元回归</span>
            <span class='labelText' v-else>多元回归</span>
          </el-form-item>
         </el-col>
      </el-row>
      <el-row :gutter=20 v-if="isTrain && isShowPre && form.learnType =='regression'">
         <el-col :span='24'>
          <el-form-item label="结论">
            <span class='labelText'>预测值是： {{prData}}</span>
          </el-form-item>
         </el-col>
     </el-row>
     <el-form-item>
        <el-button type="primary" v-loading.fullscreen.lock="fullscreenLoading"  @click="train" v-if="$route.query.type === 'add'">训练</el-button>
        <!-- <el-button type="primary" ></el-button> -->
        <el-button type="primary" @click="preTrain" v-if="isTrain" >预测试</el-button>
        <el-button type="primary" @click="save"  v-if="isTrain" >保存为模型</el-button>
        <el-button type="primary" @click="updateRule" v-if="$route.query.type === 'edit'">保存</el-button>
        <el-button type='default' @click='cancel' v-if="$route.query.type != 'check'">取消</el-button>
     </el-form-item>
    <el-row :gutter=20>
      <el-image :src="trainData.imgUrl" v-if="trainData.imgUrl"></el-image>
    </el-row>
  </el-form>
  </div>
</template>

<script>
import trainAdd from './trainAdd.js'
export default {
  ...trainAdd
}
</script>

<style lang="less" scoped>
@import './trainAdd.less';
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
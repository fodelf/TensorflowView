<!--
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-09-06 15:56:41
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-09-24 09:13:09
-->
<template>
  <el-form ref="ruleForm" :model="ruleForm" :rules='serviceRules' :inline="true" class='projectAdd' label-width='150px' label-position="left" :disabled="$route.query.type=='check'">
    <div @click='cancel' style="width:80px"><i class="el-icon-d-arrow-left" style="color:white;font-size:14px;cursor: pointer;margin-bottom: 20px;"   >返回</i></div>
    <el-tabs v-model="baseInfo">
      <el-tab-pane label="基本信息" name="baseInfo"></el-tab-pane>
    </el-tabs>
    <el-row :gutter=20>
      <el-col :span='8'>
        <el-form-item label="服务名称" prop='serviceName'>
          <el-input type='text' v-model="ruleForm.serviceName" placeholder="请输入英文或者数字"></el-input>
        </el-form-item>
      </el-col>
      <el-col :span='8'>
        <el-form-item label="服务类型" prop='serviceType'>
          <el-select v-model="ruleForm.serviceType" placeholder="请选择服务类型">
            <el-option v-for="item in serverList" :key='item.value' :label='item.label' :value='item.value'></el-option>
          </el-select>
        </el-form-item>
      </el-col>
    </el-row>
    <el-row :gutter=20>
      <el-col :span='8'>
        <el-form-item label="服务地址" prop='serviceAddress'>
          <el-input type='text' v-model="ruleForm.serviceAddress" placeholder="示例：127.0.0.1"></el-input>
        </el-form-item>
      </el-col>
      <el-col :span='8'>
        <el-form-item label="服务端口" prop='servicePort'>
            <el-input type='text'  v-model.number="ruleForm.servicePort" placeholder="示例：3000"></el-input>
        </el-form-item>
      </el-col>
    </el-row>
    <el-row :gutter=20>
       <el-col :span="8">
         <el-form-item label="熔断" prop='serviceBreak'>
           <!-- <el-input type='text' v-model='ruleForm.serviceBreak' placeholder="请求超时时间"></el-input> -->
           <el-input type='text' v-model='ruleForm.serviceBreak' placeholder="请求错误百分百比例如25"></el-input>
         </el-form-item>
       </el-col>
       <el-col :span='8'>
        <el-form-item label="限流" prop='serviceLimit'>
           <el-input type='text' v-model="ruleForm.serviceLimit" placeholder="请求次数限制"></el-input>
         </el-form-item>
       </el-col>
     </el-row>
     <el-row>
      <!-- <label class="el-form-item__label" style="color: #ced4da;">代理规则（必须至少一个代理规则）</label> -->
      <el-form-item label="代理规则（必须至少一个代理规则）" label-width='250px' class='agency-item'>
        <el-button type='primary' icon="el-icon-plus" circle @click='addRule'></el-button>
      </el-form-item>
    </el-row>
    <!-- <el-form v-for="(item,index) in ruleForm.serviceRules" :key='index' label-width='150px' :inline="true"> -->
      <el-row :gutter=20 v-for="(item,index) in ruleForm.serviceRules" :key='index'>
        <el-row :gutter=20 style="padding-left: 10px;">
        <el-col :span='8'>
          <!-- /<el-form-item label="拦截地址" prop='interceptLoc' :rules="{ required: true, message: '请输入拦截地址', trigger: 'blur' }"> -->
          <el-form-item label="拦截地址" :prop="'serviceRules.'+index+'.url'"  :rules="rules.apiUrl">
            <el-input type='text' v-model="item.url"  placeholder="示例：/api,不能以ui开头"></el-input>
          </el-form-item>
        </el-col>
         <el-col :span='6' v-if="ruleForm.serviceRules.length > 1">
          <el-button type='primary' icon='el-icon-minus' circle @click='deleteRule(index)'></el-button>
        </el-col>
        </el-row>
        <el-row :gutter=20 style="padding-left: 10px;">
        <el-col :span='8'>
          <el-form-item label="重写前缀" :prop="'serviceRules.'+index+'.pathReWriteBefore'"  :rules="rules.pathReWriteBefore">
            <el-input type='text' v-model="item.pathReWriteBefore" placeholder="示例：/api"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span='8'>
          <el-form-item label="重写地址" :prop="'serviceRules.'+index+'.pathReWriteUrl'"  :rules="rules.pathReWriteUrl">
            <el-input type='text' v-model="item.pathReWriteUrl" placeholder="示例：/api"></el-input>
          </el-form-item>
        </el-col>
       </el-row>
      </el-row>
     <!-- </el-form> -->
    <!-- <el-row :gutter=20>
      <el-col :span='8'>
        <el-form-item label="描述信息" prop='serviceAddress'>
          <el-input type='text' v-model="ruleForm.serviceAddress" placeholder="示例：127.0.0.1"></el-input>
        </el-form-item>
      </el-col>
    </el-row> -->
     <el-tabs v-model="useConsul">
      <el-tab-pane label="注册中心服务信息配合consul使用" name="useConsul"></el-tab-pane>
    </el-tabs>
    <el-row :gutter=20>
       <el-col :span="8">
         <el-form-item label="服务ID">
           <el-input type='text' v-model='ruleForm.useConsulId' placeholder="请输入英文或者数字"></el-input>
         </el-form-item>
       </el-col>
       <el-col :span='8'>
        <el-form-item label="服务标签">
           <el-input type='text' v-model="ruleForm.useConsulTag" placeholder="请输入英文或者数字"></el-input>
         </el-form-item>
       </el-col>
     </el-row>
     <el-row :gutter=20>
       <el-col :span="8">
         <el-form-item label="监控检查接口" prop='useConsulCheckPath'>
           <el-input type='text' v-model='ruleForm.useConsulCheckPath' placeholder="示例：/checkHealth"></el-input>
         </el-form-item>
       </el-col>
       <!-- <el-col :span='8'>
        <el-form-item label="健康检查端口">
           <el-input type='text' v-model="ruleForm.useConsulPort" placeholder="默认使用服务端口"></el-input>
         </el-form-item>
       </el-col> -->
     </el-row>
     <el-row :gutter=20>
       <el-col :span="8">
         <el-form-item label="健康检查间隔(秒)" prop='useConsulInterval'>
           <el-input type='text' v-model='ruleForm.useConsulInterval' placeholder="默认10s"></el-input>
         </el-form-item>
       </el-col>
       <el-col :span='8'>
        <el-form-item label="健康检查超时时间(秒)" prop='useConsulTimeout'>
           <el-input type='text' v-model="ruleForm.useConsulTimeout" placeholder="默认3s"></el-input>
         </el-form-item>
       </el-col>
     </el-row>
     <el-tabs v-model="messageWarn">
      <el-tab-pane label="钉钉信息（消息告警）" name="messageWarn"></el-tab-pane>
    </el-tabs>
    <el-row :gutter=20>
       <el-col :span="8">
         <el-form-item label="钉钉accessToken">
           <el-input type='text' v-model='ruleForm.dingdingAccessToken' placeholder="请输入"></el-input>
         </el-form-item>
       </el-col>
       <el-col :span='8'>
        <el-form-item label="钉钉secret">
           <el-input type='text' v-model="ruleForm.dingdingSercet" placeholder="请输入"></el-input>
         </el-form-item>
       </el-col>
     </el-row>
     <el-row>
       <el-form-item label="钉钉联系人手机号">
          <el-tag type='warning' :key="tag" v-for="tag in ruleForm.dingdingList" closable :disable-transitions="false" @close="handleClose(tag)">
            {{tag}}
          </el-tag>
          <el-input class="input-new-tag" v-if="inputVisible" v-model="inputValue" ref="saveTagInput" size="small"
                    @keyup.enter.native="handleInputConfirm"
                    @blur="handleInputConfirm">
          </el-input>
          <el-button v-else class='button-new-tag' type='primary' size="small" @click="showInput" icon='el-icon-plus' circle></el-button>
        </el-form-item>
     </el-row>
     <el-form-item>
        <el-button type="primary" @click="saveRule" v-if="$route.query.type === 'add'">保存</el-button>
        <el-button type="primary" @click="updateRule" v-if="$route.query.type === 'edit'">保存</el-button>
        <el-button type='default' @click='cancel' v-if="$route.query.type != 'check'">取消</el-button>
     </el-form-item>
  </el-form>
</template>

<script>
import projectAdd from './projectAdd.js'
export default {
  ...projectAdd
}
</script>

<style lang="less" scoped>
@import './projectAdd.less';
</style>
<!--
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-08-18 11:02:53
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-09-09 09:18:12
-->
<template>
  <el-card class="box-card">
    <div slot="header" class="clearfix">
      <span>{{item.title}}</span>
      <el-button type="primary" class='editBtn' size='mini' @click='edit'>编辑</el-button>
    </div>
    <el-form label-width='100px' label-position="left">
      <el-form-item label='地址'>
        {{item.address}}
      </el-form-item>
      <el-form-item label='端口号'>
        {{item.port}}
      </el-form-item>
      <el-form-item label='用户名' v-if="item.type === 'rabbitMq'">
        {{item.userName}}
      </el-form-item>
      <el-form-item label='密码' v-if="item.type === 'rabbitMq'">
        {{item.password}}
      </el-form-item>
    </el-form>
  </el-card>
</template>

<script>
export default {
  name:'systemCard',
  props:{
    item: {
      type:Object,
      default:()=>{
        return {}
      }
    }
  },
  data() {
    return {
      
    }
  },
  methods: {
    edit() {
      this.$emit("showDialog",this._props.item)
    }
  }
}
</script>

<style lang='less' scoped>
.box-card {
  width: 100%;
  margin-bottom: 20px;
  height:250px;
  border:none;
  background-color: #353c48;
  color: #ced4da;
  box-sizing: border-box;
  
  /deep/.el-card__header {
    border-bottom:none;
    font-weight: 500;
    color: #ced4da;
    .editBtn {
      float:right;
      margin-right:10px;
    }
  }

  /deep/.el-form {
    .el-form-item {
      margin-bottom:10px;
      .el-form-item__label {
        line-height: 30px;
      }
      .el-form-item__content {
        line-height: 30px;
      }
    }
  }
}
</style>


<!--
 * @Description: 新建分支
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-04-05 16:32:04
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-05-13 15:58:40
 -->
<template>
  <el-dialog
    :visible="tempVisible"
    width="40%"
    :title="title"
    :before-close="close"
  >
  <el-form
      :model="proForm"
      :rules="proRules">
    <el-form-item label="分支类型">
      <el-select  v-model="proForm.type"></el-select>
    </el-form-item>
    <el-form-item label="分支号码">
      <el-input  v-model="proForm.code"></el-input>
    </el-form-item>
  </el-form>
  <el-row type="flex" justify="end">
    <el-form-item>
      <el-button type="primary" @click="confirm">确认</el-button>
      <el-button type="info" @click="close">取消</el-button>
    </el-form-item>
  </el-row>
  </el-dialog>
</template>

<script>
import { newBranch } from '@/api/index/projectManage.js'
export default {
  name: 'BranchDialog',
  props: ['itemObj'],
  data() {
    return {
      tempVisible: false,
       proForm: {
        type: '',
        code: ''
      },
      proRules: {
        type: [
          { required: true, message: '请选择分支类型', trigger: 'blur' }
        ],
        code: [
          { required: true, message: '请输入分支号码', trigger: 'blur' }
        ]
      },
    }
  },
  methods: {
    show() {
      this.tempVisible = true
    },
    close() {
      this.tempVisible = false
    },
    /**
     * @name: confirm
     * @description: 弹窗确认
     * @param {type}: 默认参数
     * @return {type}: 默认类型
     */
    confirm() {
     newBranch(this.tempForm).then(() => {
        this.$message({
          type: 'success',
          message: '开始创建分支'
        })
        this.close()
      })
    }
  }
}
</script>

<style lang="less" scoped>
/deep/.el-dialog {
  margin-top: 5vh !important;
  margin-bottom: 0;
  background-color: #303641;
  .el-dialog__header {
    border-bottom: 1px solid #4f5467;
    .el-dialog__title {
      color: #ced4da;
    }
  }
  .el-dialog__body {
    padding: 10px 20px;
    .el-form-item__label {
      color: #ced4da;
    }
    .el-input__inner {
      background-color: #353c48;
      border: none;
      color: #ced4da;
    }
    .el-textarea__inner {
      background-color: #353c48;
      border: none;
      color: #ced4da;
    }
    .el-radio__inner {
      background-color: #272c36;
      border: 1px #adb5bd solid;
      outline: none;
    }
    .is-checked {
      .el-radio__inner {
        background-color: #fb9678;
        border: 1px solid #fb9678;
      }
      .el-radio__label {
        color: #fb9678;
      }
    }
  }
}
</style>

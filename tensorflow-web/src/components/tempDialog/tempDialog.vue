<!--
 * @Description: 描述
 * @Author: pym
 * @Github: https://github.com/fodelf
 * @Date: 2020-04-05 16:32:04
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-09-04 10:17:22
 -->
<template>
  <el-dialog
    :visible="tempVisible"
    width="40%"
    :title="title"
    :before-close="close"
    v-if="tempVisible"
  >
    <el-form
      :model="tempForm"
      :rules="tempRules"
      ref="tempForm"
      label-width="100px"
      label-position="left"
    >
      <el-row :gutter="20">
        <el-col :span="12">
          <el-form-item label="模板名称" prop="templateName">
            <el-input
              v-model="tempForm.templateName"
              placeholder="请输入模板名称"
            ></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="模板类型" prop="type">
            <el-select v-model="tempForm.type">
              <el-option
                v-for="item in typeList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>
      </el-row>
      <el-form-item
        label="服务路径"
        prop="pathUrl"
        v-if="tempForm.addMethod === 'localImport'"
      >
        <el-input
          type="text"
          v-model="tempForm.pathUrl"
          placeholder="请输入服务路径"
        ></el-input>
      </el-form-item>
      <el-form-item label="Git路径" prop="gitUrl">
        <el-input
          type="text"
          v-model="tempForm.gitUrl"
          placeholder="请输入Git路径"
        ></el-input>
      </el-form-item>
      <el-form-item label="图片说明">
        <el-upload
          class="upload-demo"
          action="/api/upload"
          accept="image/jpeg,image/gif,image/png,image/jpg"
          :limit="1"
          :multiple="false"
          :on-success="getFile"
        >
          <el-button size="small" type="primary" class="el-icon-plus"
            >点击上传</el-button
          >
        </el-upload>
      </el-form-item>
      <el-form-item label="关键字" prop="keyword">
        <el-input
          type="text"
          v-model="tempForm.keyword"
          placeholder="请输入关键字"
        ></el-input>
      </el-form-item>
      <el-form-item label="模板描述">
        <el-input
          type="textarea"
          v-model="tempForm.dec"
          :rows="2"
          placeholder="请输入模板描述"
        ></el-input>
      </el-form-item>
      <el-row type="flex" justify="end">
        <el-form-item>
          <el-button type="primary" @click="confirm">确认</el-button>
          <el-button type="info" @click="close">取消</el-button>
        </el-form-item>
      </el-row>
    </el-form>
  </el-dialog>
</template>

<script>
import { addNewTemp, updateTemp } from '@/api/templateApi.js'
import { getProjectType } from '@/api/index/projectManage.js'
export default {
  name: 'tempDialog',
  props: ['itemObj', 'actionType'],
  data() {
    return {
      tempVisible: false,
      title: '',
      tempForm: {
        templateName: '',
        type: '',
        gitUrl: '',
        keyword: '',
        dec: '',
        decImg: ''
      },
      tempRules: {
        templateName: [
          { required: true, message: '请输入模板名称', trigger: 'blur' }
        ],
        type: [
          { required: true, message: '请输入模板类型', trigger: 'change' }
        ],
        gitUrl: [{ required: true, message: '请输入Git路径', trigger: 'blur' }],
        keyword: [{ required: true, message: '请输入关键字', trigger: 'blur' }]
      },
      typeList: [],
      file: null
    }
  },
  methods: {
    show() {
      this.title = this.$props.actionType == 'modify' ? '修改模板' : '新增模板'
      if (this.$props.actionType == 'modify') {
        this.tempForm = this.$props.itemObj
      } else {
        this.proForm = {
          templateName: '',
          type: '',
          gitUrl: '',
          keyword: '',
          dec: '',
          decImg: ''
        }
      }
      this.tempVisible = true
      this.queryTempTypeList()
    },
    close() {
      this.tempVisible = false
      this.$refs.tempForm.resetFields()
    },
    getFile(response) {
      this.tempForm.decImg = response.resultEntity
    },
    queryTempTypeList() {
      getProjectType({}).then(res => {
        this.typeList = res || []
      })
    },
    /**
     * @name: confirm
     * @description: 弹窗确认
     * @param {type}: 默认参数
     * @return {type}: 默认类型
     */
    confirm() {
      this.$refs.tempForm.validate(valid => {
        if (valid) {
          if (this.$props.actionType == 'add') {
            addNewTemp(this.tempForm).then(() => {
              this.$message({
                type: 'success',
                message: '新增模板成功'
              })
              this.$emit('getTempList',this.tempForm.type)
              this.close()
            })
          } else {
            updateTemp(this.tempForm).then(() => {
              this.$message({
                type: 'success',
                message: '修改模板成功'
              })
              this.$emit('getTempList')
              this.close()
            })
          }
        } else {
          return
        }
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

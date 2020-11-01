<!--
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-22 17:59:36
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-09-08 08:51:56
 -->
<template>
  <el-dialog
    :visible="proVisible"
    width="40%"
    :title="title"
    :before-close="close"
    :close-on-click-modal = "false"
    v-if="proVisible"
  >
    <el-form
      :model="proForm"
      :rules="proRules"
      ref="proForm"
      label-width="100px"
      label-position="left"
    >
      <el-form-item label="新增方式" v-if="$props.type == 'add'">
        <el-radio-group v-model="proForm.addMethod">
          <el-radio label="localImport">本地导入</el-radio>
          <el-radio label="createNew">创建新服务</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item
        label="选择模板"
        v-if="proForm.addMethod == 'createNew' || proForm.templateUrl"
      >
        <el-row type="flex">
          <el-col :span="12">
            <el-input
              v-model="proForm.templateUrl"
              readonly
              placeholder="模板路径"
            ></el-input>
          </el-col>
          <el-col :span="3" :offset="1">
            <el-button type="primary" @click="selectTem" size="small"
              >选择模板</el-button
            >
          </el-col>
        </el-row>
      </el-form-item>
      <el-row :gutter="20">
        <el-col :span="12">
          <el-form-item label="服务名称" prop="projectName">
            <el-input
              v-model="proForm.projectName"
              placeholder="请输入服务名称"
            ></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="文件名称" prop="fileName">
            <el-input
              v-model="proForm.fileName"
              placeholder="请输入文件名称"
            ></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row :gutter="20">
        <el-col :span="12">
          <el-form-item label="服务类型" prop="type">
            <el-select v-model="proForm.type" style='width:100%;'>
              <el-option
                v-for="item in typeList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="服务路径" prop="pathUrl">
            <el-input
              type="text"
              v-model="proForm.pathUrl"
              placeholder="请输入服务所在父目录路径"
            ></el-input>
          </el-form-item>
        </el-col>
      </el-row>
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
      <el-form-item label="Git路径" prop="gitUrl">
        <el-input
          type="text"
          v-model="proForm.gitUrl"
          placeholder="请输入Git路径"
        ></el-input>
      </el-form-item>
      <el-form-item label="关键字" prop="keyword">
        <el-input
          type="text"
          v-model="proForm.keyword"
          placeholder="请输入关键字"
        ></el-input>
      </el-form-item>
      <el-form-item label="服务描述">
        <el-input
          type="textarea"
          v-model="proForm.dec"
          :rows="2"
          placeholder="服务描述"
        ></el-input>
      </el-form-item>
      <el-row type="flex" justify="end">
        <el-form-item>
          <el-button type="primary" @click="confirm">确认</el-button>
          <el-button type="info" @click="close">取消</el-button>
        </el-form-item>
      </el-row>
    </el-form>
    <!--二级模态框-->
    <selectTem ref="selectTem" v-model="proForm.templateUrl"></selectTem>
  </el-dialog>
</template>

<script>
import {
  getServiceType,
  addService,
  updateService
} from '@/api/index/projectManage.js'
// import selectTem from '@/components/selectTem/selectTem.vue'
export default {
  name: 'proDialog',
  // components: {
  //   selectTem
  // },
  props: ['itemObj', 'type'],
  data() {
    return {
      proVisible: false,
      proForm: {
        addMethod: 'localImport',
        projectName: '',
        type: '',
        pathUrl: '',
        gitUrl: '',
        keyword: '',
        dec: '',
        templateUrl: '',
        decImg:'',
        fileName:''
      },
      proRules: {
        projectName: [
          { required: true, message: '请输入服务名称', trigger: 'blur' }
        ],
        fileName: [
          { required: true, message: '请输入文件名称', trigger: 'blur' }
        ],
        type: [
          { required: true, message: '请输入服务类型', trigger: 'change' }
        ],
        pathUrl: [
          { required: true, message: '请输入服务路径', trigger: 'blur' }
        ],
        gitUrl: [{ required: true, message: '请输入Git路径', trigger: 'blur' }],
        keyword: [{ required: true, message: '请输入关键字', trigger: 'blur' }]
      },
      typeList: []
    }
  },
  methods: {
    getFile(response) {
      this.proForm.decImg = response.resultEntity
    },
    show() {
      this.title = this.$props.type == 'modify' ? '修改服务' : '新增服务'
      if (this.$props.type == 'modify') {
        this.proForm = this.$props.itemObj
      } else {
        this.proForm = {
          addMethod: 'localImport',
          projectName: '',
          type: '',
          pathUrl: '',
          gitUrl: '',
          keyword: '',
          dec: '',
          templateUrl: ''
        }
      }
      this.proVisible = true
      this.queryProTypeList()
    },
    close() {
      this.proVisible = false
      this.$refs.proForm.resetFields()
    },
    queryProTypeList() {
      getServiceType({}).then(res => {
        // console.log(res)
        this.typeList = res || []
      })
    },
    selectTem() {
      this.$refs.selectTem.show()
    },
    /**
     * @name: confirm
     * @description: 弹窗确认
     * @param {type}: 默认参数
     * @return {type}: 默认类型
     */
    confirm() {
      this.$refs.proForm.validate(valid => {
        if (valid) {
          if (this.$props.type == 'add') {
            addService(this.proForm).then(() => {
              this.$message({
                type: 'success',
                message: '新增成功！'
              })
              if(this.proForm.addMethod ==='createNew'){
                this.$confirm('如果本地存在相同文件夹，本地文件将被删除请谨慎操作').then(() => {
                  this.$router.push({
                    path: '/project/projectInit',
                    query: this.proForm
                  })
                  this.close()
              })
              .catch(() => {})
              }else{
                this.$emit('getList',this.proForm.type)
                this.close()
              }
            })
          } else {
            updateProject(this.proForm).then(() => {
              this.$message({
                type: 'success',
                message: '修改成功！'
              })
              this.$emit('getList')
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

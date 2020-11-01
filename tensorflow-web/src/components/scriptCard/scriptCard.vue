<!--
 * @Description: 描述
 * @Author: pym
 * @Github: https://github.com/fodelf
 * @Date: 2020-04-10 21:26:24
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-05-16 11:27:12
 -->
<template>
  <div class="scriptCard">
    <p class="cardTit">{{ itemObj.scriptName }}</p>
    <el-input
      type="textarea"
      v-model="itemObj.scriptContent"
      :rows="7"
      resize="none"
    ></el-input>
    <div class="btn_row">
      <div class="col_box">
        <el-button type="primary" size="small" @click="modify(itemObj)"
          >修改</el-button
        >
        <el-button
          v-if ='itemObj.scriptId >4'
          type="danger"
          size="small"
          @click="deleteAtion(itemObj.scriptId)"
          >删除</el-button
        >
      </div>
      <div class="col_box">
        <el-button type="primary" size="small" @click="action"
          v-if ='itemObj.scriptId >4'
          >立即执行</el-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import { actionScript, deleteScript } from '@/api/scriptApi.js'
export default {
  name: 'scriptCard',
  props: {
    itemObj: {
      type: Object,
      default: function() {
        return {
          scriptContent: '',
          scriptName: ''
        }
      }
    }
  },
  data() {
    return {}
  },
  methods: {
    action() {
      actionScript({
        scriptContent: this.itemObj.scriptContent
      })
        .then(() => {
          this.$message({
            type: 'success',
            message: '脚本已经启动'
          })
        })
        .catch(() => {
          this.$message({
            type: 'warning',
            message: '脚本报错了！'
          })
        })
    },
    deleteAtion(scriptId) {
      this.$confirm('确认删除此脚本？')
        .then(() => {
          deleteScript({ scriptId: scriptId }).then(() => {
            this.$emit('getList')
          })
        })
        .catch(() => {})
    },
    modify(itemObj) {
      this.$emit('modify', itemObj)
    }
  }
}
</script>

<style lang="less" scoped>
.scriptCard {
  width: 100%;
  height: 100%;
  // padding-bottom: 10px;
  box-sizing: border-box;
  border-radius: 5px;
  background: #353c48;
  box-shadow: 0 0 4px #353c48;
  .cardTit {
    height: 40px;
    line-height: 40px;
    width: 100%;
    background: #303641;
    padding: 0 15px;
    box-sizing: border-box;
    color: #ced4da;
    font-size: 14px;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
  }
  /deep/.el-textarea__inner {
    background: #272c36;
    outline: none;
    border: none;
    color: #ced4da;
    border-radius: 0;
  }
  .btn_row {
    width: 100%;
    padding: 10px 15px;
    box-sizing: border-box;
    display: flex;
    justify-content: space-between;
  }
}
</style>

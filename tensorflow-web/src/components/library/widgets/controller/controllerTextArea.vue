<!--
 * @Description:
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2019-05-14 23:33:19
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-05-09 14:57:49
 -->

<template>
  <el-form-item :label="mes.controllerName">
    <el-input v-model="value"
              @input="changeValue"
              type="textarea"></el-input>
  </el-form-item>
</template>
<script>
import controller from '@/components/library/widgets/controller/controller.vue'
export default {
  name: 'controllerSelect',
  extends: controller,
  data () {
    return {

    }
  },
  methods: {

  }

}
</script>

<style lang="less">
</style>

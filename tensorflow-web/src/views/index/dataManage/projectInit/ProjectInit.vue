<!--
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-04-01 16:11:07
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-04-01 16:27:03
 -->
<template>
  <div class="projectInit">
     <Terminal :type ='type' :actionData = 'actionData'/>
  </div>
</template>

<script>
import projectInit from './projectInit.js'
export default {
  ...projectInit
}
</script>

<style rel="stylesheet/less"  lang="less" scoped>
@import "./projectInit.less";
</style>

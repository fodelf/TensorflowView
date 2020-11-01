<!--
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-08-11 14:26:54
 * @LastEditors: pym
 * @LastEditTime: 2020-09-06 20:57:59
-->
<template>
  <div class='service-content clearfix'>
    <systemCard v-for="(item,index) in serviceList" :key='index' :item="item" class='systemCard' @showDialog='showEdit'>
    </systemCard>
    <serviceEdit ref='editService' @confirmService='confirm'></serviceEdit>
  </div>
</template>

<script>
import serviceSet from './serviceSet.js'
export default {
  ...serviceSet
}
</script>

<style lang='less' scoped>
@import './serviceSet.less';
</style>
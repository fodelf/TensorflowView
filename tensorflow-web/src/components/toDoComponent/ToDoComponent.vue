<!--
 * @Description: 待开发
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-04-12 16:43:48
 * @LastEditors: pym
 * @LastEditTime: 2020-04-12 22:44:30
 -->
<template>
  <div class='todo'>
    <i class='iconfont icon-meiyoudingdan'></i>
    <span>尚未开发，敬请期待</span>
  </div>
</template>

<style lang="less" scoped>
.todo {
  width: 100%;
  height: calc(100% - 56px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #fff;
  .iconfont {
    font-size: 150px;
    display: block;
  }
  span {
    display: block;
    font-size: 25px;
  }
}
</style>

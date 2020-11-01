<!--
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-18 22:29:01
 * @LastEditors: pym
 * @LastEditTime: 2020-04-05 10:42:58
 -->
<template>
  <div class="card">
    <div class="cardCon">
      <div class="leftCon">
        <i class="conPng iconfont"
           :class="card.icon"></i>
        <p class="conDesc">{{card.label}}</p>
      </div>
      <div class="rightCon"
           :style="{color:card.proColor}">
        {{card.num}}
      </div>
    </div>
    <div class="progress">
      <span class="progressContent"
            :style="{background:card.proColor,width:card.percent}"></span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'cardNum',
  props: {
    card: {
      type: Object,
      default: () => { }
    }
  },
  data () {
    return {}
  },

  methods: {},
  created () { },
  mounted () { }
}
</script>
<style lang="less" scoped>
.card {
  width: 100%;
  height: 120px;
  padding: 15px;
  background-color: #353c48;
  color: #ced4da;
  box-sizing: border-box;
  display: flex;
  flex-wrap: wrap;
  .cardCon {
    height: 80px;
    width: 100%;
    display: flex;
    justify-content: space-between;
    .leftCon {
      font-size: 14px;
      .conPng {
        display: block;
        font-size: 26px;
        margin-bottom: 10px;
      }
    }
    .rightCon {
      font-size: 30px;
      // line-height:80px;
      // text-align: right;
    }
  }

  .progress {
    width: 100%;
    height: 6px;
    position: relative;
    background-color: #303641;
    border-radius: 5px;
    .progressContent {
      position: absolute;
      left: 0;
      top: 0;
      height: 6px;
      display: block;
      border-radius: 5px;
    }
  }
}
</style>

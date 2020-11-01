<!--
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-21 20:50:26
 * @LastEditors: pym
 * @LastEditTime: 2020-09-06 19:33:25
 -->
<template>
  <el-carousel
    height="100%"
    :interval="3000"
    indicator-position="none"
    arrow="nerver"
  >
    <el-carousel-item v-for="item in carouselList" :key="item">
      <p class="desc">{{item}}</p>
      <div class="actor">
        <i class="user-bg"></i>
        <div class="user">
          <p class="user-name">wwz</p>
          <p>负责人</p>
        </div>
      </div>
    </el-carousel-item>
  </el-carousel>
</template>

<script>
export default {
  name: 'carousel',
  props: {
    carouselList: {
      type: Array,
      default: function() {
        return []
      }
    }
  },
  data() {
    return {}
  }
}
</script>

<style lang="less" scoped>
.el-carousel {
  height: 100%;
  width: 100%;
  padding: 25px;
  box-sizing: border-box;
  background: #fb9678;

  /deep/.el-carousel__container {
    color: #fff;
    height: 100%;
    .el-carousel__item {
      height: 100%;
      .desc {
        height: calc(100% - 50px);
      }
    }
    .actor {
      display: flex;
      height: 50px;
      .user-bg {
        display: inline-block;
        background: url(../../assets/img/headerBg.svg) no-repeat center;
        background-size: 100% 100%;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        margin-right: 10px;
        // float:left;
      }
      .user {
        .user-name {
          font-size: 24px;

          // float:left;
        }
      }
    }
  }
}
// .el-carousel--horizontal {
//   height:100%;
//   width:100%;
// }
</style>

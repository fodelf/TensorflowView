<!--
 * @Description: 头部tab组件
 * @Author: pym
 * @Github: https://github.com/fodelf
 * @Date: 2020-04-04 09:49:32
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-09-10 09:07:57
 -->
<template>
  <div class="tabBread">
    <span class="currentLoc">{{ currentTab }}</span>
    <el-breadcrumb
      class="breadcrumb-container"
      separator-class="el-icon-arrow-right"
    >
      <el-breadcrumb-item v-for="item in levelList" :key="item.path">{{
        item.meta.title
      }}</el-breadcrumb-item>
    </el-breadcrumb>
  </div>
</template>

<script>
export default {
  name: 'tabBread',
  data() {
    return {
      currentTab: '',
      levelList: []
    }
  },
  watch: {
    $route() {
      this.getBreadcrumb()
    }
  },
  created() {
    this.getBreadcrumb()
  },
  methods: {
    getBreadcrumb() {
      let matched = this.$route.matched.filter(item => item.name)
      // const first = matched[0]
      this.levelList = matched
      this.currentTab = this.levelList[this.levelList.length - 1].meta.title
      // 当前写死一个服务后面写出策略映射
      if(this.$route.query.type =='check'){
        this.currentTab ="查看服务"
        this.levelList[1].meta.title ="查看服务"
      }else if(this.$route.query.type =="add"){
        this.currentTab ="新增服务"
        this.levelList[1].meta.title ="新增服务"
      }else if (this.$route.query.type =="edit"){
        this.currentTab ="编辑服务"
        this.levelList[1].meta.title="编辑服务"
      }
    }
  }
}
</script>

<style lang="less" scoped>
.tabBread {
  width: 100%;
  height: 60px;
  padding: 15px 25px;
  background: #303641;
  box-sizing: border-box;
  display: flex;
  justify-content: space-between;
  align-items: center;
  .currentLoc {
    color: rgb(206, 212, 218);
  }
  /deep/.el-breadcrumb {
    .el-breadcrumb__item {
      .el-breadcrumb__inner {
        font-size: 12px;
        color: rgb(206, 212, 218);
      }
      .el-breadcrumb__separator {
        font-size: 12px;
      }
    }
    .el-breadcrumb__item:last-child {
      .el-breadcrumb__inner {
        color: #fb9678;
      }
    }
  }
}
</style>

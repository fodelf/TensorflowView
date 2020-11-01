<!--
 * @Description:
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2019-06-11 18:59:40
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-09-04 10:09:30
 -->
<template>
  <div id="contentMain"
       class="clearfix">
    <!-- <sideBar ref="sideBar"></sideBar> -->
    <sideMenu ref="sideBar"></sideMenu>
    <div class="mainContent">
      <!--头部组件-->
      <headerModule @changeCollapse="changeMenu"></headerModule>
      <!--面包屑组件-->
      <tabBread :currentTab="'服务管理'"></tabBread>
      <div class="main">
        <router-view />
        <!--底部组件-->
        <footerModule></footerModule>
      </div>

    </div>
  </div>
</template>

<script>
import sideMenu from '@/components/sideMenu/sideMenu.vue'
import tabBread from 'components/tabBread/tabBread'
import headerModule from '@/components/headerModule/headerModule.vue'
import footerModule from '@/components/footerModule/footerModule.vue'
export default {
  name: 'Main',
  components: {
    sideMenu,
    tabBread,
    headerModule,
    footerModule
  },
  data () {
    return {
      userName: '',
      activePath: '/',
      meslist: []
    }
  },
  mounted () { },
  methods: {
    /**
     * @name: handleSelect
     * @description: 路由跳转
     */
    handleSelect (key) {
      this.$router.push({
        path: key
      })
    },
    changeMenu () {
      this.$refs.sideBar.isCollapse = !this.$refs.sideBar.isCollapse
    }
  }
}
</script>

<style lang="less" scoped>
@import "./layout.less";
</style>

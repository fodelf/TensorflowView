<!--
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-08-11 10:08:07
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-09-09 17:56:30
-->
<template>
  <div class="sideMenu" :class="isCollapse?'min-sideBar':'sideBar'">
    <p class="bigTit">
      <i class="titBg"></i>
      <span :class="isCollapse ? 'move_right' : ''" v-show='!isCollapse'>Easy<em>AI</em></span>
    </p>
    <!-- <el-scrollbar wrap-class="scrollbar-wrapper"
                  class="side"> -->
      <el-menu :default-active="defaultActive"
                router
                class="nav"
                background-color="#353c48"
                :collapse="isCollapse">
        <treeMenuModule v-for="(item,index) in menuTree"
                        :key="index"
                        :isCollapse='isCollapse'
                        :menuItem="item" @changeName='updateName'></treeMenuModule>
      </el-menu>
    <!-- </el-scrollbar> -->
  </div>
</template>

<script>
import menuConfig from './menuConfig.js'
import treeMenuModule from './children/treeMenu'
export default {
  name:'sideMenu',
  components:{
    treeMenuModule
  },
  computed: {
    defaultActive() {
      // 暂时写死的
      if(this.$route.path.indexOf('/data') >=0){
        return "/data/dataManage";
      }else if(this.$route.path.indexOf('/model') >=0){
        return "/model/modelManage";
      }else{
        return "/home"
      }
    }
  },
  data() {
    return {
      isCollapse: false,
      menuTree:null,
      activeName:'home'
    }
  },
  methods:{
    updateName(name) {
      console.log(name)
      this.activeName = name
    }
  },
  created() {
    this.menuTree = menuConfig
  }
}
</script>

<style lang='less' scoped>
.sideMenu {
  height: 100%;
  background-color: #353c48;

  .bigTit {
    height: 65px;
    line-height: 65px;
    width: 100%;
    color: #fff;
    font-size: 16px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 10px;

    .titBg {
      display: inline-block;
      background: url('../../assets/img/work.svg') no-repeat center;
      background-size: 100% 100%;
      width: 35px;
      height: 35px;
    }

    span {
      margin-left: 8px;
      font-size: 20px;
      font-weight: bold;

      em {
        color: #fb9678;
        font-weight: bold;
      }
    }
  }

  .iconfont {
    font-size: 20px;
    margin-right: 8px;
  }
}
/deep/.el-menu {
  background-color: #353c48;
  border-right: none;
   
}
/deep/.el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 180px;
    min-height: 400px;
}
.sideBar {
  width:180px;
  flex: 0 0 180px;
  transition: all 0.3s;
  position: relative;
  // width: 250px;
 
}
.min-sideBar {
  width: 64px;
  flex: 0 0 64px;
  transition: all 0.3s;
  position: relative;
}
 
</style>
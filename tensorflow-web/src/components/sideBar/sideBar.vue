<!--
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-21 10:24:56
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-09-04 10:03:53
 -->
<template>
  <div class="sideBar" :class="isCollapse ? 'min-side' : ''">
    <p class="bigTit">
      <i class="titBg"></i
      ><span :class="isCollapse ? 'move_right' : ''">Easy<em>AI</em></span>
    </p>
    <el-menu
      :default-active="$route.path"
      router
      class="nav"
      :collapse="isCollapse"
    >
      <el-menu-item
        v-for="(menuItem, index) in menuTree"
        :key="index"
        :index="menuItem.path"
        @click="handleJumpToPath(menuItem)"
      >
        <i class="iconfont" :class="menuItem.icon"></i>
        <span slot="title">{{ menuItem.label }}</span>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'sideBar',
  data() {
    return {
      isCollapse: false,
      menuTree: [
        { name: 'home', path: '/home', icon: 'icon-shouye', label: '首页' },
        {
          name: 'projectManage',
          path: '/project/projectManage',
          icon: 'icon-xiangmu',
          label: '数据管理'
        },
        {
          name: 'systemManage',
          path: '/system/userManage',
          icon: 'icon-shezhi',
          label: '系统设置',
          children:[
            {
              name: 'serviceSet',
              path: '/system/serviceSet',
              label: '服务设置'
            }
          ]
        }
      ]
    }
  },
  methods: {
    handleJumpToPath(item) {
      console.log(item)
      this.$router.push({
        name: item.name
      })
    }
  }
}
</script>

<style lang="less" scoped>
.sideBar {
  transition: all 0.3s;
  position: relative;
  // width: 250px;
  height: 100%;
  flex: 0 0 180px;
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
  .el-menu-item {
    height: 40px;
    line-height: 40px;
    color: #8d97ad;
    border-left: 3px #353c48 solid;
    .iconfont {
      font-size: 16px;
      margin-right: 8px;
    }
  }
  .el-menu-item.is-active {
    background: none;
    color: #fb9678;
    border-left: 3px #fb9678 solid;
  }
  .el-menu-item:hover {
    color: #fb9678;
    background: none;
    .iconfont {
      color: #fb9678;
    }
  }
}
.move_right {
  -webkit-animation-name: move_right;
  animation-name: move_right;
  -webkit-animation-duration: 1s;
  animation-duration: 1s;
  -webkit-animation-iteration-count: 1;
  animation-iteration-count: 1;
  -webkit-animation-fill-mode: forwards;
  animation-fill-mode: forwards;
}
.move_left {
  -webkit-animation-name: move_left;
  animation-name: move_left;
  -webkit-animation-duration: 1s;
  animation-duration: 1s;
  -webkit-animation-iteration-count: 1;
  animation-iteration-count: 1;
  -webkit-animation-fill-mode: forwards;
  animation-fill-mode: forwards;
}
@keyframes move_right {
  from {
    // opacity: 0;
    display: none;
  }
  to {
    display: block;
    // opacity: 1;
    // -webkit-transform: translateX(-120px);
    // transform: translateX(-120px);
  }
}
@keyframes move_left {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
    -webkit-transform: translateX(120px);
    transform: translateX(120px);
  }
}
.min-side {
  width: 64px;
  flex: 0 0 64px;

  .bigTit {
    span {
      display: none;
      // overflow: hidden;
      // opacity: 0;
      // width: 0 !important;
      // // animation:fadeout 1s ease-out;
    }
  }
  // @keyframes fadeout {
  //   0% {
  //     display: block;
  //   }
  //   100% {
  //     display: none;
  //   }
  // }

  /deep/.el-menu {
    .el-menu-item {
      span {
        display: none;
      }
    }
  }
}
</style>

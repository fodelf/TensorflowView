<!--
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-08-11 10:08:56
 * @LastEditors: pym
 * @LastEditTime: 2020-08-18 15:04:45
-->
<template>
    <el-menu-item :index="menuItem.path"
                  v-if="!menuItem.children"
                  class='menuItem'
                  @click="handleJumpToPath(menuItem)">
        <i class="iconfont"
          :class="menuItem.icon"></i>
        <span slot='title'>{{ menuItem.label }}</span>
    </el-menu-item>

    <el-submenu v-else
                :index="menuItem.path" class='subMenu'>
      <template slot="title">
        <i class="iconfont"
           :class="menuItem.icon"></i>
        <span>{{ menuItem.label }}</span>
      </template>
      <treeMenuModule v-for="(child,index) in menuItem.children"
                      :key="index"
                      :menuItem="child"
                       @changeName='updateName'></treeMenuModule>
    </el-submenu>
</template>

<script>
export default {
  name:'treeMenuModule',
  props:{
    menuItem: {
      type: Object,
      default:() => {
        return {}
      }
    },
    isCollapse:{
      type:Boolean,
      default: () => {
        return false
      }
    }
  },
  data() {
    return {
      
    }
  },
  methods: {
    handleJumpToPath(item) {
      this.$router.push({
        name: item.name
      })
      this.$emit('changeName',item.name)
    },
    updateName(name) {
      this.$emit('changeName',name)
    }
  }
}
</script>

<style lang='less' scoped>
// @import "./treeMenuModule.scss";
.menuItem {
  height: 40px;
  line-height: 40px;
  color: #8d97ad;
  border-left: 3px transparent solid;
  .iconfont {
    font-size: 16px;
    margin-right: 8px;
  }
}
.menuItem.is-active {
  background: none;
  color: #fb9678;
  border-left: 3px #fb9678 solid;
}
.menuItem:hover {
  color: #fb9678;
  background: #303641;
  .iconfont {
    color: #fb9678;
  }
}
.subMenu {
   /deep/.el-submenu__title {
    height: 40px;
    line-height: 40px;
    color: #8d97ad;
    border-left: 3px transparent solid;
    .iconfont {
      font-size: 16px;
      margin-right: 8px;
    }
  }
  /deep/.el-submenu__title:hover {
    background:#303641;
  }
  /deep/.el-menu-item {
    height: 40px;
    line-height: 40px;
    width:100%;
    min-width:180px;
  }
}
 
/deep/.el-menu-item.is-active {
  background: none;
  color: #fb9678;
  border-left: 3px #fb9678 solid;
}
/deep/.el-menu-item:hover {
  color: #fb9678;
  background: #303641;
  .iconfont {
    color: #fb9678;
  }
} 
</style>

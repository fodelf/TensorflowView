<!--
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-21 21:17:29
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-09-09 17:42:06
 -->
<template>
  <div class="menuList">
    <p class="menuTit itemNum clearfix" :class="currentIndex == 'all'? 'active' : ''" @click="handleClickMenu({type:'all'})">
      <span >{{ menuObj.title }}</span>
      <i>{{ menuObj.total }}</i>
    </p>
    <ul class="menuCon">
      <li
        v-for="(item, index) in menuObj.menuList"
        :key="index"
        class="menuItem itemNum clearfix"
        :class="currentIndex == item.type ? 'active' : ''"
        @click="handleClickMenu(item, index)"
      >
        <span>{{ item.label }}</span>
        <i>{{ item.count }}</i>
      </li>
      <!-- <li>
        <el-button type="primary" @click="addMenu" icon="el-icon-plus"
          >新增</el-button
        >
      </li> -->
    </ul>
  </div>
</template>

<script>
export default {
  name: 'menuList',
  props: {
    menuObj: {
      type: Object,
      default: function () {
        return {
          title: '',
          total: 0,
          menuList: [],
          active:'all'
        }
      },
    },
  },
  data() {
    return {
      currentIndex: 'all',
    }
  },
  watch:{
     menuObj: {
      handler(newobj) {
         this.currentIndex = newobj.active
      },
      deep: true,
    }
  },
  methods: {
    addMenu() {},
    handleClickMenu(item) {
      this.currentIndex = item.type
      console.log(item)
      this.$emit('clickMenu', item)
    },
  },
}
</script>

<style lang="less" scoped>
.menuList {
  width: 100%;
  color: #ced4da;
  .menuTit {
    width: 100%;
    height: 35px;
    line-height: 35px;
    font-size: 14px;
    font-weight: bold;
    padding-bottom: 10px;
    border-bottom: 1px #4f5467 solid;
    span {
      float: left;
    }
    i {
      float: right;
    }
  }
  .menuCon {
    width: 100%;
    .menuItem {
      height: 25px;
      line-height: 25px;
      padding: 8px 0;
      font-weight: normal;
      span {
        float: left;
      }
      i {
        float: right;
      }
    }
    /deep/.el-button {
      width: 100%;
    }
  }
  .itemNum:hover {
    color: #fb9678;
  }
  .active {
    color: #fb9678;
  }
}
</style>

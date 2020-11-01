<!--
 * @Description: 描述
 * @Author: pym
 * @Github: https://github.com/fodelf
 * @Date: 2020-04-06 15:12:20
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-05-08 20:33:01
 -->
<template>
  <div class="message">
    <p class="msgTit">{{ msgObj.msgTit }}</p>
    <div class="msg">
      <el-scrollbar>
        <ul class="msgList">
          <li v-for="(item, index) in msgObj.msgList" :key="index">
            <div class="user-img">
              <i class="bgIcon"></i>
              <span></span>
            </div>
            <div class="msgContent">
              <h5 class="user-name">Admin</h5>
              <p class="msg-desc">{{ item.active }}</p>
              <span class="msg-date">{{ item.createTime }}</span>
            </div>
          </li>
        </ul>
      </el-scrollbar>
    </div>
  </div>
</template>

<script>
export default {
  name: 'actionModule',
  props: {
    msgObj: {
      type: Object,
      default: function(){
        return{ 
          msgTit: '',
          msgList: [],
        } 
      },
    },
  },
  data() {
    return {}
  },
  methods: {},
}
</script>

<style lang="less" scoped>
.message {
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  padding: 10px 15px;
  .msgTit {
    color: #ced4da;
    height: 40px;
    line-height: 40px;
    margin-bottom: 10px;
  }
  .msg {
    height: calc(100% - 40px);
    width: 100%;
    overflow: hidden;
  }
  /deep/.el-scrollbar {
    height: 100%;
    .el-scrollbar__wrap {
      overflow: scroll;
      overflow-x: auto;
    }
    .el-scrollbar__bar {
      .el-scrollbar__thumb {
        background-color: rgba(0, 0, 0, 0.2);
      }
    }
  }
  .msgList {
    width: 100%;
    li {
      border-bottom: 1px solid #4f5467;
      padding: 9px 15px;
      box-sizing: border-box;
      display: flex;
      width: 100%;
      align-items: flex-start;
      .bgIcon {
        display: inline-block;
        background: url(../../assets/img/headerBg.svg) no-repeat center;
        width: 45px;
        height: 45px;
        background-size: 100% 100%;
        border-radius: 50%;
        margin-right: 10px;
      }
      .msgContent {
        display: inline-block;
        width: 70%;
        color: #ced4da;
        .msg-desc {
          font-size: 12px;
          width: 100%;
          overflow: hidden;
          white-space: nowrap;
          text-overflow: ellipsis;
        }
        .msg-date {
          font-size: 12px;
        }
      }
    }
    li:last-child {
      border-bottom: none;
    }
    li:hover {
      background: #272c36;
    }
  }
}
</style>

<!--
 * @Description: 描述
 * @Author: pym
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-30 23:25:05
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-10-14 16:50:11
 -->
<template>
  <div class="cardTemp">
    <el-row :gutter="20">
      <el-col :span="8" v-for="item in compCardList" :key="item.projectId">
        <div class="templateCard">
          <img class="cardImg" :src="item.decImg?item.decImg:bg" />
          <div class="cardBody">
            <h4 class="cardTit">{{ item.projectName }}</h4>
            <p class="cardText">{{ item.dec }}</p>
            <el-form ref="form" :model="form" label-width="40px" style="margin-top: 10px">
            <el-form-item label="操作" style="margin-bottom:10px">
              <el-button type="primary" size="small" @click="update(item)"
                >编辑</el-button
              >
              <el-button
                type="danger"
                size="small"
                @click="deleteAtion(item)"
                >删除</el-button
              >
            </el-form-item>
            <el-form-item label="Git">
              <el-row :gutter="10" type='flex'>
                <el-col :span="10">
                  <el-select v-model="item.action" placeholder="请选择类型">
                    <el-option :label="child.label" :value="child.value"
                    v-for="(child,childIndex) in item.actions"
                    :key="childIndex"></el-option>
                    <!-- <el-option label="新建分支" value="1"></el-option>
                    <el-option label="修复bug" value="2"></el-option> -->
                  </el-select>
                </el-col>
                <el-col :span="14" style='display:flex'>
                  <el-input v-model="item.param"></el-input>
                  <el-button
                  type="primary"
                  size="small"
                  @click="action(item)"
                  style="margin-left:10px"
                  >执行</el-button>
                </el-col>
              </el-row>
            </el-form-item>
            </el-form>
          </div>
        </div>
      </el-col>
    </el-row>
    <!-- <div class="pageBox clearfix" v-if="compCardList.length !== 0">
      <el-pagination
        background
        @current-change="handleCurrentChange"
        :current-page="tablePag.pageNo"
        :page-size="tablePag.pageSize"
        layout="total, prev, pager, next, jumper"
        :total="tablePag.totalRecord"
      >
      </el-pagination>
    </div> -->
  </div>
</template>

<script>
// import { deleteComponent } from '@/api/componentApi.js'
// import tempDialog from '@/components/tempDialog/tempDialog.vue'
export default {
  name: 'templateCard',
  props: {
    tablePag: {
      type: Object,
      default: function() {
        return {
          pageNo: 1,
          pageSize: 15,
          totalRecord: 0
        }
      }
    },
    compCardList: {
      type: Array,
      default: function() {
        return []
      }
    }
  },
  data() {
    return {
      form:{
        region:'1',
        param:''
      },
      itemObj: null,
      actionType: 'modify',
      bg:require("../../../../assets/img/edit/bg.jpg")
    }
  },
  methods: {
    action(item) {
      if(item.param){
        item.param = item.param.trim()
        this.$emit('action',Object.assign(item))
      }else{
      this.$message({
        type:'warning',
        mes:'请填写参数！'
      })
      }
    },
    deleteAtion(item) {
      this.$emit('delete', item)
    },
    handleCurrentChange(val) {
      this.$emit('changePageNo', val)
    },
    getTempList() {
      this.$emit('getTempList')
    },
    update(item) {
      this.$emit('edit', item)
    }
  }
}
</script>

<style lang="less" scoped>
/deep/.el-form-item__label{
  color: white;
}
/deep/ .el-row {
  flex-wrap: wrap;
  display: flex;
}
/deep/.el-form-item{
  margin-bottom:0px
}
/deep/.el-input__inner {
    background-color: #353c48;
    border: none;
    color: #ced4da;
}
.templateCard {
  width: 100%;
  // height: 150px;
  background: #3c4452;
  margin-bottom: 20px;
  .cardBody {
    padding: 20px;
  }
  .cardImg {
    width: 100%;
    height: 180px;
  }
  .cardTit {
    font-weight: 500;
    color: #ced4da;
    margin-bottom: 10px;
  }
  .cardText {
    color: #ced4da;
    margin-bottom: 10px;
    height: 63px;
  }
}
.pageBox {
  width: 100%;
  margin-top: 5px;
  /deep/.el-pagination {
    float: right;
    .btn-prev {
      background: #303641;
    }
    .btn-next {
      background: #303641;
    }
    .el-input__inner {
      background: #303641;
    }
  }
}
</style>

<!--
 * @Description: 描述
 * @Author: pym
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-30 23:25:05
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-05-15 17:01:38
 -->
<template>
  <div class="cardTemp">
    <el-row :gutter="20">
      <el-col :span="8" v-for="(item, index) in tempCardList" :key="index">
        <div class="templateCard">
          <img class="cardImg" :src="item.decImg?item.decImg:bg" />
          <div class="cardBody">
            <h4 class="cardTit">{{ item.templateName }}</h4>
            <p class="cardText">{{ item.dec }}</p>
            <el-row>
              <el-button type="primary" size="small" @click="update(item)"
                >编辑</el-button
              >
              <el-button
                type="danger"
                size="small"
                @click="deleteAtion(item.templateId)"
                >删除</el-button
              >
            </el-row>
          </div>
        </div>
      </el-col>
    </el-row>
    <div class="pageBox clearfix" v-if="tempCardList.length !== 0">
      <el-pagination
        background
        @current-change="handleCurrentChange"
        :current-page="tablePag.pageNo"
        :page-size="tablePag.pageSize"
        layout="total, prev, pager, next, jumper"
        :total="tablePag.totalRecord"
      >
      </el-pagination>
    </div>
    <!--弹窗组件-->
    <tempDialog
      ref="tempDialog"
      :itemObj="itemObj"
      :actionType="actionType"
      @getTempList="getTempList"
    ></tempDialog>
  </div>
</template>

<script>
import { deleteTemp } from '@/api/templateApi.js'
import tempDialog from '@/components/tempDialog/tempDialog.vue'
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
    tempCardList: {
      type: Array,
      default: function() {
        return []
      }
    }
  },
  components: {
    tempDialog
  },
  data() {
    return {
      itemObj: null,
      actionType: 'modify',
      bg:require("../../assets/img/edit/bg.jpg")
    }
  },
  methods: {
    deleteAtion(templateId) {
      this.$confirm('确认删除此模板？')
        .then(() => {
          deleteTemp({ templateId: templateId }).then(() => {
            this.$message({
              type: 'success',
              message: '模板已删除'
            })
            this.$emit('getTempList')
          })
        })
        .catch(() => {})
    },
    handleCurrentChange(val) {
      this.$emit('changePageNo', val)
    },
    getTempList() {
      this.$emit('getTempList')
    },
    update(item) {
      this.itemObj = item
      this.$nextTick(() => {
        this.$refs.tempDialog.show()
      })
    }
  }
}
</script>

<style lang="less" scoped>
/deep/ .el-row {
  flex-wrap: wrap;
  display: flex;
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

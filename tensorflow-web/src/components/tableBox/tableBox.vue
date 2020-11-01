<!--
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-21 21:41:04
 * @LastEditors: pym
 * @LastEditTime: 2020-09-06 20:10:04
 -->
<template>
  <div class="tableBox" ref="tableBox">
    <el-table :data="dataList" :height="tableHeight" border ref="mainTable">
      <el-table-column
        v-for="item in headerList"
        :key="item.code"
        :label="item.name"
      >
        <template slot-scope="scope">
          {{ scope.row[item.code] ? scope.row[item.code] : '--' }}
        </template>
      </el-table-column>
      <el-table-column label="操作" width="250">
        <template slot-scope="scope">
           <el-button type="primary" @click="handleCheck(scope.row)"
            >查看</el-button
          >
          <el-button type="primary" @click="handleEdit(scope.row)"
            >编辑</el-button
          >
          <!-- <el-button v-if="actionType == 'project'" type="primary" @click="handleAction(scope.row)"
            >新建分支</el-button
          > -->
          <el-button type="danger" @click="handleDelete(scope.row)"
            >删除</el-button
          >
        </template>
      </el-table-column>
    </el-table>
    <!-- <div class="pageBox clearfix">
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
export default {
  name: 'tableBox',
  props: {
    actionType: {
      type: String,
      default: function() {
        return ''
      }
    },
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
    headerList: {
      type: Array,
      default: function() {
        return []
      }
    },
    dataList: {
      props: Array,
      default: []
    }
  },
  data() {
    return {
      tableHeight: 300
    }
  },
  methods: {
    handleCurrentChange(val) {
      this.$emit('changePageNo', val)
    },
    handleCheck(row){
      this.$emit('checkRow', row)
    },
    handleEdit(row) {
      this.$emit('editRow', row)
    },
    handleDelete(index) {
      this.$emit('deleteRow', index)
    },
    handleAction(row) {
      this.$emit('newBranch', row)
    },
    setTableHeight() {
      this.$nextTick(() => {
        this.tableHeight = this.$refs.tableBox.offsetHeight
      })
    },
    doLay() {
      this.$refs.mainTable.doLayout()
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.setTableHeight()
    })
  }
}
</script>

<style lang="less" scoped>
@border-color: #4f5467;
@bg-color: #353c48;

.tableBox {
  height: 100%;
  /deep/.el-table {
    background: @bg-color;
    border-color: @border-color;
    tr {
      color: #ced4da;

      th {
        background: @bg-color;
        border-color: @border-color;
      }
      td {
        background: @bg-color;
        border-color: @border-color;
        /deep/.el-button {
          height: 25px;
          line-height: 25px;
          padding: 0 10px;
        }
      }
    }
  }
  .el-table::before {
    background: @border-color;
  }
  .el-table::after {
    background: @border-color;
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
}
</style>

<!--
 * @Description: 描述
 * @Author: pym
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-29 22:26:36
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-09-08 08:51:19
 -->
<template> 
  <el-dialog :visible='selectTemVisible' append-to-body title='选择模板' :before-close="close" width='50%' v-if='selectTemVisible'>
    <el-row type="flex" class="row-bg" justify="end">
      <el-form :model='temForm' :inline='true'>
        <el-form-item>
          <el-select v-model='temForm.type'>
            <el-option v-for='item in typeList' :value='item.value' :label='item.label' :key='item.value'></el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-input v-model='temForm.keyword' placeholder='请输入关键字'>
          </el-input>
        </el-form-item>
      </el-form>
    </el-row>
    <el-tabs>
      <el-tab-pane v-for='(item,index) in labelList' :label='item' :key='index'>
        <el-table :data='dataList' height='calc(45vh)' border ref='dialogTable'>
          <el-table-column label="选择" width="55">
            <template slot-scope="scope">
                <el-radio  v-model="tableRadio" :label="scope.row"><i></i></el-radio>
            </template>
          </el-table-column>
          <el-table-column v-for='item in headerList' :key='item.code' :label='item.name'>
            <template slot-scope='scope'>
              {{scope.row[item.code]?scope.row[item.code]:'--'}}
            </template>
          </el-table-column>
        </el-table>
        <div class='pageBox clearfix'>
          <el-pagination
            background
            @current-change="handleCurrentChange"
            :current-page="tablePag.pageNo"
            layout="total, prev, pager, next, jumper"
            :total="tablePag.totalRecord">
          </el-pagination>
        </div>
      </el-tab-pane>
    </el-tabs>
    <el-row type="flex" class="buttons" justify="end">
      <el-button type='primary' @click='confirm'>确认</el-button>
      <el-button type='info' @click='close'>取消</el-button>
    </el-row>
  </el-dialog>
</template>

<script>
import { getTemList, getServiceType } from '@/api/index/projectManage.js'
export default {
  name:'selectTem',
  props:['value'],
  model: {
    prop:'value',
    event: "input"
  },
  data() {
    return {
      temForm:{
        type:'',
        keyword:''
      },
      labelList:['本地模板','全局模板'],
      headerList:[
        {name:'模板名称',code:'templateName'},
        {name:'模板类型',code:'type'},
        {name:'模板关键字',code:'keyword'},
        {name:'Git地址',code:'gitUrl'}
      ],
      dataList:[],
      tablePag:{
        pageNo:1,
        pageSize:10,
        totalRecord:0
      },
      typeList:[],
      selectTemVisible:false,
      tableRadio:{}
    }
  },
  methods:{
    /**
     * @name: show
     * @description: 显示弹窗
     * @param {type}: 默认参数
     * @return {type}: 默认类型
     */
    show(){
      this.selectTemVisible = true
      this.queryProTypeList()
      this.queryTemList()
    },
    /**
     * @name: close
     * @description: 关闭弹窗
     * @param {type}: 默认参数
     * @return {type}: 默认类型
     */
    close(){
      this.selectTemVisible = false
    },
    /**
     * @name: handleCurrentChange
     * @description: 分页事件
     * @param {type}: 默认参数
     * @return {type}: 默认类型
     */
    handleCurrentChange(val){
      this.tablePag.pageNo = val
      this.queryTemList()
    },
    /**
     * @name: queryTemList
     * @description: 请求模板列表
     * @param {type}: 默认参数
     * @return {type}: 默认类型
     */
    queryTemList() {
      let params = {
        type:this.temForm.type,
        pageNum:this.tablePag.pageNo,
        pageSize:this.tablePag.pageSize,
        keyword:this.temForm.keyword
      }
      getTemList(params).then(res=>{
        console.log(res)
        this.dataList = res.list
        this.tablePag.totalRecord = res.total
        this.$nextTick(()=>{
          this.$refs.dialogTable.doLayout()
        })
      })
    },
    /**
     * @name: queryProTypeList
     * @description: 请求服务类型列表
     * @param {type}: 默认参数
     * @return {type}: 默认类型
     */
    queryProTypeList(){
      getProjectType({}).then(res=>{
        console.log(res)
        this.typeList = res || []

      })
    },
    /**
     * @name: confirm
     * @description: 确认
     * @param {type}: 默认参数
     * @return {type}: 默认类型
     */
    confirm(){
      console.log(this.tableRadio)
      this.$emit('input',this.tableRadio.gitUrl)
      this.selectTemVisible = false
    }
  }
}
</script>

<style lang="less" scoped>
@border-color:#4F5467;
@bg-color:#353c48;
.buttons {
  margin-top:15px;
}
/deep/.el-tabs__nav-wrap::after {
  height:1px;
  background-color:#4F5467;
}
/deep/.el-tabs {
  .el-tabs__item {
    color:#ced4da;
  }
  .el-tabs__item:hover {
    color:#fb9678;
  }
  .el-tabs__item.is-active {
    color:#fb9678;
  }
  .el-tabs__active-bar {
    background-color:#fb9678;
  }
}
/deep/.el-table {
    background:@bg-color;
     border-color:@border-color;
    tr {
      color:#ced4da;
      .el-checkbox__inner {
        background-color:#272c36;
        border:1px solid #adb5bd;
      }
      .is-checked {
        .el-checkbox__inner {
          background-color:#fb9678;
          border:1px solid #fb9678;
        }
      }
      th {
        background:@bg-color;
        border-color:@border-color;
      }
      
      td {
        background:@bg-color;
        border-color:@border-color;
        /deep/.el-button {
          height:25px;
          line-height:25px;
          padding:0 10px;
           
        }
      }
      
    }
     .has-gutter {
        .el-checkbox {
          display:none;
        }
      }
    tr:hover {
      td {
        background-color:#303641;
      }
    }
     
  }
  .el-table::before {
    background:@border-color;
  }
  .el-table::after {
    background:@border-color;
  }
.pageBox {
    width:100%;
    margin-top:5px;
    /deep/.el-pagination {
      float:right;
      .btn-prev {
        background:#303641
      }
      .btn-next {
        background:#303641
      }
      .el-input__inner {
        background:#303641
      }
    }
  }
</style>
/*
 * @Description: 首页
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-16 21:55:11
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-23 20:23:47
 */
import{queryTrainList,deleteTrain,queryTrainSum} from "@/api/index/trainManage"
import{dateFormat} from "@/utils/index"
import scriptCard from "@/components/scriptCard/scriptCard"
import menuList from 'components/menuList/menuList.vue'
import {saveModel} from '@/api/index/modelManage.js';
export default {
  name: 'projectManage',
  components: {
    scriptCard,
    menuList,
  },
  data() {
    return {
      menuObj: {
        title: '训练总计',
        total: 0,
        menuList: [],
        active:'classification'
      },
      type: 'add',
      tablePag: {
        pageNo: 1,
        pageSize: 15,
        learnType:'',
        totalRecord: 0
      },
      itemObj: {},
      tableData: [],
      dialogTableVisible:false,
      label:'准确率',
      dataProp:'accuracy'
    }
  },
  methods: {
    addPro() {
      this.$router.push({
        name:'trainAdd',
        query:{
          type:'add'
        }
      })
    },
    check(row) {
      this.$router.push({
        name:'trainAdd',
        query:{
          type:'check',
          trainId:row.trainId
        }
      })
    },
    cancle(){
      this.dialogTableVisible = true
    },
    handleWakeUp(item){
      this.itemObj = item
      this.dialogTableVisible = true
    },
    deleteRow(data) {
      this.$confirm('确认删除此训练？')
        .then(() => {
          deleteTrain({ trainId: data.trainId }).then(() => {
            this.$message({
              type: 'success',
              message: '删除成功'
            })
            this.tablePag.pageNo = 1;
            this.queryTrainList();
          })
        })
        .catch(() => {})
    },
    editRow(row) {
      this.$router.push({
        name:'projectAdd',
        query:{
          id: row.serverId,
          type:'edit'
        }
      })
    },
    checkRow(row){
      this.$router.push({
        name:'projectAdd',
        query:{
          id: row.serverId,
          type:'check'
        }
      })
    },
    queryTrainList(){
      this.tablePag.learnType = this.menuObj.active
      queryTrainList(this.tablePag).then((res)=>{
        let list = res.list
        list.forEach((row)=>{
          row.accuracy = row.accuracy.toFixed(4)
          row.mae = row.mae.toFixed(4)
          row.loss = row.loss.toFixed(4)
          row.time = dateFormat('YYYY/mm/dd',row.time)
        })
        this.tableData = list
        this.tablePag.totalRecord = res.total;
      })
    },
    handleCurrentChange(val){
      this.tablePag.pageNo = val;
      this.queryTrainList();
    },
    saveModel(item){
      let params = {
        form:item.trainConfig.form,
        trainData:item.trainConfig.trainMes
      }
      saveModel(params).then((res)=>{
        this.$message({
          message: '保存模型成功！',
          type: 'success'
        })
      })
    },
    queryTrainSum(){
      queryTrainSum().then((res) =>{
        this.menuObj.total = res.total
        this.menuObj.menuList = res.list
        this.menuObj.active ='classification'
      })
    },
    selectMenu(item){
      this.tablePag= {
        pageNo: 1,
        pageSize: 15,
        learnType:'',
        totalRecord: 0
      }
      this.menuObj.active = item.type
      this.label = item.type =='classification'?'准确率':'平均误差'
      this.dataProp = item.type =='classification'?'accuracy':'mae'
      this.queryTrainList()
    }
  },
  mounted() {
    this.queryTrainSum()
    this.queryTrainList()
  }
}

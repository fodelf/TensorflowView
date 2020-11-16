/*
 * @Description: 首页
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-16 21:55:11
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-16 09:15:21
 */
import{queryTrainList} from "@/api/index/trainManage"
import{dateFormat} from "@/utils/index"
import scriptCard from "@/components/scriptCard/scriptCard"
import {saveModel} from '@/api/index/modelManage.js';
export default {
  name: 'projectManage',
  components: {
    scriptCard
  },
  data() {
    return {
      type: 'add',
      tablePag: {
        pageNo: 1,
        pageSize: 15,
        totalRecord: 0
      },
      itemObj: {},
      tableData: [],
      dialogTableVisible:false,
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
    cancle(){
      this.dialogTableVisible = true
    },
    handleWakeUp(item){
      this.itemObj = item
      this.dialogTableVisible = true
    },
    deleteRow(data) {
      this.$confirm('确认删除此服务？')
        .then(() => {
          deleteService({ serverId: data.serverId }).then(() => {
            this.$message({
              type: 'success',
              message: '删除成功'
            })
            this.queryProList(true)
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
      queryTrainList().then((res)=>{
        res.forEach((row)=>{
          row.accuracy = row.accuracy.toFixed(4)
          row.loss = row.loss.toFixed(4)
          row.time = dateFormat('YYYY/mm/dd',row.time)
        })
        this.tableData = res
      })
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
    }
  },
  mounted() {
    this.queryTrainList()
  }
}

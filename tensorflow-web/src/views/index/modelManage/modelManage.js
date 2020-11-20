/*
 * @Description: 首页
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-16 21:55:11
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-20 08:42:22
 */
import{queryModelList,deleteModelById} from "@/api/index/modelManage"
import{dateFormat} from "@/utils/index"
import scriptCard from "@/components/scriptCard/scriptCard"
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
    queryModelList(){
      queryModelList(this.tablePag).then((res)=>{
        let list = res.list
        list.forEach((row)=>{
          row.accuracy = row.accuracy.toFixed(4)
          row.loss = row.loss.toFixed(4)
          row.time = dateFormat('YYYY/mm/dd',row.time)
        })
        this.tableData = list
        this.tablePag.totalRecord = res.total;
      })
    },
    handleCurrentChange(val){
      this.tablePag.pageNo = val;
      this.queryModelList();
    },
    handleDelete(data) {
      this.$confirm('确认删除此训练？')
        .then(() => {
          deleteModelById({ modelId: data.modelId }).then(() => {
            this.$message({
              type: 'success',
              message: '删除成功'
            })
            this.tablePag.pageNo = 1;
            this.queryModelList();
          })
        })
        .catch(() => {})
    }
  },
  mounted() {
    this.queryModelList()
  }
}

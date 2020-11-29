/*
 * @Description: 首页
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-16 21:55:11
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-24 22:11:16
 */
import{queryModelList,deleteModelById,queryModelSum} from "@/api/index/modelManage"
import{dateFormat} from "@/utils/index"
import scriptCard from "@/components/scriptCard/scriptCard"
import menuList from 'components/menuList/menuList.vue'
export default {
  name: 'projectManage',
  components: {
    scriptCard,
    menuList
  },
  data() {
    return {
      menuObj: {
        title: '模型总计',
        total: 0,
        menuList: [],
        active:'classification'
      },
      type: 'add',
      tablePag: {
        pageNo: 1,
        pageSize: 15,
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
    modelAction(data) {
      this.$router.push({
        name:'modelAction',
        query:{
          modelId:data.modelId
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
      this.tablePag.learnType = this.menuObj.active
      queryModelList(this.tablePag).then((res)=>{
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
      this.queryModelList();
    },
    handleDelete(data) {
      this.$confirm('确认删除此模型？')
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
      this.queryModelList()
    },
    queryModelSum(flag){
      queryModelSum().then((res) =>{
        this.menuObj.total = res.total
        this.menuObj.menuList = res.list
        if(flag){
          this.menuObj.active ='classification'
        }
      })
    },
  },
  mounted() {
    this.queryModelSum(true)
    this.queryModelList()
  }
}

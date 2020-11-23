/*
 * @Description: 首页
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-16 21:55:11
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-23 19:10:21
 */
import menuList from 'components/menuList/menuList.vue'
import {
  getDataSum,
  getDataList,
  queryTrainById
} from '@/api/index/dataManage.js'
export default {
  name: 'projectManage',
  data() {
    return {
      type: 'add',
      menuObj: {
        title: '数据源总计',
        total: 0,
        menuList: [],
        active:'file'
      },
      tablePag: {
        pageNo: 1,
        pageSize: 15,
        totalRecord: 0
      },
      dataList: [],
      expandTableLoding: true,
      itemObj: {},
      tableData: []
    }
  },
  components: {
    menuList,
  },
  methods: {
    addPro() {
      this.$router.push({
        name:'dataAdd',
        query:{
          type:'add'
        }
      })
    },
    addTrain(){
      this.$router.push({
        name:'trainAdd',
        query:{
          type:'add'
        }
      })
    },
    /**
     * @name: selectMenu
     * @description: 根据服务类型查询服务
     * @param {type}: 默认参数
     * @return {type}: 默认类型
     */
    selectMenu(item) {
      let params = {}
      if(!item) {
        params = {
          type: 'all'
        }
      }else {
        this.itemObj = item
        params = {
          type: item.value
        }
      }
    },
    /**
     * @name: queryProList
     * @description: 获取服务列表
     * @param {type}: 默认参数
     * @return {type}: 默认类型
     */
    queryProList() {
      getDataSum({}).then(res => {
        this.menuObj.total = res.total
        this.menuObj.menuList = res.menuList || []
          this.$nextTick(() => {
            this.selectMenu()
          })
      })
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
    dateFormat(fmt, date) {
      date = new Date(date);
      let ret;
      const opt = {
          "Y+": date.getFullYear().toString(),        // 年
          "m+": (date.getMonth() + 1).toString(),     // 月
          "d+": date.getDate().toString(),            // 日
          "H+": date.getHours().toString(),           // 时
          "M+": date.getMinutes().toString(),         // 分
          "S+": date.getSeconds().toString()          // 秒
          // 有其他格式化字符需求可以继续添加，必须转化成字符串
      };
      for (let k in opt) {
          ret = new RegExp("(" + k + ")").exec(fmt);
          if (ret) {
              fmt = fmt.replace(ret[1], (ret[1].length == 1) ? (opt[k]) : (opt[k].padStart(ret[1].length, "0")))
          };
      };
      return fmt;
    },
    getDataList(){
      getDataList(this.tablePag).then((res)=>{
        let list = res.list
        list.forEach((data)=>{
          data.fileSize = Math.floor(data.fileSize/1024) +"k"
          data.time = this.dateFormat("YYYY/mm/dd HH:MM:SS",data.time)
          data.hasChildren = true
          data.children = []
          data.isOpen = false
        })
        this.tableData = list
        this.tablePag.totalRecord = res.total;
      })
    },
    handleCurrentChange(val){
     this.tablePag.pageNo = val;
     this.getDataList();
    },
    handleExpandChange(row){
      if(row.isOpen){
        row.isOpen = false
        for(let i =0 ; i <this.tableData.length;i++){
          let children = this.tableData[i];
          if(children.dataId ==row.dataId){
            this.tableData[i] = row
            this.tableData = JSON.parse(JSON.stringify(this.tableData))
            this.$forceUpdate()
            break;
          }
        }
        return;
      }else{
        row.isOpen = true
      }
      queryTrainById({dataId:row.dataId}).then((res)=>{
        row.children = res
        for(let i =0 ; i <this.tableData.length;i++){
           let children = this.tableData[i];
           if(children.dataId ==row.dataId){
             this.tableData[i] = row
             this.tableData = JSON.parse(JSON.stringify(this.tableData))
             this.$forceUpdate()
             break;
           }
        }
       
        this.expandTableLoding = false
      })
    //  alert("ss")
    },
  },
  mounted() {
    this.queryProList(true)
    this.getDataList();
  },
  created() {
    
  }
}

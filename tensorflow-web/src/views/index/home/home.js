/*
 * @Description: 首页
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-16 21:55:11
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-09-22 08:50:24
 */
import cardNum from '@/components/cardNum/cardNum'
import carousel from '@/components/carousel/carousel.vue'
import actionModule from '@/components/actionModule/actionModule.vue'
import barLinesChart from '@/components/barLinesChart/BarLinesChart'
import weather from '@/components/weather/weather.vue'
import { getIndexCount, queryIndexTrend, queryActualTime, queryWarningList} from '@/api/home.js'
import { getServiceList } from '@/api/index/projectManage.js'
export default {
  name: 'home',
  data() {
    return {
      chartData:null,
      serviceType:'all',
      serviceList:[{
        "serviceName":"全部",
        "serverId":"all"
      }],
      cardList: [
        {
          icon: 'icon-xiangmu',
          label: '服务总数',
          num: 0,
          percent: '50%',
          proColor: '#fb9678',
          key: 'serverSum'
        },
        {
          icon: 'icon-mobanguanli1',
          label: '告警总数',
          num: 0,
          percent: '60%',
          proColor: '#01c0c8',
          key: 'warningSum'
        },
        {
          icon: 'icon-mobanguanli',
          label: '请求总数',
          num: 0,
          percent: '70%',
          proColor: '#ab8ce4',
          key: 'requestSum'
        },
        {
          icon: 'icon-gongju',
          label: '失败总数',
          num: 0,
          percent: '80%',
          proColor: '#00c292',
          key: 'failSum'
        }
      ],
      systemStatus:{
        "dataSum":{"fail":0,"success":0,"total":0},
        "realTime":"2020/09/09",
        "todayState":
        "good"
      },
      carouselList: [],
      todoList: [],
      personalObj: {
        msgTit: '个人动态',
        msgList: []
      },
      teamObj: {
        msgTit: '团队动态',
        msgList: []
      }
    }
  },
  components: {
    cardNum,
    carousel,
    actionModule,
    barLinesChart,
    weather
  },
  methods: {
    /**
     * @name: queryIndexCount
     * @description: 查询文件数量
     * @param {type}: 默认参数
     * @return {type}: 默认类型
     */
    queryIndexCount() {
      console.log('0000')
      getIndexCount().then(res => {
        console.log('2222')
        console.log(res)
        this.cardList.map(item => {
          return (item.num = res[item.key] || 0)
        })
      })
    },
    queryChart() {
      queryIndexTrend(this.serviceType).then(res => {
        this.chartData = res
      })
    },
    getActualTime() {
      queryActualTime().then(res=>{
        this.systemStatus = res
      })
    },
    getWarningList() {
      queryWarningList().then(res=>{
        this.carouselList = res.warningList || []
      })
    },
    getServiceList() {
      // let params = {}
      // params = {
      //   type: "all"
      // }
      let list =  [{
        "serviceName":"全部",
        "serverId":"all"
      }]
      this.serviceList = list
      getServiceList().then((res) => {
        this.serviceList = list.concat(res.serverList || [])
      })
    },
  },
  mounted() {
    console.log("pc")
  },
  destroyed(){
    console.log("pd")
  },
  beforeCreate(){
    console.log("pbeforeCreated")
  },
  created() {
    this.queryIndexCount()
    this.queryChart()
    this.getActualTime()
    this.getWarningList()
    this.getServiceList()
  }
}

/*
 * @Description: 首页
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-16 21:55:11
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-09-22 08:50:24
 */
import cardNum from '@/components/cardNum/cardNum.vue'
import barLinesChart from '@/components/barLinesChart/BarLinesChart'
import weather from '@/components/weather/weather.vue'
import { getIndexCount, queryIndexTrend,getModel} from '@/api/index/home.js'
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
          label: '数据源总数',
          num: 0,
          percent: '50%',
          proColor: '#fb9678',
          key: 'dataSum'
        },
        {
          icon: 'icon-mobanguanli',
          label: '训练总数',
          num: 0,
          percent: '70%',
          proColor: '#ab8ce4',
          key: 'trainSum'
        },
        {
          icon: 'icon-mobanguanli1',
          label: '模型总数',
          num: 0,
          percent: '60%',
          proColor: '#01c0c8',
          key: 'modelSum'
        },
        {
          icon: 'icon-gongju',
          label: '请求总数',
          num: 0,
          percent: '80%',
          proColor: '#00c292',
          key: 'resquestSum'
        }
      ],
      systemStatus:{
        best:false,
        bad:false,
      },
      carouselList: [],
      isgood:true
    }
  },
  components: {
    cardNum,
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
    getWarningList() {
      queryWarningList().then(res=>{
        this.carouselList = res.warningList || []
      })
    },
    getModel(){
      getModel().then(res=>{
        this.systemStatus = res
      })
    }
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
    this.getModel()
    // this.getActualTime()
    // this.getWarningList()
    // this.getServiceList()
  }
}

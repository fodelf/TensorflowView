<!--
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-16 21:59:55
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-09-22 09:02:14
 -->
<template>
  <div ref="chart" id ='chart'></div>
</template>

<script>
import echarts from 'echarts'
export default {
  name: 'barLinesChart',
  props:['chartData'],
  data() {
    return {
      myChart:null,
      option: {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
              type: 'cross',
              crossStyle: {
                  color: '#999'
              }
          }
        },
        color: ['rgb(251, 150, 120)', 'rgb(1, 192, 200)', 'rgb(171, 140, 228)'],
        legend: {
            data: ['失败次数', '成功次数', '汇总次数'],
            // icon: 'circle',
            right: 0,
            itemWidth: 15, //图例的宽度
            itemHeight: 10, //图例的高度
            textStyle: {
              //图例文字的样式
              color: '#ced4da',
              fontSize: 12
            }
        },
        xAxis: [
            {
                type: 'category',
                data: [],
                axisPointer: {
                    type: 'shadow'
                },
                axisLabel: {
                  color: '#888'
                },
                axisLine: {
                  lineStyle: {
                    color: '#666'
                  }
                }
            }
        ],
        yAxis: [
            {
                type: 'value',
                // name: '次数',
                // min: 0,
                // max: 250,
                // interval: 50,
                axisLabel: {
                    formatter: '{value}',
                    color: '#888'
                },
                axisLine: {
                  show: false
                },
                splitLine: {
                  lineStyle: {
                    color: '#666'
                  }
                }
            },
            {
                type: 'value',
                // name: '次数',
                // min: 0,
                // max: 25,
                // interval: 5,
                axisLabel: {
                    formatter: '{value}',
                    color: '#888'
                },
                 axisLine: {
                  show: false
                },
                splitLine: {
                  lineStyle: {
                    color: '#666'
                  }
                }
            }

        ],
        series: []
      }
    }
  },
  methods: {
    initChart() {
      this.myChart = echarts.init(document.getElementById('chart'))
      // this.myChart.setOption(this.option)
    }
  },
  mounted() {
    this.initChart()
    window.onresize = ()=> {
      try {
        this.myChart.resize()
      } catch (error) {

      }
    }
  },
  created() {
  },
  destroyed(){
  },
  beforeCreate(){
  },
  watch:{
    // 组件封装稍后
    chartData:function(newValue) {
      if(JSON.stringify(newValue) != '{}'){
        console.log(newValue)
        let xAxis =[]
        let yAxis =[]
        if(newValue.length < 7){
          let dis =  7 - newValue.length;
          let child = newValue[0]?newValue[0]:[new Date()]
          let time  = child[0]
          for(let i = 0; i < dis; i++){
            var now=new Date(time);
            var date=new Date(now.getTime()-(i+1)*24*3600*1000);
            var year=date.getFullYear();
            var month=date.getMonth()+1>9?date.getMonth()+1:"0"+(date.getMonth()+1);
            var day=date.getDate()>9?date.getDate():"0"+date.getDate();
            var date=year+"/"+month+"/"+day;
            var childData =[date ,0]
            newValue.unshift(childData);
          }
        }
        newValue.forEach((item)=>{
          xAxis.push(item[0]);
          yAxis.push(item[1]);
        })
        this.option.series = []
        this.option.xAxis[0].data = xAxis;
        let series = [{
          data:yAxis,
          type: 'line'
        }]
        // let failObj = {
        //   name: '失败次数',
        //   type:'bar',
        //   data: newValue.failList
        // }
        // this.option.series.push(failObj)
        // let successObj = {
        //   name: '成功次数',
        //   type:'bar',
        //   data: newValue.successList
        // }
        // this.option.series.push(successObj)
        // let totalObj = {
        //   name: '汇总次数',
        //   type:'line',
        //   data: newValue.totalList
        // }
        // this.option.series.push(totalObj)
        this.option.series = series;
        this.myChart.setOption(this.option)
      }
    }
  }

}
</script>

<style lang="less" scoped>
#chart {
  width: 100%;
  height: calc(100% - 60px);
  padding: 10px;
  box-sizing: border-box;
}
</style>

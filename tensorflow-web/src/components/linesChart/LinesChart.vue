<!--
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-16 21:59:55
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2020-04-27 09:19:54
 -->
<template>
  <div ref="chart" id ='chart'></div>
</template>

<script>
import echarts from 'echarts'
export default {
  name: 'linesChart',
  props:['chartData'],
  data() {
    return {
      myChart:null,
      option: {
        title: {
          text: '日常操作记录',
          textStyle: {
            color: '#ced4da',
            fontWeight: 500
          }
        },
        color: ['rgb(251, 150, 120)', 'rgb(1, 192, 200)', 'rgb(171, 140, 228)','rgb(0, 194, 146)'],
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['项目', '模板', '组件', '脚本'],
          icon: 'circle',
          right: 0,
          itemWidth: 10, //图例的宽度
          itemHeight: 10, //图例的高度
          textStyle: {
            //图例文字的样式
            color: '#ced4da',
            fontSize: 12
          }
        },
        grid: {
          left: '3%',
          right: '7%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: [],
          axisLabel: {
            color: '#888'
          },
          axisLine: {
            lineStyle: {
              color: '#666'
            }
          }
        },
        yAxis: {
          type: 'value',
          axisLine: {
            show: false
          },
          axisLabel: {
            color: '#888'
          },
          splitLine: {
            lineStyle: {
              color: '#666'
            }
          }
        },
        series: []
      }
    }
  },
  methods: {
    initChart() {
      this.myChart = echarts.init(document.getElementById('chart'))
      // myChart.setOption(this.option)
    }
  },
  mounted() {
    this.initChart()
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
        this.option.xAxis.data = newValue.date
        newValue.list.forEach((item)=>{
          let obj = {
            name: item.name,
            type: 'line',
            stack: '总量',
            smooth: true,
            data: item.list
          }
          this.option.series.push(obj)
        })
        this.myChart.setOption(this.option)
      }
    }
  }

}
</script>

<style lang="less" scoped>
#chart {
  width: 100%;
  height: 100%;
  padding: 15px;
  box-sizing: border-box;
}
</style>

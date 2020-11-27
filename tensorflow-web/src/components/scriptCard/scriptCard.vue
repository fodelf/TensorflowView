<!--
 * @Description: 描述
 * @Author: pym
 * @Github: https://github.com/fodelf
 * @Date: 2020-04-10 21:26:24
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-24 12:58:32
 -->
<template>
  <div class="scriptCard">
    <el-form>
        <el-form-item label="调用路径">
        </el-form-item>
        <div style='background: #272c36;height:40px;line-height:40px;'>{{url}}</div>
        <el-form-item label="调用参数(默认读取第一行数据除modelId可自行修改)">
          <el-input
              type="textarea"
              v-model="param"
              :rows="7"
              resize="none"
            ></el-input>
        </el-form-item>
        <el-form-item label="原始结果">
          <span style='color:white'>{{org}}</span>
        </el-form-item>
        <el-form-item label="预测结果">
          <!-- <span style='color:white'>{{res}}</span> -->
          <el-input
              type="textarea"
              v-model="res"
              :rows="2"
              resize="none"
          ></el-input>
        </el-form-item>
    </el-form>
    <div class="btn_row">
      <div class="col_box">
        <el-button type="primary" size="small" @click="test()"
          >调用</el-button>
        <!-- <el-button type="primary" size="small" @click="cancle(itemObj)"
          >取消</el-button>   -->
      </div>
    </div>
  </div>
</template>

<script>
import { getParam ,trainOnline} from '@/api/index/modelManage'
export default {
  name: 'scriptCard',
  props: {
    itemObj: {
      type: Object,
      default: function() {
        return {
          scriptContent: '',
          modelName: ''
        }
      }
    }
  },
  data() {
    return {
      url:location.host+"/api/v1/model/trainOnline",
      param: '',
      res:'',
      org:''
    }
  },
  watch: {
    itemObj: {
      handler(newVal, oldVal){
        if('accuracy' in newVal){
          let formConfig = JSON.parse(newVal.formConfig)
          getParam(formConfig).then((res) => {
            let param = {
              modelId:newVal.modelId,
              trainData:res.param
            }
            this.org= res.target
            this.param = JSON.stringify(param, null, 2)
          })
        }
      },
      deep: true,
      immediate: true
    }
  },
  methods: {
    test(){
      trainOnline(JSON.parse(this.param)).then((res) =>{
        if(typeof res == "object"){
          this.res = JSON.stringify(res,null, 2)
        } else{
          this.res = res
        } 
      })
    },
    cancle() {
      this.$emit('cancle')
    }
  }
}
</script>

<style lang="less" scoped>
.scriptCard {
  width: 100%;
  height: 100%;
  // padding-bottom: 10px;
  box-sizing: border-box;
  border-radius: 5px;
  background: #353c48;
  box-shadow: 0 0 4px #353c48;
  .cardTit {
    height: 40px;
    line-height: 40px;
    width: 100%;
    background: #303641;
    padding: 0 15px;
    box-sizing: border-box;
    color: #ced4da;
    font-size: 14px;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
  }
  /deep/.el-textarea__inner {
    background: #272c36;
    outline: none;
    border: none;
    color: #ced4da;
    border-radius: 0;
  }
  .btn_row {
    width: 100%;
    padding: 10px 15px;
    box-sizing: border-box;
    display: flex;
    justify-content: flex-end;
  }
  /deep/.el-form-item__label{
    color: white
  }
  /deep/.el-form-item{
    margin-bottom: 0px;
  }
}
</style>

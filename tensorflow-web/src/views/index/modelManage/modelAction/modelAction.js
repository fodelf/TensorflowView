/*
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-09-06 15:56:49
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-24 21:23:48
 */
import { getParam ,trainOnline} from '@/api/index/modelManage'
export default {
  name: 'dataAdd',
  data() {
    return {
      url:location.host+"/api/v1/model/trainOnline",
      param: '',
      res:'',
      org:'',
      form:{}
    }
  },
  methods:{
    cancel() {
      this.$router.go(-1)
    },
    getParam(){
      getParam({modelId:this.$route.query.modelId}).then((res) => {
        let param = {
          modelId:this.$route.query.modelId,
          trainData:res.param
        }
        this.org= res.target
        this.param = JSON.stringify(param, null, 2)
      })
    },
    test(){
      trainOnline(JSON.parse(this.param)).then((res) =>{
        if(typeof res == "object"){
          this.res = JSON.stringify(res,null, 2)
        } else{
          this.res = res
        }
      })
    },
  },
  created() {
    this.getParam();
  }
}
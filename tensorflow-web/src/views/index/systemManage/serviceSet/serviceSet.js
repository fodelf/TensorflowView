/*
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-08-11 14:27:02
 * @LastEditors: pym
 * @LastEditTime: 2020-09-06 21:24:55
 */
import systemCard from '@/components/systemCard/systemCard'
import serviceEdit from '@/components/serviceEdit/serviceEdit'
import {
  confirmConsul,
  confirmMq,
  querySystemDetail
} from '@/api/system.js'
export default {
   name:'serviceSet',
   components:{
    systemCard,
    serviceEdit
   },
   data() {
     return {
      serviceList:[
        {
          title:'Consul配置用于注册中心',
          address:'',
          port:'',
          type:'consul'
        },
        {
          title:'RabbitMQ配置用于日志监控',
          address:'',
          port:'',
          userName:'',
          password:'',
          type:'rabbitMq'
        }
      ]
     }
   },
   methods: {
    showEdit(obj) {
      this.$refs.editService.show(obj)
    },
    confirm(obj){
      if(obj.type === 'consul') {
        let params = {
          address: obj.address,
          port:obj.port*1
        }
        confirmConsul(params).then(res=>{
          this.$refs.editService.close()
          this.getDetail()
        })
      }else {
        let params = {
          address:obj.address,
          port:obj.port*1,
          userName:obj.userName,
          password:obj.password
        }
        confirmMq(params).then(res=>{
          this.$refs.editService.close()
          this.getDetail()
        })
      }
    },
    getDetail() {
      querySystemDetail().then(res=>{
        this.serviceList.map(item=>{
          if(JSON.stringify(res[item.type])!=='{}'){
            item.address =  res[item.type].address || ''
            item.port = res[item.type].port || ''
            if(item.type === 'rabbitMq'){
              item.userName =  res[item.type].userName || ''
              item.password = res[item.type].password || ''
            }
          } 
           
        })
      })
    }
   },
   created() {
     this.getDetail()
   }
 }
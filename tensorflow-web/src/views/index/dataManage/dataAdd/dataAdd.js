/*
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-09-06 15:56:49
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-06 08:36:51
 */
import {
  getDataType,
  createData
  // dataDetail,
  // updatedata
} from '@/api/index/dataManage.js'
export default {
  name: 'dataAdd',
  data() {
    const validateEn = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入数据源名称'));
      } else {
        if((/[^\w\.\/]/g).test(value)){
          callback(new Error('只能输入英文字母和数字'));
        }
        callback();
      }
    }
    const validateCheckPath = (rule, value, callback) => {
      if (value === '') {
        callback();
      } else {
        if(!(/^\/[0-9a-zA-Z]*$/).test(value)){
          callback(new Error('路径格式不正确'));
        }
        callback();
      }
    }
    return {
      form: {
        dataName: '',
        dataType: '',
        filePath:'',
        fileName:'',
        fileSize:''
      },
      dataRules:{
        dataName:[
          { required: true, validator: validateEn, trigger: 'blur' },
        ],
        dataType:[
          { required: true, message: '请选择服务类型', trigger: 'blur' },
        ]
      },
      serverList:[]
    }
  },
  methods:{
    getFile(res){
      this.form.filePath = res.data.filePath
      this.form.fileName = res.data.fileName
      this.form.fileSize = res.data.fileSize
    },
    cancel() {
      this.$router.push({
        name:'dataManage'
      })
    },
    queryProjectType() {
      getDataType().then(res=>{
        this.serverList = res || []
        try {
          this.form.dataType = this.serverList[0]['dataId']
        } catch (error) {}
      })
    },
    save() {
      createData(this.form).then(res=>{
        this.$router.push({
          name:'dataManage'
        })
      })
    },
    initDetail() {
      let id = this.$route.query.id
      dataDetail(id).then(res=>{
        this.ruleForm = JSON.parse(JSON.stringify(res))
      })
    }
  },
  created() {
    this.queryProjectType()
    if(this.$route.query.id){
      this.initDetail()
    }else {
      this.ruleForm= {
      }
    }
  }
}
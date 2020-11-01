/*
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-09-06 15:56:49
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-09-24 09:14:42
 */
import {
  getServiceType,
  addService,
  serviceDetail,
  updateService
} from '@/api/index/projectManage.js'
export default {
  name: 'projectAdd',
  data() {
    const validateEn = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入服务名称'));
      } else {
        if((/[^\w\.\/]/g).test(value)){
          callback(new Error('只能输入英文字母和数字'));
        }
        callback();
      }
    }
    const validateAddress= (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入服务地址'));
      } else {
        if(!((/^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/).test(value)||(/^(?=^.{3,255}$)(http(s)?:\/\/)?(www\.)?[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+(:\d+)*(\/\w+\.\w+)*$/).test(value))){
          callback(new Error('请输入正确的服务地址'));
        }
        callback();
      }
    }
    const validatePort = (rule, value, callback) => {
      if (value === '') {
        callback();
      } else {
        if(!Number.isInteger(value*1)){
          callback(new Error('只能输入整数'));
        }
        callback();
      }
    }
    const validateBreak = (rule, value, callback) => {
      if (value === '') {
        callback();
      } else {
        if(isNaN(Number(value))){
          callback(new Error('只能输入数字'));
        }
        callback();
      }
    }
    const validateBreak1=(rule, value, callback) => {
      if (value === '') {
        callback();
      } else {
        if(isNaN(Number(value))){
          if(value<0 ||value>100){
            callback(new Error('只能输入100以内的数字'));
          }
          callback(new Error('只能输入数字'));
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
      ruleForm: {
        serviceName: '',
        serviceType: '',
        serviceAddress: '',
        servicePort: '',
        serviceRules: [],
        serviceBreak:"",
        serviceLimit:'',
        useConsulId:'',
        useConsulTag:'',
        useConsulCheckPath:'',
        useConsulPort:'',
        useConsulInterval:'',
        useConsulTimeout:'',
        dingdingAccessToken:'',
        dingdingSecret:'',
        dingdingList:[],
      },
      serviceRules:{
        serviceName:[
          { required: true, validator: validateEn, trigger: 'blur' },
        ],
        serviceType:[
          { required: true, message: '请选择服务类型', trigger: 'blur' },
        ],
        serviceAddress:[
          { required: true,validator: validateAddress, trigger: 'blur' },
        ],
        servicePort:[
          {validator: validatePort, trigger: 'blur'},
        ],
        serviceLimit:[
          {validator: validatePort, trigger: 'blur'},
        ],
        serviceBreak:[
          {validator: validateBreak1, trigger: 'blur'},
        ],
        useConsulId:[
          { validator: validateEn, trigger: 'blur' },
        ],
        useConsulTag:[
          { validator: validateEn, trigger: 'blur' },
        ],
        useConsulCheckPath:[
          { validator: validateCheckPath, trigger: 'blur' },
        ],
        useConsulInterval:[
          { validator: validateBreak, trigger: 'blur' },
        ],
        useConsulTimeout:[
          { validator: validateBreak, trigger: 'blur' },
        ]
      },
      rules:{
        apiUrl:[
          { required: true, message: '请输入正确的拦截地址', validator: validateCheckPath, trigger: 'blur' },
        ],
        pathReWriteBefore:[
          {validator: validateCheckPath, trigger: 'blur' },
        ],
        pathReWriteUrl:[
          {validator: validateCheckPath, trigger: 'blur' },
        ]
      },
      inputVisible:false,
      inputValue:'',
      baseInfo:'baseInfo',
      useConsul:'useConsul',
      messageWarn:'messageWarn',
      serverList:[]
    }
  },
  methods:{
    handleClose(tag) {
      if(this.$route.query.type =='check'){
        return
      }
      this.ruleForm.dingdingList.splice(this.ruleForm.dingdingList.indexOf(tag), 1);
    },
    showInput() {
      this.inputVisible = true;
      this.$nextTick(_ => {
        this.$refs.saveTagInput.$refs.input.focus();
      });
    },
    handleInputConfirm() {
      let inputValue = this.inputValue;
      if (inputValue) {
        this.ruleForm.dingdingList.push(inputValue);
      }
      this.inputVisible = false;
      this.inputValue = '';
    },
    addRule() {
      this.ruleForm.serviceRules.push(
        {
          interceptLoc:'',
          locationReset:'',
          pathReWriteBefore:"",
          pathReWriteUrl:""
        }
      );
    },
    deleteRule(index) {
      this.ruleForm.serviceRules.splice(index,1)
    },
    cancel() {
      this.$router.push({
        name:'projectManage'
      })
    },
    queryProjectType() {
      getServiceType().then(res=>{
        this.serverList = res.serverTypeList || []
      })
    },
    saveRule() {
      if(this.ruleForm.serviceRules.length == 0){
        this.$message({
          message: '拦截规则不能为空',
          type: 'warning'
        });
        return
      }
      this.$refs["ruleForm"].validate((valid) => {
        if (valid) {
          let params = JSON.parse(JSON.stringify(this.ruleForm))
          params.servicePort = params.servicePort*1
          params.serviceLimit = params.serviceLimit*1
          params.serviceBreak = params.serviceBreak*1
          params.useConsulPort = params.useConsulPort*1
          params.useConsulInterval = params.useConsulInterval*1
          params.useConsulTimeout = params.useConsulTimeout*1
          addService(params).then(res=>{
            this.$router.push({
              name:'projectManage'
            })
          })
        } else {
          return false
        }
      })
    },
    initDetail() {
      let id = this.$route.query.id
      serviceDetail(id).then(res=>{
        this.ruleForm = JSON.parse(JSON.stringify(res))
      })
    },
    updateRule() {
      if(this.ruleForm.serviceRules.length == 0){
        this.$message({
          message: '拦截规则不能为空',
          type: 'warning'
        });
        return
      }
      this.$refs["ruleForm"].validate((valid) => {
        if (valid) {
          let params = JSON.parse(JSON.stringify(this.ruleForm))
          params.servicePort = params.servicePort*1
          params.serviceLimit = params.serviceLimit*1
          params.serviceBreak = params.serviceBreak*1
          params.useConsulPort = params.useConsulPort*1
          params.useConsulInterval = params.useConsulInterval*1
          params.useConsulTimeout = params.useConsulTimeout*1
          updateService(params).then(res=>{
            this.$router.push({
              name:'projectManage'
            })
          })
        } else {
          return false
        }
      })
    }
  },
  created() {
    this.queryProjectType()
    if(this.$route.query.id){
      this.initDetail()
    }else {
      this.ruleForm= {
        serviceName: '',
        serviceType: 'http',
        serviceAddress: '',
        servicePort: '',
        serviceRules: [],
        serviceBreak:"",
        serviceLimit:'',
        useConsulId:'',
        useConsulTag:'',
        useConsulCheckPath:'',
        useConsulPort:'',
        useConsulInterval:'',
        useConsulTimeout:'',
        dingdingAccessToken:'',
        dingdingSecret:'',
        dingdingList:[],
      }
    }
  }
}
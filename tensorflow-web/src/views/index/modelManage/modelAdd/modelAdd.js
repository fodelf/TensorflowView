/*
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-09-06 15:56:49
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-10 12:37:32
 */
import {
  getDataList,
  createData,
  train,
  parseHeader
} from '@/api/index/dataManage.js'
export default {
  name: 'dataAdd',
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
      form: {
        dataName: '',
        dataType: '',
        filePath:'',
        target:'',
        activeFunction:'relu',
        number:2,
        times:1
      },
      isTrain:false,
      activeFuns:[
        {label: 'relu',value:'relu'},
        {label: 'sigmoid',value:'sigmoid'},
      ],
      dataRules:{
        dataName:[
          { required: true, validator: validateEn, trigger: 'blur' },
        ],
        dataType:[
          { required: true, message: '请选择服务类型', trigger: 'blur' },
        ],
        activeFuns:[
          { required: true, validator: validateEn, trigger: 'blur' },
        ],
        number:[
          { required: true, validator: validateEn, trigger: 'blur' },
        ],
        times:[
          { required: true, validator: validateEn, trigger: 'blur' },
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
      serverList:[],
      src:'',
      dataList:[{index:'类型',dataName:"xx"},{index:'类型',dataName:"xx"}],
      headerList:[
        { name: '首列', code: 'index' },
        { name: '列一', code: 'dataName' },
        { name: '列二', code: 'fileName' },
        { name: '列三', code: 'fileType' },
        { name: '列四', code: 'fileSize' }
      ],
      trainData:{
        imgUrl:"",
        test:{
          "accuracy":"",
          "loss":""
        }
      },
      fullscreenLoading:false,
      preDataList:[],
      preHeadList:[]
    }
  },
  methods:{
    getFile(res){
      this.form.filePath = res
    },
    cancel() {
      this.$router.push({
        name:'projectManage'
      })
    },
    handleChangeDataType(){
      this.parseHeader()
    },
    queryProjectType() {
      getDataList().then(res=>{
        this.serverList = res || []
        try {
          this.form.dataType = this.serverList[0]['id']
          this.form.filePath = this.serverList[0]['filePath']
          this.parseHeader()
        } catch (error) {
          console.log(error)
        }
      })
    },
    parseHeader(){
      try {
        parseHeader({filePath:this.form.filePath}).then(res=>{
          let lineOne = {"index":"源数据"};
          let lineTow = {"index":"数据类型"};
          res.forEach((item,index)=>{
            lineOne[index] = item[index]
            lineTow[index] = item["type"]
            item["radio"]=''
          })
          this.headerList = res;
          this.headerList.unshift({ name: '首列', code: 'index' });
          this.dataList = [lineOne,lineTow];
        })
      } catch (error) {}
    },
    save() {
      createData(this.form).then(res=>{
        // this.$router.push({
        //   name:'dataManage'
        // })
      })
    },
    train(){
      // this.fullscreenLoading = true
      const loading = this.$loading({
        lock: true,
        text: '训练中，请耐心等待！',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      });
      if(!this.form.target){
        this.$message({
          message: '目标对象不能为空',
          type: 'warning'
        });
        // this.fullscreenLoading = false
        loading.close()
        return
      }
      train(this.form).then(res=>{
        this.trainData = res
        this.preHeadList = this.headerList.filter(item=>item.name !== this.form.target&&item.name !== '首列')
        let obj = {}
        this.preHeadList.forEach(item=>{
          obj[item] = ''
        })
        this.preDataList = [obj]
        this.isTrain = true
        // this.fullscreenLoading = false
        loading.close()
      }).catch(err => {
        loading.close()
      })
    },
    changeTarget(){
      this.isTrain = false
    },
    initDetail() {
      let id = this.$route.query.id
      dataDetail(id).then(res=>{
        this.ruleForm = JSON.parse(JSON.stringify(res))
      })
    },
    updateRule() {
    },
    preTrain(){
      console.log(this.preDataList)
      debugger
    }
  },
  created() {
    this.queryProjectType()
    if(this.$route.query.id){
      this.initDetail()
    }else {
      this.ruleForm= {
        dataName: '',
        dataType: '',
        dataAddress: '',
        dataPort: '',
        dataRules: [],
        dataBreak:"",
        dataLimit:'',
        useConsulId:'',
        useConsulTag:'',
        useConsulCheckPath:'',
        useConsulPort:'',
        useConsulInterval:'',
        useConsulTimeout:'',
        dingdingList:[],
      }
    }
  }
}
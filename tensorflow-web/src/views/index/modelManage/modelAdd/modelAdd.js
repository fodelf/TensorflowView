/*
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-09-06 15:56:49
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-13 08:22:48
 */
import {
  getDataList,
  createData,
  train,
  parseHeader
} from '@/api/index/dataManage.js'
import {
  preTrain
} from '@/api/index/modelManage.js'
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
      dataList:[],
      form: {
        trainName: '',
        dataName:"",
        dataId: '',
        id:"",
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
        dataId:[
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
      headerList:[
        // { name: '首列', code: 'index' },
        // { name: '列一', code: 'dataName' },
        // { name: '列二', code: 'fileName' },
        // { name: '列三', code: 'fileType' },
        // { name: '列四', code: 'fileSize' }
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
      preHeadList:[],
      prData:''
    }
  },
  methods:{
    getFile(res){
      this.form.filePath = res
    },
    cancel() {
      this.$router.go(-1)
      // this.$router.push({
      //   name:'projectManage'
      // })
    },
    handleChangedataId(){
      this.parseHeader()
    },
    queryProjectType() {
      getDataList().then(res=>{
        this.serverList = res || []
        try {
          this.form.dataId = this.serverList[0]['dataId']
          this.form.id = this.serverList[0]['id']
          this.form.filePath = this.serverList[0]['filePath']
          this.form.dataName = this.serverList[0]['dataName']
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
      let param = {
        form:this.form,
        trainData:this.trainData
      }
      createData(param).then(res=>{
        this.$message({
          message: '保存模型成功！',
          type: 'success'
        });
        // this.$router.push({
        //   name:'dataManage'
        // })
      })
    },
    train(){
      // this.fullscreenLoading = true
      // const loading = this.$loading({
      //   lock: true,
      //   text: '训练中，请耐心等待！',
      //   spinner: 'el-icon-loading',
      //   background: 'rgba(0, 0, 0, 0.7)'
      // });
      if(!this.form.target||!this.form.trainName){
        this.$message({
          message: '名称和目标对象不能为空',
          type: 'warning'
        });
        // this.fullscreenLoading = false
        // loading.close()
        return
      }
      train(this.form).then(res=>{
        this.$message({
          message: '训练以及开始，稍后在消息中查看！',
          type: 'success'
        });
        // this.trainData = res
        // let headerList = JSON.parse(JSON.stringify(this.headerList))
        // this.preHeadList = headerList.filter(item=>item.name !== this.form.target&&item.name !== '首列')
        // let obj = {}
        // this.preHeadList.forEach(item=>{
        //   obj[item] = ''
        // })
        // this.preDataList = [obj]
        // this.isTrain = true
        // this.fullscreenLoading = false
        // loading.close()
      }).catch(err => {
        // loading.close()
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
      let headerList = JSON.parse(JSON.stringify(this.headerList))
      var preHeadList = headerList.filter(item=>item.name !== this.form.target&&item.name !== '首列')
      var preData = {};
      preHeadList.forEach((item,index)=>{
        preData[item.name] = this.preDataList[0][index];
      })
      let param = {
         form:this.form,
         trainData:this.trainData,
         preData:preData
      }
      preTrain(param).then((res)=>{
        this.prData = res;
      })
    }
  },
  created() {
    this.queryProjectType()
    if(this.$route.query.id){
      this.initDetail()
    }else {
      this.ruleForm= {
        dataName: '',
        dataId: '',
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
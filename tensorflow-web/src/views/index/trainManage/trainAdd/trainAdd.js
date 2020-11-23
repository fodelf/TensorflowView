/*
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-09-06 15:56:49
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-23 12:56:56
 */
import {
  getDataAll,
  createData,
  parseHeader,
} from '@/api/index/dataManage.js'
import {
  saveModel
} from '@/api/index/modelManage.js'
import {
  preTrain,
  queryTrainByTrainId,
  trainAction,
} from '@/api/index/trainManage.js'
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
        number:1,
        times:100,
        learnType:"classification"
      },
      typeList:[{
        label:"回归",
        value:"regression"
      },{
        label:'分类',
        value:"classification"
      }
      ],
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
        ],
        learnType:[
          { required: true, validator: validateEn, trigger: 'blur' },
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
      prData:'',
      isShowPre:false
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
    getDataAll(flag) {
      getDataAll().then(res=>{
        this.serverList = res || []
        try {
          if(flag){
            this.form.dataId = this.serverList[0]['dataId']
            this.form.id = this.serverList[0]['id']
            this.form.filePath = this.serverList[0]['filePath']
            this.form.dataName = this.serverList[0]['dataName']
          }
          this.parseHeader()
        } catch (error) {
          console.log(error)
        }
      })
    },
    getDataAllCheck(){
      getDataAll().then(res=>{
        this.serverList = res || []
        this.parseHeader(true)
      })
    },
    parseHeader(flag){
      try {
        parseHeader({filePath:this.form.filePath}).then(res=>{
          let lineOne = {"index":"源数据"};
          let lineTow = {"index":"数据类型"};
          let preLineOne = {}
          res.forEach((item,index)=>{
            lineOne[index] = item[index]
            lineTow[index] = item["type"]
            item["radio"]=''
            if(flag){
              preLineOne[index] = item[index]
            }
          })
          this.headerList = res;
          this.headerList.unshift({ name: '首列', code: 'index' });
          this.dataList = [lineOne,lineTow];
          if(flag){
            let headerList = JSON.parse(JSON.stringify(this.headerList))
            this.preHeadList = headerList.filter(item=>item.name !== this.form.target&&item.name !== '首列')
            this.preDataList = [preLineOne]
          }
        })
      } catch (error) {}
    },
    save() {
      let param = {
        form:this.form,
        trainData:this.trainData
      }
      saveModel(param).then(res=>{
        this.$message({
          message: '保存模型成功！',
          type: 'success'
        });
        this.$router.push({
          name:'trainManage'
        })
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
      if(this.form.learnType == 'regression'){
        let select = this.headerList.filter((item)=>{
             return  this.form.target == item.name
        })
        if(select[0].type =='文本'){
          this.$message({
            message: '文本类型不能进行回归预测',
            type: 'warning'
          });
          // this.fullscreenLoading = false
          // loading.close()
          return
        }
      }
      trainAction(this.form).then(res=>{
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
      let headerList = JSON.parse(JSON.stringify(this.preHeadList))
      var preData = {};
      headerList.forEach((item)=>{
        preData[item.name] = item[item.code];
      })
      let param = {
         form:this.form,
         trainData:this.trainData,
         preData:preData
      }
      preTrain(param).then((res)=>{
        this.isShowPre = true
        if(this.form.learnType=='classification'){
          if(this.trainData.group.length ==2){
            this.prData = (res[0][0]*100).toFixed(2) +'%';
          }else if(this.trainData.group.length >2){
            let prData =''
            this.trainData.group.forEach((item,index) =>{
              prData = prData + item+"概率是"+(res[0][index]*100).toFixed(2) +'%'+";"
            })
            this.prData = prData
          }
        }else{
          this.prData = res
        }
      })
    }
  },
  created() {
    if(this.$route.query.type =='check'){
      queryTrainByTrainId({trainId:this.$route.query.trainId}).then((res)=>{
        this.isTrain = true;
        let trainConfig = JSON.parse(res.trainConfig)
        this.form = trainConfig['form']
        this.trainData =  trainConfig['trainMes']
        this.getDataAllCheck()
      })
    }else if(this.$route.query.type =='add'){
      this.getDataAll(true)
    }
    if(this.$route.query.id){
      this.initDetail()
    }else {
    }
  }
}
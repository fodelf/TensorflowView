/*
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-08-11 14:26:40
 * @LastEditors: pym
 * @LastEditTime: 2020-08-12 15:13:36
 */
export default {
  name: 'userManage',
  data() {
    return {
      headerList:[
        { name:'用户名', code:'userName' },
        { name:'部门', code:'depart' },
        { name:'角色', code:'role' },
        { name:'邮箱', code:'email' },
        { name:'手机号', code:'phone' }
      ],
      tableData:[
        {
          userName:'111',
          depart:'233',
          role:'3434',
          email:'2587197926@qq.com',
          phone:'13245344567'
        }
      ],
      tablePag: {
        pageNo: 1,
        pageSize: 15,
        totalRecord: 0
      }
    }
  },
  methods: {
    handleCurrentChange(val) {
      this.tablePag.pageNo = val
    }
  }

}
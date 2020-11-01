/*
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-04-01 16:18:14
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-04-01 16:39:11
 */
import Terminal from '@/components/terminal/TerminalView.vue'
export default {
  name: 'projectInit',
  data () {
    return {
      type:'project',
      actionData:{}
    }
  },
  components: {
    Terminal
  },
  methods: {
  },
  mounted () {
    
  },
  created(){
    this.actionData = this.$route.params
  }
}
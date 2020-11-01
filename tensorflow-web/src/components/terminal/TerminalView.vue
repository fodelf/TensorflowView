<template>
  <div id="terminalContent">
    <div id="terminal" ref="terminal"></div>
  </div>
</template>
<script>
import { Terminal } from 'xterm'
// import { WebLinksAddon } from "xterm-addon-web-links";
import 'xterm/dist/xterm.css'
// import "xterm/dist/addons/fullscreen/fullscreen.css"; //如果不成功，请检查路径

import * as fit from 'xterm/lib/addons/fit/fit'

import * as fullscreen from 'xterm/lib/addons/fullscreen/fullscreen'
import * as attach from 'xterm/lib/addons/attach/attach'

Terminal.applyAddon(fit)
Terminal.applyAddon(attach)
Terminal.applyAddon(fullscreen) // Apply the `fullscreen` addon

export default {
  name: 'Shell',
  props: {
    type: {
      type: String,
      default: () => {
        return ''
      }
    },
    actionData: {
      type: Object,
      default: () => {
        return {}
      }
    }
  },
  data() {
    return {
      order: '',
      urlParam: {
        fullTag: '',
        namespace: '',
        podName: ''
      },
      shellWs: '', // ws实例
      term: '', // 保存terminal实例
      showOrder: '', // 保存服务端返回的命令
      inputList: [] // 保存用户输入的命令，用以上下健切换
    }
  },

  created() {
    // this.checkURLparam();
    // this.wsShell();
  },

  mounted() {
    let _this = this
    // const terminal = new Terminal();
    let term = new Terminal({
      rendererType: 'canvas', //渲染类型
      rows: 40, //行数
      convertEol: true, //启用时，光标将设置为下一行的开头
      scrollback: 10, //终端中的回滚量
      disableStdin: true, //是否应禁用输入。
      cursorStyle: 'underline', //光标样式
      cursorBlink: true, //光标闪烁
      theme: {
        foreground: 'yellow', //字体
        background: '#060101', //背景色
        cursor: 'help' //设置光标
      }
    })
    // 换行并输入起始符“$”
    term.prompt = () => {
      // term.write('\r\n$ ')
    }

    term.open(this.$refs['terminal'])
    // term.toggleFullScreen() //全屏
    term.fit()

    // term.writeln('Hello from \x1B[1;3;31mxterm.js\x1B[0m $ ')
    term.prompt()

    function runFakeTerminal(_this) {
      if (term._initialized) {
        return
      }

      term._initialized = true

      term.prompt = () => {
        term.write('\r\n ')
      }

      // term.writeln('Welcome to xterm.js')
      // term.writeln(
      //   'This is a local terminal emulation, without a real terminal in the back-end.'
      // )
      // term.writeln('Type some keys and commands to play around.')
      // term.writeln('')
      term.prompt()

      // 监控键盘输入事件
      // / **
      //     *添加事件监听器，用于按下键时的事件。事件值包含
      //     *将在data事件以及DOM事件中发送的字符串
      //     *触发了它。
      //     * @返回一个IDisposable停止监听。
      //  * /
      // let last = 0

      // term.on('key', function(key, ev) {
      //   // 可打印状态，即不是alt键ctrl等功能健时
      //   const printable =
      //     !ev.altKey && !ev.altGraphKey && !ev.ctrlKey && !ev.metaKey

      //   // 因服务端返回命令包含乱码，但使用write方法输出时并不显示，故将真实显示内容截取出来
      //   let index = _this.showOrder.indexOf('sh')
      //   let show = _this.showOrder.substr(index, _this.showOrder.length - 1)

      //   //  当输入回车时
      //   if (ev.keyCode === 13) {
      //     if (_this.order == 'cls' || _this.order == 'clear') {
      //       _this.order = ''
      //       return false
      //     }
      //     //先将数据发送
      //     term.prompt()
      //     // 判断如果不是英文给出提醒
      //     let reg = /[a-zA-Z]/
      //     let order = {
      //       Data: _this.order,
      //       Op: 'stdin'
      //     }

      //     if (!reg.test(_this.order)) {
      //       term.writeln('请输入有效指令~')
      //     } else {
      //       // 发送数据
      //       _this.inputList.push(_this.order)
      //       last = _this.inputList.length - 1
      //       _this.onSend(order)
      //       _this.order = ''
      //       // 清空输入内容变量
      //     }
      //   } else if (ev.keyCode === 8) {
      //     // 当输入退

      //     // Do not delete the prompt
      //     // 当前行字符长度如果等于后端返回字符就不进行删除
      //     if (term._core.buffer.x > _this.showOrder.length) {
      //       term.write('\b \b') // 输出退格
      //     }

      //     // 将输入内容变量删除

      //     if (_this.trim(_this.order) == _this.trim(_this.showOrder)) {
      //       return false
      //     } else {
      //       _this.order = _this.order.substr(0, _this.order.length - 1)
      //     }
      //   } else if (ev.keyCode == 38 || ev.keyCode == 40) {
      //     let len = _this.inputList.length
      //     let code = ev.keyCode

      //     if (code === 38 && last <= len && last >= 0) {
      //       // 直接取出字符串数组最后一个元素
      //       let inputVal = _this.inputList[last]
      //       term.write(inputVal)
      //       if (last > 0) {
      //         last--
      //       }
      //     }
      //     if (code === 40 && last < len) {
      //       // last现在为当前元素
      //       if (last == len - 1) {
      //         return
      //       }
      //       if (last < len - 1) {
      //         last++
      //       }

      //       let inputVal = _this.inputList[last]
      //       term.write(inputVal)
      //     }
      //   } else if (ev.keyCode === 9) {
      //     // 如果按tab键前输入了之前后端返回字符串的第一个字符，就显示此命令
      //     if (_this.order !== '' && show.indexOf(_this.order) == 0) {
      //       term.write(_this.showOrder)
      //     }
      //   } else if (printable) {
      //     // 当为可打印内容时
      //     if (/[a-zA-Z]/.test(key)) {
      //       key = key.toLowerCase()
      //     }
      //     // 存入输入内容变量
      //     _this.order = _this.order + key
      //     // 将变量写入终端内
      //     term.write(key)
      //   }
      // })

      _this.term = term

      // 粘贴事件
      // term.on('paste', function(data) {
      //   _this.order = data
      //   term.write(data)
      // })
    }
    runFakeTerminal(_this)
    //var url = `${window.location.href}://${window.location.host}:${window.location.port}`
    _this.socket = window['io'](`http://${window.location.host}`)
    // this.socket = window['io'].connect(`ws://${window.location.host}`);

    _this.socket.on('mes', data => {
      // console.log("11111111111")
      term.writeln(data)
    })
    this.initAction()
  },

  methods: {
    // 初始化action
    initAction() {
      switch (this.$props.type) {
        case 'project':
          this.handleProject()
          break

        default:
          break
      }
    },
    handleProject() {
      this.socket.emit('project', this.$route.query)
      // console.log(this.$route.query)
    },
    // 检查url参数,必要参数不存在,返回到首页
    checkURLparam() {
      let urlObj = this.base.urlValue()

      let fullTag = urlObj.full_tag ? urlObj.full_tag : '' //所在父节点
      fullTag = fullTag.replace(/(^ +| +$)/g, '')

      let namespace = urlObj.namespace ? urlObj.namespace : '' //所在父节点
      namespace = namespace.replace(/(^ +| +$)/g, '')

      let podName = urlObj.pod_name ? urlObj.pod_name : '' //所在父节点
      podName = podName.replace(/(^ +| +$)/g, '')

      if (!fullTag || !namespace) {
        //所在的父级节点为空或者deploy_id不存在的情况下,弹框提示然后返回首页
        this.$alert('缺少必要参数,马上返回首页~', '提示', {
          closeOnClickModal: false,
          closeOnPressEscape: false,
          showClose: false,
          confirmButtonText: '确定',
          type: 'error',
          callback: () => {
            this.$router.replace('/web')
          }
        })
      } else {
        this.urlParam.fullTag = fullTag //所在父节点
        this.urlParam.namespace = namespace //当前部署任务详情id
        this.urlParam.podName = podName //当前部署任务详情id
      }
    },
    /**
     * **wsShell 创建页面级别的websocket,加载页面数据
     * ws 接口:/v1/task/deploy/detail/container
     * 参数:无
     * ws参数:
     * @deployId   任务id
     * @tagString  当前节点
     * 返回:无
     * **/
    wsShell() {
      // const _this = this;
      // let tag_string = this.urlParam.fullTag;
      // let namespace = this.urlParam.namespace;
      // let pod_name = this.urlParam.podName;
      // let query = `?tag_string=${tag_string}&namespace=${namespace}&pod_name=${pod_name}`;
      // let url = `v1/container/terminal/ws${query}`;
      //   let loading; //初始化加载状态变量
      // this.shellWs = this.base.WS({
      //   url,
      //   isInit: true,
      //   openFn() {
      //     console.log("open");
      //   },
      //   messageFn(e) {
      //     console.log("message", e);
      //     if (e) {
      //       let data = JSON.parse(e.data);
      //       // 如果返回字符包含这些字符显示close提示
      //       if (data.Data == "\n" || data.Data == "\r\nexit\r\n") {
      //         alert("closed");
      //       }
      //       _this.term.write(data.Data);
      //       _this.showOrder = data.Data;
      //       _this.order = "";
      //     }
      //   },
      //   errorFn(e) {
      //     //出现错误关闭当前ws,并且提示
      //     console.log("error", e);
      //     _this.$message.error({
      //       message: "ws 请求失败,请刷新重试~",
      //       duration: 5000
      //     });
      //   }
      // });
    },

    onSend(data) {
      this.socket.emit('in', data)
      // data = this.base.isObject(data) ? JSON.stringify(data) : data;
      // data = this.base.isArray(data) ? data.toString() : data;
      // data = data.replace(/\\\\/, "\\");
      // this.shellWs.onSend(data);
    },

    //删除左右两端的空格
    trim(str) {
      return str.replace(/(^\s*)|(\s*$)/g, '')
    }
  }
}
</script>
<style lang="less" scoped>
#terminalContent {
  width: 100%;
  height: calc(100% - 56px);
  padding: 20px 25px;
  box-sizing: border-box;
  #terminal {
    width: 100%;
    height: 100%;
  }
}
</style>

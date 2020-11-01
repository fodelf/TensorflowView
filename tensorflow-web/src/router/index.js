/*
 * @Description:路由控制
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2019-06-05 18:57:53
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-07-23 10:28:14
 */
import Vue from 'vue'
import Router from 'vue-router'
import MainLayout from '@/views/layout/Layout.vue'
const Home = () => import('@/views/home/Home.vue')
const ProjectManage = () => import('@/views/projectManage/projectManage.vue')
const ProjectInit = () =>
  import('@/views/projectManage/projectInit/ProjectInit.vue')
import templateManage from '@/views/templateManage/templateManage.vue'
import componentManage from '@/views/componentManage/componentManage.vue'
import scriptManage from '@/views/scriptManage/ScriptManage.vue'
import ToDoComponent from '@/components/toDoComponent/ToDoComponent.vue'
// const TerminalView = () => import('components/terminal/TerminalView.vue')
Vue.use(Router)
const vueRouter = new Router({
  routes: [
    {
      path: '/',
      component: MainLayout,
      redirect: '/home',
      children: [
        {
          path: '/home',
          name: 'home',
          component: Home,
          meta: {
            title: '首页'
          }
        }
      ]
    },
    {
      path: '/project',
      name: 'project',
      redirect: '/project/projectManage',
      component: MainLayout,
      meta: {
        title: '服务管理'
      },
      children: [
        {
          path: 'projectManage',
          component: ProjectManage,
          name: 'projectManage',
          meta: {
            title: '服务列表'
          }
        },
        {
          path: 'projectInit',
          component: ProjectInit,
          name: 'projectInit',
          meta: {
            title: '服务初始化'
          }
        }
      ]
    },
    {
      path: '/template',
      name: 'template',
      redirect: '/template/templateManage',
      component: MainLayout,
      meta: {
        title: '模板管理'
      },
      children: [
        {
          path: 'templateManage',
          component: templateManage,
          name: 'templateManage',
          meta: {
            title: '模板列表'
          }
        }
      ]
    },
    {
      path: '/comp',
      name: 'comp',
      redirect: '/comp/componentManage',
      component: MainLayout,
      meta: {
        title: '组件管理'
      },
      children: [
        {
          path: 'componentManage',
          component: componentManage,
          name: 'componentManage',
          meta: {
            title: '组件列表'
          }
        }
      ]
    },
    {
      path: '/script',
      name: 'script',
      redirect: '/script/scriptManage',
      component: MainLayout,
      meta: {
        title: '脚本管理'
      },
      children: [
        {
          path: 'scriptManage',
          component: scriptManage,
          name: 'scriptManage',
          meta: {
            title: '脚本列表'
          }
        }
      ]
    },
    {
      path: '/tools',
      name: 'tools',
      redirect: '/tools/toolsManage',
      component: MainLayout,
      meta: {
        title: '工具管理'
      },
      children: [
        {
          path: 'toolsManage',
          component: ToDoComponent,
          name: 'toolsManage',
          meta: {
            title: '工具列表'
          }
        }
      ]
    },
    {
      path: '/drag',
      name: 'drag',
      redirect: '/drag/dragManage',
      component: MainLayout,
      meta: {
        title: '拖拽生成'
      },
      children: [
        {
          path: 'dragManage',
          component: ToDoComponent,
          name: 'dragManage',
          meta: {
            title: '拖拽'
          }
        }
      ]
    },
    {
      path: '/test',
      name: 'test',
      redirect: '/test/automatedTesting',
      component: MainLayout,
      meta: {
        title: '测试'
      },
      children: [
        {
          path: 'automatedTesting',
          component: ToDoComponent,
          name: 'automatedTesting',
          meta: {
            title: '自动化测试'
          }
        }
      ]
    },
    {
      path: '/devOps',
      name: 'devOps',
      redirect: '/devOps/Monitor',
      component: MainLayout,
      meta: {
        title: '运维监控'
      },
      children: [
        {
          path: 'Monitor',
          component: ToDoComponent,
          name: 'Monitor',
          meta: {
            title: '告警报错'
          }
        }
      ]
    },
    {
      path: '/system',
      name: 'system',
      redirect: '/system/systemManage',
      component: MainLayout,
      meta: {
        title: '系统'
      },
      children: [
        {
          path: 'systemManage',
          component: ToDoComponent,
          name: 'systemManage',
          meta: {
            title: '系统设置'
          }
        }
      ]
    }
  ]
})
// const routerPush = Router.prototype.push
// Router.prototype.push = function push(location) {
//   return routerPush.call(this, location).catch(error => error)
// }
// vueRouter.beforeEach(function (to, from, next) {
//   // const nextRoute = ['控制台', '仪表盘']
//   // const auth = localStorage.getItem('userId')
//   // // 跳转至上述3个页面
//   // if (nextRoute.indexOf(to.name) >= 0) {
//   //   // 未登录
//   //   if (!auth) {
//   //     vueRouter.push({ path: '/login' })
//   //   }
//   // }
//   // // 已登录的情况再去登录页，跳转至首页
//   // if (to.name === 'login') {
//   //   if (auth.IsLogin) {
//   //     vueRouter.push({ path: '' })
//   //   }
//   // }
//   next()
// })
export default vueRouter

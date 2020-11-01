/*
 * @Description:路由控制
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2019-06-05 18:57:53
 * @LastEditors: pym
 * @LastEditTime: 2020-09-06 21:47:43
 */
import Vue from 'vue'
import Router from 'vue-router'
import MainLayout from '@/views/layout/Layout.vue'
const Home = () => import('@/views/index/home/Home.vue')
const DataManage = () => import('@/views/index/dataManage/dataManage.vue')
const ProjectManage = () => import('@/views/index/projectManage/projectManage.vue')
const ProjectInit = () =>
  import('@/views/index/projectManage/projectInit/ProjectInit.vue')
const ProjectAdd = () =>  import('@/views/index/projectManage/projectAdd/projectAdd.vue')
import serviceSet from '@/views/index/systemManage/serviceSet/serviceSet.vue'

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
      path: '/data',
      name: 'data',
      redirect: '/data/dataManage',
      component: MainLayout,
      meta: {
        title: '服务管理'
      },
      children: [
        {
          path: 'dataManage',
          component: DataManage,
          name: 'dataManage',
          meta: {
            title: '数据源列表'
          }
        },
        {
          path: 'projectInit',
          component: ProjectInit,
          name: 'projectInit',
          meta: {
            title: '服务初始化'
          }
        },
        {
          path: 'projectAdd',
          component: ProjectAdd,
          name: 'projectAdd',
          meta: {
            title: '新增服务'
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
        },
        {
          path: 'projectAdd',
          component: ProjectAdd,
          name: 'projectAdd',
          meta: {
            title: '新增服务'
          }
        }
      ]
    },
    {
      path: '/system',
      name: 'system',
      redirect: '/system/serviceSet',
      component: MainLayout,
      meta: {
        title: '系统设置'
      },
      children: [
        {
          path: 'serviceSet',
          component: serviceSet,
          name: 'serviceSet',
          meta: {
            title: '服务设置'
          }
        }
      ]
    }
  ]
})
const routerPush = Router.prototype.push
Router.prototype.push = function push(location) {
  return routerPush.call(this, location).catch(error => error)
}
export default vueRouter

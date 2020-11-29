/*
 * @Description:路由控制
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2019-06-05 18:57:53
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-24 12:43:20
 */
import Vue from 'vue'
import Router from 'vue-router'
import MainLayout from '@/views/layout/Layout.vue'
const Home = () => import('@/views/index/home/Home.vue')
const DataManage = () => import('@/views/index/dataManage/dataManage.vue')
const ModelManage = () => import('@/views/index/modelManage/modelManage.vue')
const ModelAction = () => import('@/views/index/modelManage/modelAction/modelAction.vue')
const TrainManage = () => import('@/views/index/trainManage/trainManage.vue')
const ModelAdd = () =>  import('@/views/index/trainManage/trainAdd/trainAdd.vue')
// const ProjectInit = () =>
//   import('@/views/index/projectManage/projectInit/ProjectInit.vue')
// const ProjectAdd = () =>  import('@/views/index/projectManage/projectAdd/projectAdd.vue')
const DataAdd = () =>  import('@/views/index/dataManage/dataAdd/dataAdd.vue')
// import serviceSet from '@/views/index/systemManage/serviceSet/serviceSet.vue'

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
        title: '数据管理'
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
          path: 'dataAdd',
          component: DataAdd,
          name: 'dataAdd',
          meta: {
            title: '新增数据源'
          }
        }
      ]
    },
    {
      path: '/model',
      name: 'model',
      redirect: '/model/modelManage',
      component: MainLayout,
      meta: {
        title: '模型管理'
      },
      children: [
        {
          path: 'modelManage',
          component: ModelManage,
          name: 'modelManage',
          meta: {
            title: '模型列表'
          }
        },
        {
          path: 'modelAction',
          component: ModelAction,
          name: 'modelAction',
          meta: {
            title: '模型调用'
          }
        }
      ]
    },
    {
      path: '/train',
      name: 'train',
      redirect: '/train/trainManage',
      component: MainLayout,
      meta: {
        title: '训练管理'
      },
      children: [
        {
          path: 'trainManage',
          component: TrainManage,
          name: 'trainManage',
          meta: {
            title: '训练列表'
          }
        },
        {
          path: 'trainAdd',
          component: ModelAdd,
          name: 'trainAdd',
          meta: {
            title: '新增训练'
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

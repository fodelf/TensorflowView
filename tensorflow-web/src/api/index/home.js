/*
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-21 19:52:07
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-05-07 19:15:39
 */
import request from '@/utils/request'

export function getIndexCount() {
  return request({
    url: '/api/home/getIndexCount',
    method: 'GET',
  })
}

export function getTodoList() {
  return request({
    url: '/api/home/queryTodoList',
    method: 'GET',
  })
}

export function insertTask(params) {
  return request({
    url: '/api/home/insertTodoList',
    method: 'POST',
    params:params
  })
}
export function changeTodoList(params) {
  return request({
    url: '/api/home/changeTodoList',
    method: 'POST',
    params:params
  })
}

export function queryIndexTrend() {
  return request({
    url: '/api/home/queryIndexTrend',
    method: 'GET',
  })
}

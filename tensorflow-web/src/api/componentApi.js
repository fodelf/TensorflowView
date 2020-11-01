/*
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-04-16 21:24:45
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-04-16 21:52:51
 */
import request from '@/utils/request'

export function getCompSum(params) {
  return request({
    url: '/api/component/queryComponentSum',
    method: 'GET',
    params: params
  })
}
export function getComponentList(params) {
  return request({
    url: '/api/component/queryComponentList',
    method: 'GET',
    params: params
  })
}
export function insertComponent(params) {
  return request({
    url: '/api/component/insertComponent',
    method: 'POST',
    params: params
  })
}
export function deleteComponent(params) {
  return request({
    url: '/api/component/deleteComponent',
    method: 'POST',
    params: params
  })
}

export function updateComponent(params) {
  return request({
    url: '/api/component/updateComponent',
    method: 'POST',
    params: params
  })
}

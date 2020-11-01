/*
 * @Descripttion: 
 * @version: 
 * @Author: pym
 * @Date: 2020-09-06 21:00:45
 * @LastEditors: pym
 * @LastEditTime: 2020-09-06 21:16:14
 */
import request from '@/utils/request'

export function confirmConsul(params) {
  return request({
    url: '/uiApi/v1/system/editConsul',
    method: 'POST',
    params: params
  })
}
export function confirmMq(params) {
  return request({
    url: '/uiApi/v1/system/editRabbitMq',
    method: 'POST',
    params: params
  })
}
export function querySystemDetail() {
  return request({
    url: '/uiApi/v1/system/systemDetail',
    method: 'GET',
  })
}

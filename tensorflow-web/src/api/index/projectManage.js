/*
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-21 22:21:31
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-09-10 09:34:16
 */
import request from '@/utils/request'

export function getServiceSum() {
  return request({
    url: '/uiApi/v1/service/serviceSum',
    method: 'GET'
  })
}
export function getServiceList(params) {
  return request({
    url: '/uiApi/v1/service/serviceList',
    method: 'GET',
    params: params
  })
}
export function getServiceType() {
  return request({
    url: '/uiApi/v1/eumn/serverTypeList',
    method: 'GET',
  })
}
export function addService(params) {
  return request({
    url: '/uiApi/v1/service/addService',
    method: 'POST',
    params: params
  })
}
export function serviceDetail(id) {
  return request({
    url: `/uiApi/v1/service/serviceDetail?serverId=${id}`,
    method: 'GET'
  })
}
export function updateService(params) {
  return request({
    url: '/uiApi/v1/service/editService',
    method: 'POST',
    params: params
  })
}
export function deleteService(params) {
  return request({
    url: '/uiApi/v1/service/deleteService',
    method: 'POST',
    params: params
  })
}



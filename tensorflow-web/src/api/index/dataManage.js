/*
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-21 22:21:31
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-02 09:28:30
 */
import request from '@/utils/request'

export function getServiceList() {
  return request({
    url: '/uiApi/v1/service/serviceList',
    method: 'GET'
  })
}

export function getServiceList() {
  return request({
    url: '/uiApi/v1/service/serviceList',
    method: 'GET'
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



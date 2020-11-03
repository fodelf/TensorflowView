/*
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-21 22:21:31
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-03 20:34:47
 */
import request from '@/utils/request'

export function getDataType() {
  return request({
    url: '/api/v1/data/getDataType',
    method: 'GET'
  })
}

export function getDataList() {
  return request({
    url: '/api/v1/data/getDataList',
    method: 'GET'
  })
}
export function getServiceType() {
  return request({
    url: '/uiApi/v1/eumn/serverTypeList',
    method: 'GET',
  })
}
export function createData(params) {
  return request({
    url: '/api/v1/data/createData',
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
export function train(params) {
  return request({
    url: '/api/v1/data/train',
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



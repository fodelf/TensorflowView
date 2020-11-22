/*
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-21 22:21:31
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-18 19:43:02
 */
import request from '@/utils/request'

export function getDataType() {
  return request({
    url: '/api/v1/data/getDataType',
    method: 'GET'
  })
}
export function getDataSum() {
  return request({
    url: '/api/v1/data/getDataSum',
    method: 'GET'
  })
}
export function getDataList(params) {
  return request({
    url: '/api/v1/data/getDataList',
    method: 'GET',
    params: params
  })
}
export function getDataAll() {
  return request({
    url: '/api/v1/data/getDataAll',
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
export function queryTrainById(params) {
  return request({
    url: `/api/v1/data/queryTrainById`,
    method: 'POST',
    params: params
  })
}
export function parseHeader(params) {
  return request({
    url: '/api/v1/data/parseHeader',
    method: 'POST',
    params: params
  })
}



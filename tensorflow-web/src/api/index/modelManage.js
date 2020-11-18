/*
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-21 22:21:31
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-18 19:09:04
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
export function queryModelList(params) {
  return request({
    url: '/api/v1/model/queryModelList',
    method: 'GET',
    params:params
  })
}
export function save(params) {
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
export function getParam(params) {
  return request({
    url: '/api/v1/model/getParam',
    method: 'POST',
    params: params
  })
}
export function trainOnline(params) {
  return request({
    url: '/api/v1/model/trainOnline',
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
export function preTrain(params) {
  return request({
    url: '/api/v1/model/preTrain',
    method: 'POST',
    params: params
  })
}
export function saveModel(params) {
  return request({
    url: '/api/v1/model/saveModel',
    method: 'POST',
    params: params
  })
}

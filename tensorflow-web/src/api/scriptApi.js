/*
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-04-12 14:40:07
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-04-14 19:44:38
 */
import request from '@/utils/request'

export function insertScript(params) {
  return request({
    url: '/api/script/insertScript',
    method: 'POST',
    params: params
  })
}
export function queryScriptList(params) {
  return request({
    url: '/api/script/queryScriptList',
    method: 'GET',
    params: params
  })
}
export function actionScript(params) {
  return request({
    url: '/api/script/actionScript',
    method: 'POST',
    params: params
  })
}
export function deleteScript(params) {
  return request({
    url: '/api/script/deleteScript',
    method: 'POST',
    params: params
  })
}

export function updateScript(params) {
  return request({
    url: '/api/script/updateScript',
    method: 'POST',
    params: params
  })
}

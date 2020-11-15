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
    url: '/api/v1/home/getIndexCount',
    method: 'GET',
  })
}

export function queryIndexTrend() {
  return request({
    url: '/api/v1/home/getTrainCount',
    method: 'GET',
  })
}

export function getModel() {
  return request({
    url: '/api/v1/model/getModel',
    method: 'GET',
  })
}

export function queryMessage() {
  return request({
    url: '/api/v1/home/queryMessage',
    method: 'GET',
  })
}
export function queryMessageCount() {
  return request({
    url: '/api/v1/home/queryMessageCount',
    method: 'GET',
  })
}
export function updateMessage() {
  return request({
    url: '/api/v1/home/updateMessage',
    method: 'GET',
  })
}


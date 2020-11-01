/*
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-21 19:52:07
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-05-16 11:27:48
 */
import request from '@/utils/request'

export function queryToolsList() {
  return request({
    url: '/api/tool/queryToolsList',
    method: 'GET',
  })
}

/*
 * @Description: 描述
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2020-03-21 19:52:07
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-09-22 08:54:13
 */
import request from '@/utils/request'

export function getPersonActive() {
  return request({
    url: '/api/home/getPersonActive',
    method: 'GET',
  })
}

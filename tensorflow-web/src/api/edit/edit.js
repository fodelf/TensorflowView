/*
 * @Description:登陆模块请求
 * @Author: 吴文周
 * @Github: https://github.com/fodelf
 * @Date: 2019-06-05 17:27:29
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-05-11 14:26:22
 */
import request from '../../utils/request'

export function preview (params) {
  return request({
    url: '/api/drag/insertPage',
    method: 'POST',
    params: params
  })
}

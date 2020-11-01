/*
 * @Description: 描述
 * @Author: 吴文周
 * @Github: http://gitlab.yzf.net/wuwenzhou
 * @Date: 2020-07-23 19:46:07
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-07-23 20:37:27
 */
import request from '@/utils/request'
// 新增告警
export function insertWarning(params) {
  return request({
    url: '/api/warning/insertWarning',
    method: 'POST',
    params: params
  })
}
// 新增告警
export function queryWarningList() {
  return request({
    url: '/api/warning/queryWarningList',
    method: 'GET'
  })
}

'''
Description: 描述
Author: 吴文周
Github: http://gitlab.yzf.net/wuwenzhou
Date: 2020-11-18 19:22:43
LastEditors: 吴文周
LastEditTime: 2020-11-18 19:24:58
'''
from router.common import *
train = Blueprint('train', __name__)
@train.route('/queryTrainByTrainId')
def queryTrainByTrainId():
    data = request_parse(request)
    t = dataBase.queryTrainByTrainId(data)
    res = {
        'code': code,
        'msg': msg,
        'data':t
    }
    return jsonify(res)
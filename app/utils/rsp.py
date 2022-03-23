# -- coding: utf-8 --
# @Time : 2021/10/20 16:27
# @Author : 怃
# @Email : chenzhe12320@163.com
# @File : rsp.py
# @Project : Hq
# @Description : xxx

from typing import Union


# 简单定义返回
def resp_ok(code=1, msg="success", data: Union[list, dict, str] = None) -> dict:
    return {"code": code, "message": msg, "data": data}


def resp_fail(code=0, msg="fail", data: Union[list, dict, str] = None) -> dict:
    return {"code": code, "message": msg, "data": data}

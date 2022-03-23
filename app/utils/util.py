# -- coding: utf-8 --
# @Time : 2022/2/18 16:45
# @Author : 怃
# @Email : chenzhe12320@163.com
# @File : util.py
# @Project : Valentine
# @Description : xxx
import base64
import socket
import yaml
from functools import lru_cache
from datetime import datetime


def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


@lru_cache()
def read_yaml(path):
    with open(path, 'r', encoding='gbk') as f:
        data = yaml.load(f.read(), Loader=yaml.Loader)
        return data


def image2byte(path):
    with open(path, 'rb') as f:
        img_byte = base64.b64encode(f.read())
        return img_byte


def model_to_dict(obj, *ignore: list):
    if getattr(obj, '__table__', None) is None:
        return obj
    data = dict()
    for c in obj.__table__.columns:
        if c.name in list(*ignore):
            # 如果字段忽略, 则不进行转换
            continue
        val = getattr(obj, c.name)
        if isinstance(val, datetime):
            data[c.name] = val.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(val, bytes) and c.name == "avatar":
            data[c.name] = f'data:image/jpeg;base64,{val.decode()}'
        else:
            data[c.name] = val
    return data


if __name__ == '__main__':
    pass

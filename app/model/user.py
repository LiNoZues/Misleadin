# -- coding: utf-8 --
# @Time : 2022/2/18 16:54
# @Author : 怃
# @Email : chenzhe12320@163.com
# @File : user.py
# @Project : Valentine
# @Description : xxx
from pydantic import BaseModel


class UserLogin(BaseModel):
    username: str
    password: str

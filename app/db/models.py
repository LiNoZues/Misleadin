# -- coding: utf-8 --
# @Time : 2022/2/21 13:58
# @Author : 怃
# @Email : chenzhe12320@163.com
# @File : models.py
# @Project : Valentine
# @Description : xxx
from datetime import datetime

from sqlalchemy import Column, String, DATETIME, INT
from sqlalchemy.dialects.mysql import MEDIUMBLOB
from .database import Base
from app.utils.util import image2byte
from config import Config


class User(Base):
    __tablename__ = 'user'
    id = Column(INT, primary_key=True)
    created_at = Column(DATETIME, nullable=False)
    updated_at = Column(DATETIME, nullable=False)
    username = Column(String(16), unique=True, index=True, comment="账号")
    name = Column(String(16), index=True, comment="昵称")
    password = Column(String(32), unique=False)
    email = Column(String(64), unique=True, nullable=False, default="123456@789.com")
    role = Column(INT, default=0, comment="0: 普通用户 1: 组长 2: 超级管理员")
    last_login_at = Column(DATETIME)
    # MediumBlob 最大16M
    avatar = Column(MEDIUMBLOB, nullable=True, default=None, comment="头像图片二进制")

    # def to_dict(self):
    #     return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, account, password, role=0):
        self.username = account
        self.password = password
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.role = role
        self.name = account
        self.avatar = image2byte(Config.DEFAULT_AVATAR_DIR)
# -- coding: utf-8 --
# @Time : 2022/2/21 15:07
# @Author : 怃
# @Email : chenzhe12320@163.com
# @File : userDao.py
# @Project : Valentine
# @Description : xxx
from datetime import datetime

from loguru import logger as log
from config import Config
from app.middleware.Jwt import UserToken
from app.db.models import User

from sqlalchemy import func, select

from app.utils.ldap3 import ldap3_login


class UserDao:
    @staticmethod
    async def login(username, password,async_db):
        """
        :param async_db:
        :param username: 用户名
        :param password: 密码
        :return:
        """
        # 数据库存加盐后的密码
        salt_pwd = UserToken.add_salt(password)
        session = async_db
        # 连接数据库
        async with session.begin():
            query = await session.execute(
                select(User).where(User.username == username, User.password == salt_pwd)
            )
            user = query.scalars().first()
            if not user:
                rsp = ldap3_login(username, password)
                if not rsp:
                    raise Exception("用户名密码错误")
                else:
                    user = User(username, salt_pwd)
                    # 用户是配置的超级管理员
                    if username in Config.ADMIN_USERS:
                        user.role = Config.ADMIN
                    session.add(user)
            user.last_login_at = datetime.now()
            await session.flush()
            session.expunge(user) # 不加这一行在转化成dict的时候会报错  将对象从session中清除
            log.info(f"用户:{user.name}登录成功")
            return user

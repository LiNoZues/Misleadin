# -- coding: utf-8 --
# @Time : 2022/2/21 10:46
# @Author : 怃
# @Email : chenzhe12320@163.com
# @File : config.py
# @Project : Valentine
# @Description : xxx
import os
from urllib import parse
from app.utils.util import read_yaml
ENV = "DEV"


class BaseConfig(object):
    ROOT = os.path.dirname(os.path.abspath(__file__))
    STATIC_DIR = os.path.join(ROOT,"static")
    DEFAULT_AVATAR_DIR = os.path.join(STATIC_DIR,'default_avatar.png')
    CONF_DIR = os.path.join(ROOT,'config.yaml')
    LOG_DIR = os.path.join(ROOT, 'logs')
    LOG_FORMAT = '|<level>{level: <8}</level>| <green>{time:YYYY-MM-DD HH:mm:ss}</green>| <cyan>{name}</cyan>:<cyan>{' \
                 'function}</cyan>|line:{line}|<level>{message}</level> '

    # MySQL连接信息
    MYSQL_HOST = "121.36.217.176"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PWD = parse.quote_plus("123456")  # parse.quote_plus(pwd) 避免 密码中存在@符号
    DBNAME = "valentine"

    REDIS_HOST = "121.36.217.176"
    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_PASSWORD = "jxqgbzg.66"

    # Redis连接信息
    REDIS_NODES = [{"host": REDIS_HOST, "port": REDIS_PORT, "db": REDIS_DB, "password": REDIS_PASSWORD}]

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
        MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_PORT, DBNAME)

    # 异步URI
    ASYNC_SQLALCHEMY_URI = f'mysql+aiomysql://{MYSQL_USER}:{MYSQL_PWD}@{MYSQL_HOST}:{MYSQL_PORT}/{DBNAME}'

    # 权限 0 普通用户 1 组长 2 管理员
    MEMBER = 0
    MANAGER = 1
    ADMIN = 2

    ADMIN_USERS = read_yaml(CONF_DIR)['ADMIN']


class DevConfig(BaseConfig):
    pass


# 开发环境配置
class ProConfig(BaseConfig):
    pass


Config = DevConfig() if ENV == "DEV" else ProConfig()

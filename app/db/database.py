# -- coding: utf-8 --
# @Time : 2022/2/21 14:09
# @Author : 怃
# @Email : chenzhe12320@163.com
# @File : database.py
# @Project : Valentine
# @Description : xxx
from config import Config
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from loguru import logger as log

# 同步engine
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, pool_recycle=1500)
# 异步engine
async_engine = create_async_engine(Config.ASYNC_SQLALCHEMY_URI, pool_recycle=1500)
Session = sessionmaker(engine)

async_session = sessionmaker(async_engine, class_=AsyncSession, autocommit=False,
                             autoflush=False)

# 创建对象的基类:
Base = declarative_base()





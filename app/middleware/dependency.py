# -- coding: utf-8 --
# @Time : 2022/2/22 10:35
# @Author : 怃
# @Email : chenzhe12320@163.com
# @File : dependency.py
# @Project : Valentine
# @Description : xxx
from app.db.database import async_session


async def get_async_db_session():
    async with async_session() as session:
        yield session

# -- coding: utf-8 --
# @Time : 2022/2/21 11:12
# @Author : 怃
# @Email : chenzhe12320@163.com
# @File : user.py
# @Project : Valentine
# @Description : xxx

from fastapi import APIRouter, Depends
from app.model.user import UserLogin
from app.db.crud.user.userDao import UserDao
from app.middleware.Jwt import UserToken
from app.middleware.dependency import get_async_db_session
from app.utils.rsp import resp_ok, resp_fail
from sqlalchemy.ext.asyncio import AsyncSession
import traceback
from app.utils.util import model_to_dict

from loguru import logger as log

router = APIRouter(
    prefix='/v1/user',
    tags=['user']
)


@router.post('/login', description="登录接口")
async def login(user: UserLogin, async_db: AsyncSession = Depends(get_async_db_session)):
    try:
        log.info(user)
        user = await UserDao.login(**user.dict(), async_db=async_db)
        user = model_to_dict(user, ['password', 'id'])
        token = UserToken.get_token(user)
        return resp_ok(msg="登录成功", data=dict(token=token, userInfo=user))
    except Exception as e:
        return resp_fail(msg=f"登录失败,{str(e)}")


@router.get("/test")
async def funtion_test():
    return resp_ok(msg="测试")

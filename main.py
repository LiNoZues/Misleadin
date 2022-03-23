# -- coding: utf-8 --
# @Time : 2022/2/16 14:43
# @Author : 怃
# @Email : chenzhe12320@163.com
# @File : main.py
# @Project : Valentine
# @Description : xxx

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.utils.util import get_host_ip
from app.api import user
from app.db.database import Base,engine
from app import loginit
from config import Config
loginit()
Base.metadata.create_all(engine)

valentine_app = FastAPI()
origins = [
        "*",
    ]
valentine_app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)
valentine_app.mount("/static", StaticFiles(directory=Config.STATIC_DIR), name="static")
valentine_app.include_router(user.router)
if __name__ == '__main__':
    uvicorn.run("main:valentine_app", reload=True, host=get_host_ip(), port=3000,access_log=True)

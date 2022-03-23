# -- coding: utf-8 --
# @Time : 2022/2/21 11:01
# @Author : 怃
# @Email : chenzhe12320@163.com
# @File : __init__.py.py
# @Project : Valentine
# @Description : xxx
import logging
from loguru import logger
import sys
from app.utils.custom_log import InterceptHandler, format_record
from config import Config


def loginit():
    logging.getLogger().handlers = [InterceptHandler()]
    logger.configure(
        handlers=[{"sink": sys.stdout, "level": logging.DEBUG, "format": format_record}])
    logger.add(f'{Config.LOG_DIR}/DEBUG.log', rotation="20 MB", compression="zip", enqueue=True, retention="5 days",
               backtrace=True, diagnose=True, level="DEBUG",
               format=Config.LOG_FORMAT)
    logger.add(f'{Config.LOG_DIR}/WARNING.log', rotation="20 MB", compression="zip", enqueue=True, retention="5 days",
               backtrace=True, diagnose=True, level="WARNING",
               format=Config.LOG_FORMAT)
    logger.add(f'{Config.LOG_DIR}/ERROR.log', rotation="10 MB", compression="zip", enqueue=True, retention="5 days",
               backtrace=True, diagnose=True, level="ERROR",
               format=Config.LOG_FORMAT)
    logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]

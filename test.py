# -- coding: utf-8 --
# @Time : 2022/2/18 16:33
# @Author : 怃
# @Email : chenzhe12320@163.com
# @File : test.py
# @Project : Valentine
# @Description : xxx

import asyncio


async def test():
    await asyncio.sleep(2)
    print("sleep")


loop = asyncio.get_event_loop()
loop.run_until_complete( asyncio.wait([test(), test()]))
loop.close()
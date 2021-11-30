# -*- coding:utf-8 -*-
# !/usr/bin/env python
# @Author  :PolarBear
# @DES     :任务调度模块，定时存储sqlite,处理前端请求
# @DATE    :2021.11.17

from apscheduler.schedulers.background import BlockingScheduler
from datetime import datetime
import subprocess,time,os
from SystemInfo import SysInfo as sys_info
from SystemInfo import get_pro


scheduler = BlockingScheduler()
# Save SystemInfo
def func_info():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sys_info(flag=True)
    print(now)
# Save ProgressInfo
def func_pro():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    get_pro('test1')
    print(now)

if __name__ == '__main__':
    # scheduler.add_job(func,'interval',seconds=2)
    # while 1:
    #     scheduler.start()

    #scheduler.add_job(func, 'cron', hour=11, minute=20)
    scheduler.add_job(func_info, 'interval', seconds=5)
    # scheduler.add_job(func_pro,'interval',seconds=3)
    # print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        ...

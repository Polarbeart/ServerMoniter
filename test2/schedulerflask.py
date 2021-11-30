# -*- coding:utf-8 -*-
# !/usr/bin/env python
# @Author  :PolarBear
# @DES     :任务调度模块，定时存储sqlite,处理前端请求
# @DATE    :2021.11.17


from flask import Flask
from flask_apscheduler import APScheduler
import datetime


class Config(object):
    SCHEDULER_API_ENABLED = True


scheduler = APScheduler()


# interval examples
@scheduler.task('interval', id='do_job_1', seconds=3, misfire_grace_time=900)
def job1():
    print(str(datetime.datetime.now()) + ' Job 1 executed')

#
# # cron examples
# @scheduler.task('cron', id='do_job_2', minute='*')
# def job2():
#     print(str(datetime.datetime.now()) + ' Job 2 executed')
#
#
# @scheduler.task('cron', id='do_job_3', week='*', day_of_week='sun')
# def job3():
#     print(str(datetime.datetime.now()) + ' Job 3 executed')
#
#
# @scheduler.task('cron', id='do_job_3', day='*', hour='13', minute='26', second='05')
# def job4():
#     print(str(datetime.datetime.now()) + ' Job 4 executed')


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(Config())

    # it is also possible to enable the API directly
    # scheduler.api_enabled = True
    scheduler.init_app(app)
    scheduler.start()

    app.run(port=8000)
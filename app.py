# -*- coding:utf-8 -*-
# !/usr/bin/env python
# @Author  :PolarBear
# @DES     :Flask执行文件
# @DATE    :2021.11.11

from flask import Flask, render_template, jsonify,request
import time
from datetime import datetime
from test2.strdraw import logo
# from sqlitedb.sqlitedb import sqlClass
from oracledb.oralce4 import oracleOperation
from SystemInfo import SysInfo as sys_info
from SystemInfo import get_pro
from apscheduler.schedulers.background import BlockingScheduler

scheduler = BlockingScheduler()
sql = oracleOperation()
app = Flask(__name__)

#####################
ip_sub = None      ##更换的IP提交
list_value = None  ##检测是否点击提交按钮
#####################




@app.route('/')
def helloworld():
    cates =[]
    ip = get_txt_ip()
    sql1 = "select distinct ip from systeminfo "
    res = sql.define_self(sql1)
    # cates = ['192.168','192.169','192.172','192.171','test1']
    for i in res:
        print(i[0])
        cates.append(i[0])
    sql2 = "select PRONAME,MEMUSED,STATE,TIME,PORT from progress where ip ='192.168.43.81'"
    print(sql2)
    res2 = sql.define_self(sql2)
    content = res2
    print(cates)

    list_value = request.values.get("list_value")
    print("下拉选择值"+str(list_value))
    if list_value != None:
        cates.remove(list_value)
        cates.insert(0,list_value)
        with open('select.txt','w')as f:
            f.write(list_value)
    else:
        ...
    return render_template('main.html',content = content,cates = cates)
    # return render_template('main.html')

@app.route("/c1")
def get_c1_data():
    data = [1,1,1,1]
    ip_sub = get_txt_ip()
    if ip_sub != None:
        sql_c1 = "select * from (select cpuUsed,memoryUsed from SYSTEMINFO where ip = '"+ip_sub+"' order by tim desc) where rownum <2 "
        res = sql.define_self(sql_c1)

        for i in res:
            print(i[0])
            # i[1] =round(i[1],2)
            # print(i[1])
            data = [i[0],i[1],21,0.4]
    return jsonify({"confirm":data[0],"suspect":data[1],"heal":data[2],"dead":data[3]})

@app.route('/c2')
def get_c2_data():
    data= ['conhost.exe','0.0528','running','2021-11-13 10:45:51']
    #return jsonify({"process":data[0],"memory":data[1],"state":data[2],"create":data[3]})
    return jsonify({'data1': {"confirm":data[1],"suspect":data[1],"heal":data[2],"dead":data[3]},'data2':{"confirm":data[0],"suspect":data[1],"heal":data[2],"dead":data[3]}})


@app.route('/l1')
def get_l1_data():
    percent,time = [],[]
    ip_sub = get_txt_ip()
    if ip_sub !=None:
        sql_l1 = "select * from (select cpuused,time from SYSTEMINFO where ip = '"+ip_sub+"' order by tim desc) where rownum <37 order by time asc"
        res = sql.define_self(sql_l1)
        # print(res[0])
        # if res[0]:
        for i in res:
            percent.append(str(i[0]))
            # tim = timeStamp(i[1])
            time.append(i[1])

    else:
        print("数据库中没有该表！！")
        ...


    return jsonify({"time": time,"percent": percent})


@app.route('/l2')
def get_l2_data():
    percent, time = [], []
    ip_sub  = get_txt_ip()
    if ip_sub !=None:
        sql_l2 = "select * from (select memoryUsed,time from SYSTEMINFO where ip = '" + ip_sub + "' order by tim desc) where rownum <37 order by time asc"
        res = sql.define_self(sql_l2)
        # print("l2 的值"+str(res[0]))
        # if res[0]:
        for i in res:
            percent.append(str(i[0]))
            # tim = timeStamp((i[-1]))
            time.append(i[1])

    return jsonify({"time": time,"percent": percent})



@app.route('/r1')
def get_r1_data():
    realTimeSent, realTimeRcvd,time = [], [],[]
    # sql_l1 = "select ip,realTimeRcvd,realTimeSent,tim from SYSTEMINFO where ip = 'test1' limit 5"
    ip_sub = get_txt_ip()
    if ip_sub !=None:

        sql_r1 = "select * from (select realTimeRcvd,realTimeSent,time from SYSTEMINFO where ip = '" + ip_sub + "' order by tim desc) where rownum <37 order by time asc"

        res = sql.define_self(sql_r1)
        # if res[0]:
        for i in res:
            realTimeRcvd.append(i[0])
            realTimeSent.append(i[1])
            # tim = timeStamp((i[-1]))
            time.append(i[-1])

    return jsonify({"realTimeSent":realTimeSent,"realTimeRcvd":realTimeRcvd,"time": time})



@app.route("/r2")
def get_r2_data():
    d= [20,50,30]

    return jsonify({"value1": d[0],"value2": d[1],"value3":d[2]})


@app.route("/list")
def get_list_data():
    # option = request.getParameter("selector")
    # selector = request.form.get('selector')
    cate_id = request.form.get('value')
    hobby_list = request.form.getlist("list_value")

    list_value = request.values.get("list_value")

    # print("下拉选择值"+str(value))
    return jsonify({"select":list_value})

# 读取txt,获取提交保存的ip
def get_txt_ip():
    with open('select.txt','r')as f:
        ip_sub = f.read()
        print("读取得到的ip值为"+ip_sub)
        return ip_sub


# Save SystemInfo
def func_info():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sys_info(flag=False)
    print(now)
# Save ProgressInfo
def func_pro():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    get_pro('test1')
    print(now)


 # 输入毫秒级的时间，转出正常格式的时间
def timeStamp(timeNum):
    timeStamp = float(timeNum / 1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%H:%M:%S", timeArray)
    print(otherStyleTime)
    return otherStyleTime

if __name__ == '__main__':
    # logo()
    # app.config.from_object(Config())
    # tim = time.time()
    # print(tim)
    # timeStamp(tim)
    app.run(debug=True)





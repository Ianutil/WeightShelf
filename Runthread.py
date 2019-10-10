#!/usr/bin/python
# -*- coding: UTF-8 
# author: Ian
# Please,you must believe yourself who can do it beautifully !
"""
Are you OK?
"""

from PyQt5 import QtCore
import threading

# SERVICE_URL = "http://10.10.10.4:5000"
SERVICE_URL = "https://sss.bailianic.com"

# 继承QThread
class Runthread(QtCore.QThread):
    # python3,pyqt5与之前的版本有些不一样
    #  通过类成员对象定义信号对象
    _signal = QtCore.pyqtSignal(dict)

    def __init__(self, parent=None):
        super(Runthread, self).__init__()

    def __del__(self):
        self.wait()


    def setRequest(self, req):
        self.req = req

    def run(self):
        try:

            time = QtCore.QDateTime.currentDateTime()
            text = "开始时间：{0} 线程# {1}".format(time.toString("yyyy-MM-dd hh:mm:ss"), threading.current_thread().name)



            time = QtCore.QDateTime.currentDateTime()
            print("结束时间：", time.toString("yyyy-MM-dd hh:mm:ss"))

            print("---------->",self.req)

            self.callback(self.req)
            self._signal.emit(self.req);  # 可以在这里写信号焕发

        except Exception as e:
            data = {}
            self.callback(data)
            self._signal.emit(data);  # 可以在这里写信号焕发

            print(e)

    def callback(self, data):
        # print(threading.current_thread().name)
        self._signal.emit(data);  # 可以在这里写信号焕发


if __name__ == "__main__":
    print("Hello World")
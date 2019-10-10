#!/usr/bin/python
# -*- coding: UTF-8 
# author: Ian
# Please,you must believe yourself who can do it beautifully !
"""
Are you OK?
"""

from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import requests
import DeviceManager
import SceneStyleSheet

class WeightResetScene(QtWidgets.QWidget):
    def __init__(self):
        super(WeightResetScene, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("稳重校验器")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        desktop = QtWidgets.QApplication.desktop()
        # 获取显示器分辨率大小
        self.screenRect = desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()

        # self.width = 960
        # self.height = 640
        print("Screen Size#", self.width, "x", self.height)
        self.setFixedSize(self.width, self.height)
        self.resize(self.height, self.height)

        self.setStyleSheet('''
                                                  QWidget{
                                                  border:none;
                                                  margin-bottom:0px;
                                                  margin-left:0px;
                                                  margin-top:0px;
                                                  margin-right:0px;
                                                  padding:0px;
                                                  }
                                              ''')

        self.createMain()
        DeviceManager.startDevice(scene=self)

    def createMain(self):
        # 创建窗口主部件
        self.main_widget = QtWidgets.QWidget(self)
        self.main_widget.setFixedSize(self.width, self.height)
        print(self.main_widget.width(), "x", self.main_widget.height())

        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)
        self.main_widget.setStyleSheet('''
                                          QWidget{
                                          background-color:black;
                                          border:none;
                                          margin-bottom:0px;
                                          margin-left:0px;
                                          margin-top:0px;
                                          margin-right:0px;
                                          padding:0px;
                                          }
                                      ''')

        self.setScene()
        self.setStyleScene()
        self.scene_style_sheet = SceneStyleSheet.SceneStyleSheet()
        self.scene_style_sheet.setFixedSize(self.width, self.height)
        self.scene_style_sheet.initUI()
        self.scene_style_sheet.show()
        # 行号，列号，行宽，列宽
        self.main_layout.addWidget(self.scene_widget, 0, 0, 1, 1)

        # 行号，列号，行宽，列宽
        self.main_layout.addWidget(self.style_widget, 0, 0, 1, 1)
        self.main_layout.addWidget(self.scene_style_sheet, 0, 0, 1, 1)
        self.style_widget.setVisible(False)

    def setScene(self):
        self.scene_widget = QtWidgets.QWidget(self)
        self.scene_layout = QtWidgets.QGridLayout()
        self.scene_widget.setLayout(self.scene_layout)
        self.background_label = QtWidgets.QLabel()
        self.scene_layout.addWidget(self.background_label, 0, 0, 1, 1)
        # url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1564554481205&di=ce95a7ca24ab3636db04fb923d0166b4&imgtype=0&src=http%3A%2F%2Fd.hiphotos.baidu.com%2Fimage%2Fpic%2Fitem%2F0b7b02087bf40ad1719cf19f592c11dfa9ecce55.jpg"
        # self.showInternetImage(url, self.label)
        image = QtGui.QPixmap("./resource/bg.jpg")
        image = image.scaled(self.width, self.height , QtCore.Qt.KeepAspectRatio)
        # self.background_label.setPixmap(image)

    def setStyleScene(self):
        self.style_widget = QtWidgets.QWidget(self)
        self.style_layout = QtWidgets.QGridLayout()
        self.style_widget.setLayout(self.style_layout)

        self.left_widget = QtWidgets.QWidget(self)
        # self.left_widget.setFixedSize(self.width, self.height)
        self.left_layout = QtWidgets.QGridLayout()
        self.left_widget.setLayout(self.left_layout)
        self.style_layout.addWidget(self.left_widget, 0, 0, 1, 1)

        self.item_image_label = QtWidgets.QLabel()
        self.left_layout.addWidget(self.item_image_label, 0, 0, 1, 1, QtCore.Qt.AlignTop|QtCore.Qt.AlignLeft)
        image = QtGui.QPixmap("./resource/farmer-water.jpeg")
        image = image.scaled(self.width/3 * 2 ,self.height - 45, QtCore.Qt.KeepAspectRatio)
        # image = image.scaledToHeight(self.left_widget.height(), QtCore.Qt.FastTransformation)
        self.item_image_label.setPixmap(image)
        styleSheet = '''
                                          QWidget{
                                          background-color:white;
                                          border:none;
                                          margin-bottom:0px;
                                          margin-left:0px;
                                          margin-top:0px;
                                          margin-right:0px;
                                          padding:0px;
                                          font-size:24px;
                                          font-weight:700;
                                          font-family:"Helvetica Neue", Helvetica, Arial, sans-serif;
                                          color:red;
                                          }
                                      '''
        self.right_wight = QtWidgets.QWidget()
        self.right_layout = QtWidgets.QGridLayout()
        self.right_wight.setLayout(self.right_layout)
        self.style_layout.addWidget(self.right_wight, 0, 1, 1, 1)
        self.right_wight.setStyleSheet(styleSheet)
        self.item_name_label = QtWidgets.QLabel("农夫山泉")
        self.right_layout.addWidget(self.item_name_label, 0, 0, 1, 1, QtCore.Qt.AlignTop|QtCore.Qt.AlignLeft)
        self.item_name_label.setStyleSheet(styleSheet)

        self.item_value_label = QtWidgets.QLabel("数量：1")
        self.right_layout.addWidget(self.item_value_label, 1, 0, 1, 1, QtCore.Qt.AlignTop|QtCore.Qt.AlignLeft)
        self.item_value_label.setStyleSheet(styleSheet)

        move_label = QtWidgets.QLabel("")
        self.right_layout.addWidget(move_label, 2, 0, 8, 1, QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.item_value_label.setStyleSheet(styleSheet)

    def keyPressEvent(self, keyEvent):
        print(keyEvent.key(), chr(81))
        if keyEvent.key() == 81:
            self.close()

    def showInternetImage(self, url, widget):
        try:
            req = requests.get(url)
            image = QtGui.QPixmap()
            image.loadFromData(req.content)
            widget.setScaledContents(True)
            widget.setPixmap(image)
        except Exception as e:
            print(e)

    def updateScene(self, data):
        print("updateScene#",   data)
        self.style_widget.setVisible(True)
        self.scene_style_sheet.updateScene(data)

        if not data:
            self.item_image_label.setPixmap(None)
            self.item_name_label.setText("加载失败")
            self.item_value_label.setText("")
            return
        if data["item_id"] == 4:
            item_url = "./resource/farmer-water.jpeg"
            item_name = "农夫山泉"
        elif data["item_id"] == 5:
            item_url = "./resource/mai-move.jpg"
            item_name = "脉动"
        else:
            item_url = "./resource/farmer-water.jpeg"
            item_name = "农夫山泉"

        image = QtGui.QPixmap(item_url)
        image = image.scaled(self.width / 3 * 2, self.height - 45, QtCore.Qt.KeepAspectRatio)
        # image = image.scaledToHeight(self.left_widget.height(), QtCore.Qt.FastTransformation)
        self.item_image_label.setPixmap(image)

        self.item_name_label.setText("商品："+item_name)
        self.item_value_label.setText("数量：{0}".format(data["quantity"]))

def startApp():
    app = QtWidgets.QApplication(sys.argv)
    window = WeightResetScene()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    print("Hello World")

    startApp()

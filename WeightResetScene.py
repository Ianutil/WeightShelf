#!/usr/bin/python
# -*- coding: UTF-8 
# author: Ian
# Please,you must believe yourself who can do it beautifully !
"""
Are you OK?
"""

from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import WeightShelfReset


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
        # self.height = self.screenRect.height()
        # self.width = self.screenRect.width()

        self.width = 960
        self.height = 640
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

    def createMain(self):
        # 创建窗口主部件
        self.main_widget = QtWidgets.QWidget(self)
        self.main_widget.setFixedSize(self.width, self.height)
        print(self.main_widget.width(), "x", self.main_widget.height())

        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)
        self.main_widget.setStyleSheet('''
                                          QWidget{
                                          background-color:white;
                                          border:none;
                                          margin-bottom:0px;
                                          margin-left:0px;
                                          margin-top:0px;
                                          margin-right:0px;
                                          padding:0px;
                                          }
                                      ''')

        self.createWeight()
        self.createBottom()

        # 行号，列号，行宽，列宽
        self.main_layout.addWidget(self.weight_widget, 0, 0, 2, 1)
        self.main_layout.addWidget(self.bottom_widget, 2, 0, 2, 1)

    def createWeight(self):
        self.weight_widget = QtWidgets.QWidget()
        print(self.weight_widget.width(), "x", self.weight_widget.height())
        self.weight_widget.setFixedSize(self.width - 50, self.height / 9 * 8 - 50)
        print("createWeight#", self.weight_widget.width(), "x", self.weight_widget.height())
        self.weight_layout = QtWidgets.QGridLayout()
        self.weight_widget.setLayout(self.weight_layout)
        self.weight_widget.setStyleSheet('''
                                                  QWidget{
                                                  border:none;
                                                  margin-bottom:0px;
                                                  margin-left:0px;
                                                  margin-top:0px;
                                                  margin-right:0px;
                                                  padding:0px;
                                                  }
                                              ''')

        index = 0
        for i in range(0, 8):
            row_widget = QtWidgets.QWidget()
            row_layout = QtWidgets.QGridLayout()
            row_widget.setFixedSize(self.weight_widget.width() - 50, self.weight_widget.height() / 8)
            row_widget.setLayout(row_layout)
            row_widget.setStyleSheet('''
     QWidget{
     border:none;
     margin-bottom:0px;
     margin-left:0px;
     margin-top:0px;
     margin-right:0px;
     padding:0px;
     }
 ''')

            self.weight_layout.addWidget(row_widget, i, 0, 1, 1)

            for j in range(0, 8):
                index += 1
                cell_widget = QtWidgets.QWidget()
                cell_layout = QtWidgets.QGridLayout()
                cell_widget.setLayout(cell_layout)
                row_layout.addWidget(cell_widget, i, j, 1, 1)
                cell_widget.setStyleSheet('''
                     QWidget{
                     border:none;
                     background-color:#EEEEEE;
                     margin-bottom:0px;
                     margin-left:0px;
                     margin-top:0px;
                     margin-right:0px;
                     padding:0px;
                     }
                 ''')

                name = QtWidgets.QLabel("稳重{0}".format(index))
                name.setObjectName("weight_name_{0}".format(index))
                cell_layout.addWidget(name, 0, 0, 1, 1)
                name.setStyleSheet('''
                                     QWidget{
                                     border:2px;
                                     margin-bottom:0px;
                                     margin-left:0px;
                                     margin-top:0px;
                                     margin-right:0px;
                                     padding:0px;
                                     font-size:12px;
                                     color:#666666;
                               
                                     }
                                 ''')

                value = QtWidgets.QLabel("0")
                value.setObjectName("weight_value_{0}".format(index))
                cell_layout.addWidget(value, 0, 1, 1, 3, QtCore.Qt.AlignRight)
                value.setStyleSheet('''
                     QWidget{
                     border:2px;
                     margin-bottom:0px;
                     margin-left:0px;
                     margin-top:0px;
                     margin-right:0px;
                     padding:0px;
                     color:#333333;
                     font-style:bold;
                     }
                 ''')

    def createBottom(self):
        self.bottom_widget = QtWidgets.QWidget()
        print(self.bottom_widget.width(), "x", self.bottom_widget.height())
        self.bottom_widget.setFixedSize(self.width - 50, self.height / 9 * 1)
        print(self.bottom_widget.width(), "x", self.bottom_widget.height())
        self.bottom_layout = QtWidgets.QGridLayout()
        self.bottom_widget.setLayout(self.bottom_layout)
        self.bottom_widget.setStyleSheet('''
                                             QWidget{
                                             border:none;
                                             background-color:#EEEEEE;
                                             }
                                         ''')

        texts = ["上一页", "称号：0", "砝码", "清零", "退出", "下一页"]
        for i in range(0, len(texts)):
            button = QtWidgets.QPushButton(texts[i])
            self.bottom_layout.addWidget(button, 0, i, 1, 1, QtCore.Qt.AlignVCenter)
            button.setObjectName("button_{0}".format(i+1))
            button.setStyleSheet('''
                                     QWidget{
                                     border:10px;
                                     border-color:#999999;
                                     padding-left:5px;
                                     padding-right:5px;
                                     padding-top:3px;
                                     padding-bottom:3px;
                                     font-size:16px;
                                     color:#666666;
                                     }
                                 ''')

        # button = self.bottom_layout.findChild(QtWidgets.QPushButton, "button_1")
        # button.clicked.connect(lambda: self.onClick(button))
        # button = self.bottom_layout.findChild(QtWidgets.QPushButton, "button_2")
        # button.clicked.connect(lambda: self.onClick(button))
        # button = self.bottom_layout.findChild(QtWidgets.QPushButton, "button_3")
        # button.clicked.connect(lambda: self.onClick(button))
        # button = self.bottom_layout.findChild(QtWidgets.QPushButton, "button_4")
        # button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        # button = self.bottom_layout.findChild(QtWidgets.QPushButton, "button_5")
        # button.clicked.connect(lambda: self.onClick(button))

    def onClick(self, tag):

        print("onClick#"+tag)


def startApp():
    app = QtWidgets.QApplication(sys.argv)
    window = WeightResetScene()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    print("Hello World")

    startApp()

#!/usr/bin/python
# -*- coding: UTF-8 
# author: Ian
# Please,you must believe yourself who can do it beautifully !
"""
Are you OK?
"""

from PyQt5 import QtWidgets, QtCore, QtGui, QtMultimedia, QtMultimediaWidgets
import sys

Video_URL = ["http://edge.ivideo.sina.com.cn/145667727.mp4?KID=sina,viask&Expires=1565280000&ssig=BB5Mjy85no",
             ]

class SceneStyleSheet(QtWidgets.QWidget):
    def __init__(self):
        super(SceneStyleSheet, self).__init__()
        print("SceneStyleSheet#w={0} h={1}".format(self.width(), self.height()))
        # self.initUI()
        # self.show()

    def initUI(self):
        print("SceneStyleSheet#w={0} h={1}".format(self.width(), self.height()))

        self.scene_main_layout = QtWidgets.QGridLayout()
        self.setLayout(self.scene_main_layout)

        self.setStyleSheet('''
                     QWidget{
                     background-color:transparent;
                     background-image: linear-gradient(-45deg, #383C53 0%, #1C1F2E 100%);
                     border:none;
                     margin:0px;
                     padding:0px;
                     }
                 ''')


        self.left_widght = QtWidgets.QWidget()
        self.left_layout = QtWidgets.QGridLayout()
        self.left_widght.setLayout(self.left_layout)
        self.left_layout.setContentsMargins(0, 0, 0, 0)

        self.middle_widght = QtWidgets.QWidget()
        self.middle_layout = QtWidgets.QGridLayout()
        self.middle_widght.setLayout(self.middle_layout)
        self.middle_layout.setContentsMargins(18, 0, 0, 0)


        self.right_widght = QtWidgets.QWidget()
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widght.setLayout(self.right_layout)
        self.right_layout.setContentsMargins(30, 0, 0, 0)

        move = QtWidgets.QLabel("")
        move.setFixedSize(30, 20)
        self.scene_main_layout.addWidget(move, 0, 0, 1, 1, QtCore.Qt.AlignCenter)
        self.scene_main_layout.addWidget(self.left_widght, 0, 1, 1, 1)

        move = QtWidgets.QLabel("")
        move.setFixedSize(30, 20)
        self.scene_main_layout.addWidget(move, 0, 2, 1, 1, QtCore.Qt.AlignCenter)

        self.scene_main_layout.addWidget(self.middle_widght, 0, 3, 1, 1)
        move = QtWidgets.QLabel("")
        move.setFixedSize(30, 20)
        self.scene_main_layout.addWidget(move, 0, 4, 1, 1, QtCore.Qt.AlignCenter)

        self.scene_main_layout.addWidget(self.right_widght, 0, 5, 1, 1)
        move = QtWidgets.QLabel("")
        move.setFixedSize(30, 20)
        self.scene_main_layout.addWidget(move, 0, 6, 1, 1, QtCore.Qt.AlignCenter)

        self.left_widght.setFixedSize(780 ,960)
        self.middle_widght.setFixedSize(540 ,960)
        self.right_widght.setFixedSize(360 ,960)

        self.initCSS()

        # self.setLeftWidget()
        self.setMiddleWidget()
        self.setRightWidget()
        self.setSelectedGoods()

        print("right_widght#", self.left_widght.width(), self.left_widght.height())
        print("middle_widght#", self.middle_widght.width(), self.middle_widght.height())
        print("right_widght#", self.right_widght.width(), self.right_widght.height())
    def setLeftWidget(self):

        self.left_media_label = QtWidgets.QLabel("左边")
        self.left_media_label.setStyleSheet('''
                                          QWidget{
                                          background-color:#3f7fFfFF;
                                          font-size:24px;
                                          font-weight:700;
                                          font-family:"Helvetica Neue", Helvetica, Arial, sans-serif;
                                          color:red;
                                          }
                                      ''')
        image = QtGui.QPixmap("./resource/mai-move.jpg")
        image = image.scaled(self.left_widght.width(), self.height(), QtCore.Qt.KeepAspectRatio)
        self.left_media_label.setPixmap(image)
        self.left_layout.addWidget(self.left_media_label, 0, 0, 1, 1, QtCore.Qt.AlignCenter)

        video_url = Video_URL[0]
        self.player = QtMultimedia.QMediaPlayer()
        self.player_widget = QtMultimediaWidgets.QVideoWidget()
        self.player_widget.setFixedSize(self.width()/2, self.height())
        self.left_layout.addWidget(self.player_widget, 0, 0, 1, 1, QtCore.Qt.AlignCenter)
        self.player.setVideoOutput(self.player_widget)
        # self.player.setMedia(QtMultimedia.QMediaContent(QtWidgets.QFileDialog.getOpenFileUrl()[0]))
        # self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile("/Users/ianchang/Downloads/dance.mp4")))
        # self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(video_url)))

        self.playlist = QtMultimedia.QMediaPlaylist()
        self.playlist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile("/Users/ianchang/Public/Git/Git_Hub/tf-openpose/etcs/dance.mp4")))
        self.playlist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile("/Users/ianchang/Public/opencv-master/doc/js_tutorials/js_assets/cup.mp4")))
        self.playlist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile("/Users/ianchang/Public/2018-08-06/ScreenTest/MI/123.mp4")))
        self.playlist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile("/Users/ianchang/Public/2017-11-23/BAD8015AC2CE8184FD6451F7F856755B.mp4")))
        self.playlist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile("/Users/ianchang/Public/Git/Git_Hub/cross/samples/Test_JS/Resources/image/abc.mp4")))
        self.playlist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(video_url)))
        self.playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.CurrentItemInLoop)
        self.playlist.setCurrentIndex(0)
        self.player.setPlaylist(self.playlist)
        self.player.play()

    def setMiddleWidget(self):
        middle_sytle_sheet = '''
                     QWidget#title_label{
                     font-family: Alibaba-PuHuiTi-R;
                     font-size: 36px;
                     color: #6B4108;
                     text-align: justify;
                     line-height: 30px;
                     margin-left:30px;
                     margin-top:30px;
                     }
                                      '''
        title_label = QtWidgets.QLabel("热销排行榜")
        title_label.setObjectName("title_label")
        title_label.setStyleSheet(middle_sytle_sheet)

        self.middle_layout.addWidget(title_label, 0, 0, 1, 1)

        title_icon = QtWidgets.QLabel("热销排行榜")
        image = QtGui.QPixmap("./resource/line.png")
        image = image.scaled(38, 35, QtCore.Qt.KeepAspectRatio)
        title_icon.setPixmap(image)
        self.middle_layout.addWidget(title_icon, 0, 1, 1, 2)

        title_icon.setStyleSheet('''
                QWidget{
                margin-top:30px;
                }
        ''')

        for i in range(0, 5):
            item_widget = QtWidgets.QWidget()
            item_widget.setObjectName("item_widget")
            item_layout = QtWidgets.QGridLayout()
            item_widget.setLayout(item_layout)
            item_layout.setContentsMargins(0, 0, 15, 0)
            self.middle_layout.addWidget(item_widget, 1+i, 0, 1, 3)
            item_widget.setFixedSize(500, 200)
            item_widget.setStyleSheet('''
                QWidget{
                    background-color:white;
                    margin:30px;
                    border-radius:15px;
                }
            ''')
            item_image = QtWidgets.QLabel()
            item_layout.addWidget(item_image, 0, 0, 10, 2)
            # item_image.setFixedSize(100, 100)
            image = QtGui.QPixmap("./resource/tin.png")
            image = image.scaled(70, 100, QtCore.Qt.KeepAspectRatio)
            item_image.setPixmap(image)
            item_image.setAlignment(QtCore.Qt.AlignCenter)
            item_image.setStyleSheet('''
                            QWidget{
                                margin-left:15px;
                                padding-left:15px;
                            }
                        ''')

            item_name = QtWidgets.QLabel("脉动脉动脉动脉动脉动脉动脉动脉动脉动")
            item_layout.addWidget(item_name, 1, 1, 5, 4, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
            item_name.setStyleSheet('''
                     QWidget{
                     font-family: Alibaba-PuHuiTi-R;
                     font-size: 28px;
                     color: #3B3B3B;
                     padding-left:8px;
                     }
                 ''')

            item_count = QtWidgets.QLabel("剩余{0}瓶".format(i+5))
            item_layout.addWidget(item_count, 3, 1, 5, 4, QtCore.Qt.AlignLeft)
            item_count.setObjectName("item_count")
            item_count.setStyleSheet('''
                                 QWidget{
                                 font-family: Alibaba-PuHuiTi-R;
                                 font-size: 24px;
                                 color: #8F8F8F;
                                 padding-left:8px;
                                 text-align: justify;
                                 }
                                                  ''')


            item_grade = QtWidgets.QLabel()
            item_layout.addWidget(item_grade, 2, 16, 6, 3)
            if i < 3:
                image = QtGui.QPixmap("./resource/triumph-0{0}".format(i+1))
                image = image.scaled(42, 42, QtCore.Qt.KeepAspectRatio)
                item_grade.setPixmap(image)
            else:
                item_grade.setText(str(i+1))
            item_grade.setStyleSheet('''
                QWidget{
                font-family: Impact, Alibaba-PuHuiTi-R;
                font-size: 36px;
                color: #E0CFA5;
                text-align: justify;
                }
            ''')
        move = QtWidgets.QLabel("")
        move.setFixedSize(10, 100)
        self.middle_layout.addWidget(move, 6, 0, 2, 3)

    def setRightWidget(self):
        title_label = QtWidgets.QLabel("为你推荐")
        title_label.setObjectName("title_label")
        title_label.setStyleSheet('''
                             QWidget#title_label{
                             font-family: Alibaba-PuHuiTi-R;
                             font-size: 36px;
                             color: #FFFFFF;
                             text-align: justify;
                             margin-left:0px;
                             }
                                              ''')

        self.right_layout.addWidget(title_label, 0, 0, 1, 3)

        for i in range(0, 8):
            item_widget = QtWidgets.QWidget()
            item_widget.setObjectName("item_widget")
            item_layout = QtWidgets.QGridLayout()
            item_widget.setLayout(item_layout)
            item_layout.setContentsMargins(0, 0, 30 ,0)
            self.right_layout.addWidget(item_widget, 1 + i, 0, 1, 3)
            item_widget.setStyleSheet('''
                        QWidget{
                            margin-top:15px;
                        }
                    ''')
            item_image = QtWidgets.QLabel()
            item_image.setFixedSize(80, 100)
            item_layout.addWidget(item_image, 0, 0, 2, 2)
            image = QtGui.QPixmap("./resource/tin.png")
            image = image.scaled(80, 100, QtCore.Qt.KeepAspectRatio)
            item_image.setPixmap(image)
            item_image.setAlignment(QtCore.Qt.AlignCenter)
            item_image.setStyleSheet('''
                                    QWidget{
                                        background-color:white;
                                        padding-top:5px;
                                        padding-bottom:5px;
                                        padding-left:5px;
                                        padding-right:5px;
                                        border-radius:8px;
                                    }
                                ''')

            item_name = QtWidgets.QLabel("可口可乐350可口可乐350可口可乐350可口可乐350可口可乐350")
            item_layout.addWidget(item_name, 0, 2, 2, 6, QtCore.Qt.AlignLeft)
            item_name.setStyleSheet('''
                             QWidget{
                             font-family: Alibaba-PuHuiTi-R;
                             font-size: 24px;
                             color: #F5F5F5;
                             margin-left:15px;
                             }
                         ''')
        move = QtWidgets.QLabel("")
        move.setFixedSize(10, 50)
        self.right_layout.addWidget(move, 9, 0, 1, 3)



    def keyPressEvent(self, keyEvent):

        if keyEvent.key() == 81:
            self.close()
            return

        count = self.playlist.mediaCount()
        index = self.playlist.currentIndex()
        volume = self.player.volume()

        if keyEvent.key() == 16777236:
            # 向右，播放下一个
            next_index = index + 1

            if next_index >= count:
                next_index = 0

            self.playlist.setCurrentIndex(next_index)
        elif keyEvent.key() == 16777234:
            # 向左，向生播上一个
            next_index = index - 1

            if next_index < 0:
                next_index = count - 1

            self.playlist.setCurrentIndex(next_index)
        elif keyEvent.key() == 16777235:
            # 向上，声音放大
            up_volume = volume +1

            if up_volume > 100:
                up_volume = 100

            self.player.setVolume(up_volume)

        elif keyEvent.key() == 16777237:
            # 向下，声音变小
            down_volume = volume - 1

            if down_volume < 00:
                down_volume = 0

            self.player.setVolume(down_volume)

    def initCSS(self):
        self.left_widght.setObjectName("left_widght")
        self.left_widght.setStyleSheet('''
                                QWidget#left_widght{
                                    background-color:black;
                                    margin-left:0px;
                                    margin-right:0px;
                                    margin-top:0px;
                                    margin-bottom:0px;
                                }
                        ''')

        self.middle_widght.setObjectName("middle_widght")
        self.middle_widght.setStyleSheet('''
                        QWidget#middle_widght{
                            background-image:url("./resource/BG_phb.png");
                            background-repeat:no-repeat;
                            margin-left:0px;
                            margin-right:0px;
                            margin-top:0px;
                            margin-bottom:0px;
                        }
                ''')

        self.right_widght.setObjectName("right_widght")
        self.right_widght.setStyleSheet('''
                                QWidget#right_widght{
                                    background-image:url("./resource/BG_tj.png");
                                    background-repeat:no-repeat;
                                    margin-left:0px;
                                    margin-right:0px;
                                    margin-top:0px;
                                    margin-bottom:0px;
                                }
                        ''')

    def setSelectedGoods(self):
        self.left_item_widght = QtWidgets.QWidget()
        self.left_item_layout = QtWidgets.QGridLayout()
        self.left_item_widght.setLayout(self.left_item_layout)
        self.left_layout.addWidget(self.left_item_widght, 0, 0, 1, 1)
        self.left_item_layout.setContentsMargins(0,0, 0, 0)
        self.left_layout.setContentsMargins(0,0, 0, 0)
        self.left_item_widght.setObjectName("left_item_widght_border")
        self.left_item_widght.setStyleSheet('''
                                        QWidget#left_item_widght_border{
                                            background-color:white;
                                            border-width:0px;
                                            border-radius:8px;
                                        }
                                ''')

        left_top_widght = QtWidgets.QWidget()
        left_top_layout = QtWidgets.QGridLayout()
        left_top_widght.setLayout(left_top_layout)
        self.left_item_layout.addWidget(left_top_widght, 0, 0, 10, 1)
        left_top_widght.setStyleSheet('''
                             QWidget{
                                 background-color:#F2F2F2;
                               }
                            ''')

        left_bottom_widght = QtWidgets.QWidget()
        left_bottom_layout = QtWidgets.QGridLayout()
        left_bottom_widght.setLayout(left_bottom_layout)
        self.left_item_layout.addWidget(left_bottom_widght, 9, 0, 2, 1)
        left_bottom_widght.setStyleSheet('''
                     QWidget{
                         background-color:#E9E9E9;
                       }
                    ''')

        self.left_item_image = QtWidgets.QLabel()
        left_top_layout.addWidget(self.left_item_image, 0, 0, 3, 8, QtCore.Qt.AlignCenter)
        image = QtGui.QPixmap("./resource/bottle.png")
        image = image.scaled(780, 780, QtCore.Qt.KeepAspectRatio)
        self.left_item_image.setPixmap(image)

        # 右边商品详细
        item_detail_widget = QtWidgets.QWidget()
        item_detail_layout = QtWidgets.QGridLayout()
        item_detail_layout.setContentsMargins(0, 0, 0, 0)
        item_detail_widget.setLayout(item_detail_layout)
        left_top_layout.addWidget(item_detail_widget, 1, 7, 1, 3)
        item_detail_widget.setObjectName("item_detail_widget")
        item_detail_widget.setStyleSheet('''
                             QWidget#item_detail_widget{
                                 background-color:#7751E2;
                                 padding:0px;
                                 margin:0px;
                                 border-radius:8px;
                               }
                            ''')

        self.left_item_category = QtWidgets.QLabel("矿物质泉水")
        item_detail_layout.addWidget(self.left_item_category, 0, 0, 1, 1, QtCore.Qt.AlignTop|QtCore.Qt.AlignHCenter)
        self.left_item_category.setStyleSheet('''
                     QWidget{
                         padding:0px;
                         margin-top:30px;
                         font-family: Alibaba-PuHuiTi-R;
                         font-size: 24px;
                         color: #FFFFFF;
                         text-align: justify;
                         background-color:#00000000;
                       }
                    ''')

        item_detail_01_widget = QtWidgets.QWidget()
        item_detail_01_layout = QtWidgets.QGridLayout()
        item_detail_01_layout.setContentsMargins(0, 0, 0, 0)
        item_detail_01_widget.setLayout(item_detail_01_layout)
        item_detail_01_widget.setMinimumWidth(250)
        item_detail_01_widget.setMinimumHeight(250)
        item_detail_layout.addWidget(item_detail_01_widget, 1, 0, 4, 1)
        item_detail_01_widget.setStyleSheet('''
                     QWidget{
                        background-color:#FFFFFF;
                        margin-top:15px;
                        padding-top:15px;
                       }
                    ''')


        small_style_sheet = '''
        QWidget{
        opacity: 0.4;
        font-family: Alibaba-PuHuiTi-R;
        font-size: 16px;
        color: #999999;
        margin-top:-10px;
        text-align: justify;
        }
        '''
        big_style_sheet = '''
        QWidget{
        opacity: 0.4;
        font-family: Alibaba-PuHuiTi-R;
        font-size: 18px;
        color: #666666;
        text-align: justify;
        }
        '''
        move = QtWidgets.QLabel("")
        move.setFixedSize(10, 20)
        item_detail_01_layout.addWidget(move, 0, 0, 1, 1, QtCore.Qt.AlignCenter)
        self.left_item_category_01 = QtWidgets.QLabel("强劲气泡")
        item_detail_01_layout.addWidget(self.left_item_category_01, 1, 0, 1, 1, QtCore.Qt.AlignCenter)
        self.left_item_category_02 = QtWidgets.QLabel("源自天然")
        item_detail_01_layout.addWidget(self.left_item_category_02, 2, 0, 1, 1, QtCore.Qt.AlignCenter)
        self.left_item_category_03 = QtWidgets.QLabel("强劲绵密")
        item_detail_01_layout.addWidget(self.left_item_category_03, 3, 0, 1, 1, QtCore.Qt.AlignCenter)
        self.left_item_category_04 = QtWidgets.QLabel("0卡无糖")
        item_detail_01_layout.addWidget(self.left_item_category_04, 4, 0, 1, 1, QtCore.Qt.AlignCenter)
        self.left_item_category_01.setStyleSheet(big_style_sheet)
        self.left_item_category_02.setStyleSheet(small_style_sheet)
        self.left_item_category_03.setStyleSheet(big_style_sheet)
        self.left_item_category_04.setStyleSheet(small_style_sheet)

        move = QtWidgets.QLabel("")
        item_detail_01_layout.addWidget(move, 5, 0, 1, 1, QtCore.Qt.AlignCenter)

        bottom_bg = QtWidgets.QLabel()
        left_bottom_layout.addWidget(bottom_bg, 1, 0, 1, 1)
        bottom_bg.setStyleSheet('''
             QWidget{
                 background-color:#E9E9E9;
               }
            ''')

        self.left_item_name = QtWidgets.QLabel("农夫山泉    550ml");
        left_bottom_layout.addWidget(self.left_item_name, 1, 2, 1, 8)
        self.left_item_name.setStyleSheet('''
             QWidget{
                 font-family: Alibaba-PuHuiTi-R;
                 font-size: 36px;
                 color: #2B2E3E;
                 text-align: justify;
               }
            ''')
        self.left_item_count = QtWidgets.QLabel("仅剩3瓶");
        left_bottom_layout.addWidget(self.left_item_count, 2, 2, 1, 8)
        self.left_item_count.setStyleSheet('''
             QWidget{
                 opacity: 0.4;
                 font-family: Alibaba-PuHuiTi-R;
                 font-size: 30px;
                 color: #7f2B2E3E;
                 text-align: justify;
               }
            ''')

    def updateScene(self, data):
        if not data:
            self.left_item_image.setPixmap(None)
            self.left_item_image.setText("加载失败")
            self.left_item_image.setText("")
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
        image = image.scaled(780, 780, QtCore.Qt.KeepAspectRatio)
        self.left_item_image.setPixmap(image)

        self.left_item_name.setText(item_name)
        self.left_item_count.setText("仅剩{0}瓶".format(data["quantity"]))


if __name__ == "__main__":
    print("Hello World")
    app = QtWidgets.QApplication(sys.argv)
    window = SceneStyleSheet()
    window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    # window.setFixedSize(900, 640)
    window.setFixedSize(1920, 1080)
    window.initUI()
    window.show()
    sys.exit(app.exec_())

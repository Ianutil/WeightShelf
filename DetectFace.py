#!/usr/bin/python
# -*- coding: UTF-8 
# author: Ian
# Please,you must believe yourself who can do it beautifully !
"""
Are you OK?
"""

import cv2
import time
import base64
import Runthread

# 一次最大上传图像数
UPDATE_FACE_COUNT = 5
# 上传时间间隔
UPDATE_FACE_INTERVAL = 10

class DetectFace(object):

    def __init__(self):
        super().__init__()
        self.initCamera()

        self.start_time = time.time()
        self.isStartUploadFace = False
        self.isUploadFace = False
        self.encode_faces = []

    def initCamera(self):
        # 摄像机
        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH,480)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT,320)

        # 确保此xml文件与该py文件在一个文件夹下，否则将这里改为绝对路径
        file = r"/Users/ianchang/Public/2017-11-07/OpenCVForAndroid-opencv3.2.0/OpenCVLibrary320/build/intermediates/bundles/debug/res/raw/haarcascade_frontalface_default.xml"
        self.classifier = cv2.CascadeClassifier(file)


    def startApp(self):

        while True:
            ret, frame = self.camera.read()

            if ret == False: return

            # 变换彩色空间顺序
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            size = frame.shape[:2]
            divisor = 4
            h, w = size
            minSize = (w // divisor, h // divisor)
            # gray: 进行检测的图像, 这里是转换后的。
            # scaleFactor: 官网文档说是每次图片缩小的比例, 其实可以这么理解, 距离相机不同的距离, 物体大小是不一样的, 在物体大小不一致的情况下识别一个东西是不方便的, 这就需要进行多次的缩放, 这就是这个参数的作用。
            # minNeighbors: 可以理解为每次检测时, 对检测点(Scale)周边多少有效点同时检测, 因为可能选取的检测点大小不足而导致遗漏。
            # minSize: 检测点的最小值, 或者说就是检测点的最终值
            faceRects = self.classifier.detectMultiScale(gray, 1.2, 2, cv2.CASCADE_SCALE_IMAGE, minSize)

            # 绘制人脸
            for faceRect in faceRects:
                x, y, w, h = faceRect
                # 上传人脸信息
                self.collectFace(frame, faceRect)

                cv2.rectangle(frame, (x, y), (x + h, y + w), (0, 255, 0), 2)

            cv2.imshow("Camera", frame)

            if cv2.waitKey(120) & 0xff == ord('q'):
                cv2.imwrite("./resource/face.jpg", frame)
                cv2.destroyAllWindows()
                break

    def collectFace(self, frame, rect):
        x, y, w, h = rect

        # 上传的服务器
        face_array = frame[y - 10: y + h + 10, x - 10: x + w + 10]

        current_time = time.time()
        # 增加5张待上传的采集图像
        if self.isStartUploadFace and len(self.encode_faces) < UPDATE_FACE_COUNT:
            # 只有不在上传图像状态下，才判断是否到了该上传图像的时刻
            self.start_time = current_time

            byte_image = face_array.tobytes()
            byte_image = base64.b64encode(byte_image)
            byte_image = str(byte_image, 'utf-8')
            shape = str(face_array.shape[0]) + ',' + str(face_array.shape[1]) + ',' + str(
                face_array.shape[2])
            self.encode_faces.append({"data": byte_image, "shape": shape})
            print("收集的人脸的个数#",len(self.encode_faces))
            # 每隔6秒上传一次图片
        elif current_time - self.start_time > UPDATE_FACE_INTERVAL:
            # 只有不在上传图像状态下，才判断是否到了该上传图像的时刻了
            self.start_time = current_time
            # 开始采集图像标志
            self.isStartUploadFace = True
            self.isUploadFace = False
            self.encode_faces.clear()
            print("开始上传", self.start_time)

        # 收集到5张人脸后，上传到服务器，进行识别
        if len(self.encode_faces) >= UPDATE_FACE_COUNT and self.isUploadFace == False:
            # 关闭采集图像标志
            self.isStartUploadFace = False
            self.isUploadFace = True

            req = {"store_id": "s6001", "device_id": "b001", "faces": self.encode_faces}
            print("上传成功")
            # 开始上传到服务器
            # self.thread = Runthread.Runthread()
            # self.thread.setRequest(req)
            # self.thread._signal.connect(self.updateFace)
            # self.thread.start()

if __name__ == "__main__":
    print("Hello World")

    detect = DetectFace()
    detect.startApp()
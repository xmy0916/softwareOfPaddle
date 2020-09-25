import threading
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2
from paddledetectionThread import DetectionThread
from paddlesegThread import SegThread


class OpenCameraThread(object):
    isRunning = True
    image = None
    def __init__(self,cameraType,mode,srcLabel,dstLabel,showImg):
        '''
        :param cameraType:0-本地相机；1-USB协议相机；2-Gige协议相机
        :param srcLabel:原图显示的label
        :param dstLabel:结果显示的label
        '''
        self.cameraType = cameraType
        self.mode = mode
        self.srcLabel = srcLabel
        self.dstLabel = dstLabel
        self.showImg = showImg
        self.detect = DetectionThread()
        self.seg = SegThread()
        self.cameraThread = threading.Thread(target=self.openCameraThread)
        self.segThread = threading.Thread(target=self.segPredectThread)
        self.detectThread = threading.Thread(target=self.detectPredictThread)
        self.cameraThread.start()
        if self.mode == 0:
            self.segThread.start()
        elif self.mode == 1:
            self.detectThread.start()
        print("打开相机初始化成功")

    def openCameraThread(self):
        # 本地相机
        if self.cameraType == 0:
            cap = cv2.VideoCapture(0)
            while OpenCameraThread.isRunning:
                ret, img = cap.read()
                if img is None:
                    continue
                OpenCameraThread.image = img.copy() # OpenCameraThread.image给别的线程处理预测等
                self.showImg(img,self.srcLabel)
            cap.release()
            cv2.destroyAllWindows()
            OpenCameraThread.isRunning = False
            print("实时摄像头进程关闭")
        # usb相机
        elif self.cameraType == 1:
            cap = cv2.VideoCapture(1)
            while OpenCameraThread.isRunning:
                ret, img = cap.read()
                if img is None:
                    continue
                OpenCameraThread.image = img.copy() # OpenCameraThread.image给别的线程处理预测等
                self.showImg(img,self.srcLabel)
            cap.release()
            cv2.destroyAllWindows()
            OpenCameraThread.isRunning = False
            print("实时摄像头进程关闭")
        elif self.cameraType == 2:
            """
            gige相机驱动程序
            """
            pass


    def segPredectThread(self):
        while OpenCameraThread.isRunning:
            if OpenCameraThread.image is None:
                continue
            segResult = self.seg.segOnePicture(OpenCameraThread.image)
            self.showImg(segResult, self.dstLabel)
        print("seg进程关闭")

    def detectPredictThread(self):
        while OpenCameraThread.isRunning:
            if OpenCameraThread.image is None:
                continue
            segResult = self.detect.detectOnePicture(OpenCameraThread.image)
            self.showImg(segResult, self.dstLabel)
        print("detect进程关闭")


    def stop(self):
        OpenCameraThread.isRunning = False



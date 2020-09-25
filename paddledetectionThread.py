import threading
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2


class DetectionThread(object):
    def __init__(self):
        pass

    def detectOnePicture(self,img):
        """
        :param img:
        :return: 目标检测结果
        """
        return img
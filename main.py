import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QMessageBox
import mainUI
from openCameraThread import OpenCameraThread
from paddledetectionThread import DetectionThread
import cv2
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainCode(QMainWindow, mainUI.MainUi):
    def __init__(self):
        QMainWindow.__init__(self)
        mainUI.MainUi.__init__(self)
        # 槽函数
        self.left_button_2.clicked.connect(self.openLocalCameraThread)
        self.left_button_1.clicked.connect(self.openUSBCameraThread)
        self.left_button_3.clicked.connect(self.openGigeCameraThread)
        self.left_close.clicked.connect(self.closeApp)
        self.button_choose_model_dir.clicked.connect(self.getDir)


    def openLocalCameraThread(self):
        self.sourceImage_label.setText("加载视屏中......")
        with open("./connfig.txt","r") as config:
            mode = int(config.readline())
            self.openCameraThread = OpenCameraThread(0,mode, self.sourceImage_label,self.resultImage_label,self.showImg)


    def openUSBCameraThread(self):
        self.sourceImage_label.setText("加载视屏中......")
        with open("./connfig.txt","r") as config:
            mode = int(config.readline())
            self.openCameraThread = OpenCameraThread(1,mode, self.sourceImage_label,self.resultImage_label,self.showImg)


    def openGigeCameraThread(self):
        self.sourceImage_label.setText("加载视屏中......")
        with open("./connfig.txt", "r") as config:
            mode = int(config.readline())
            self.openCameraThread = OpenCameraThread(2, mode, self.sourceImage_label, self.resultImage_label,
                                                     self.showImg)



    def showImg(self,img,label):
        res = self.img_resize(img, label)
        img2 = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)  # opencv读取的bgr格式图片转换成rgb格式
        _image = QtGui.QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3,
                              QtGui.QImage.Format_RGB888)  # pyqt5转换成自己能放的图片格式
        jpg_out = QtGui.QPixmap(_image)  # 转换成QPixmap
        label.setPixmap(jpg_out)  # 设置图片显示
        label.setAlignment(Qt.AlignCenter)


    def img_resize(self,image,label):
        '''
        :param image: cv2读取的mat图片
        :param label: 显示在那个label
        :return: 返回处理后适合显示的图片
        '''
        if image is None:
            return
        height, width = image.shape[0], image.shape[1]
        # 设置新的图片分辨率框架
        width_new = label.width()
        height_new = label.height()
        # 判断图片的长宽比率
        if width / height >= width_new / height_new:
            img_new = cv2.resize(image, (width_new, int(height * width_new / width)))
        else:
            img_new = cv2.resize(image, (int(width * height_new / height), height_new))
        return img_new


    def closeApp(self):
        try:
            self.openCameraThread.stop()
            self.close()
        except:
            self.close()


    def getDir(self):
        _dir = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        if len(_dir) != 0:
            if self.is_chinese(_dir):
                print("有中文")
                QMessageBox.warning(self, '警告', '暂不支持含有中文的路径')
                return
            else:
                self.dir_lineedit.setText(_dir)

    def is_chinese(self,string):
        """
        检查整个字符串是否包含中文
        :param string: 需要检查的字符串
        :return: bool
        """
        for ch in string:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True

        return False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = MainCode()
    md.show()
    sys.exit(app.exec_())
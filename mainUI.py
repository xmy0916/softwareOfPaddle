# coding:utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
import qtawesome
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication,QFileDialog,QMessageBox,QSlider,QComboBox
import os

class MainUi(object):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setFixedSize(960, 700)

        self.init_config()
        self.init_button()
        self.init_label()
        # self.init_toolBar()
        self.init_widget()

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.main_layout.setSpacing(0) # 去缝

    def init_button(self):
        self.left_close = QtWidgets.QPushButton("×")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("一")  # 最小化按钮

        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.film', color='white'), "usb相机")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.file-image-o', color='white'), "本地视频")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.picture-o', color='white'), "gige相机")
        self.left_button_3.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "反馈建议")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "关注我们")
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "遇到问题")
        self.left_button_9.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")

        self.left_mini.clicked.connect(self.showMinimized)
        self.sure.clicked.connect(self.writeConfig)

    def init_label(self):
        self.left_label_1 = QtWidgets.QPushButton("相机种类")
        self.left_label_1.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("联系与帮助")
        self.left_label_3.setObjectName('left_label')

        self.sourceImage_label = QtWidgets.QLabel()
        self.sourceImage_label.setObjectName('sourceImageLabel')
        self.sourceImage_label.setFixedSize(400,400)
        self.sourceImage_label.setStyleSheet("border:1px solid black")

        self.resultImage_label = QtWidgets.QLabel()
        self.resultImage_label.setObjectName("resultImageLabel")
        self.resultImage_label.setFixedSize(400,400)
        self.resultImage_label.setStyleSheet("border:1px solid black")

    def init_widget(self):
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占12行2列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占12行列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_layout.addWidget(self.left_mini, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

        self.right_layout.addWidget(self.sourceImage_label, 0, 0, 1, 7)
        self.right_layout.addWidget(self.resultImage_label, 0, 11, 1, 7)

        self.right_layout.addWidget(self.combo, 1, 0, 1, 3)
        self.right_layout.addWidget(self.checkBoxLabel,1, 3, 1, 2)
        self.right_layout.addWidget(self.checkBox, 1, 5, 1, 1)

        self.right_layout.addWidget(self.button_choose_model_dir,1, 6, 1, 3)
        self.right_layout.addWidget(self.dir_lineedit, 1, 9, 1, 5)

        self.right_layout.addWidget(self.inputSize_label,1, 14, 1, 2)
        self.right_layout.addWidget(self.size_lineedit, 1, 16, 1, 5)
        self.right_layout.addWidget(self.sure,1,21,1,1)

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
            QWidget#left_widget{
                background:gray;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
        ''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

    # def init_toolBar(self):
    #     self.sld = QSlider(Qt.Horizontal, self)
    #     self.sld.setFocusPolicy(Qt.NoFocus)
    #     self.sld.setGeometry(30, 40, 100, 30)

    def init_config(self):
        self.combo = QtWidgets.QComboBox(self)
        self.combo.addItem("图像分割")
        self.combo.addItem("目标检测")
        self.combo.addItem("图片分类")

        self.checkBoxLabel = QtWidgets.QLabel("使用GPU:")
        self.checkBoxLabel.setAlignment(Qt.AlignCenter)
        self.checkBox = QtWidgets.QCheckBox(self)

        self.button_choose_model_dir = QtWidgets.QPushButton("选择模型路径")
        self.dir_lineedit = QtWidgets.QLineEdit("")

        self.inputSize_label = QtWidgets.QLabel("输入大小:")
        self.inputSize_label.setAlignment(Qt.AlignCenter)
        self.size_lineedit = QtWidgets.QLineEdit("")
        self.size_lineedit.setPlaceholderText("例如：400 500")

        self.sure = QtWidgets.QPushButton("确定")

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.RightButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()


    def closeApp(self):
        app = QApplication.instance()
        # 退出应用程序
        app.quit()


    def writeConfig(self):
        if os.path.exists("./connfig.txt"):
            os.remove("./connfig.txt")

        with open("./connfig.txt","w") as config:
            config.write(str(self.combo.currentIndex()) + "\n")
            if self.checkBox.checkState() == Qt.Checked:
                config.write("1\n")
            else:
                config.write("0\n")

            config.write(self.dir_lineedit.text() + "\n")
            config.write(self.size_lineedit.text() + "\n")
            QMessageBox.about(self, '提示', '配置保存成功')


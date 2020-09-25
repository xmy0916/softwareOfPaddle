import threading
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2
import importlib
import numpy as np
from utils.palette import get_palette
from PIL import Image as PILImage
import paddle.fluid as fluid


class SegThread(object):
    def __init__(self):
        self.cfg = getattr(importlib.import_module('paddleseg.configs.paddleseg'), 'cfg')
        # 使用GPU
        place = fluid.CUDAPlace(0) if int(self.cfg.gpu) == 1 else fluid.CPUPlace()
        self.exe= fluid.Executor(place)

        # 加载预测模型
        self.test_prog, self.feed_name, self.fetch_list = fluid.io.load_inference_model(
            dirname=self.cfg.model_path, executor=self.exe, params_filename='__params__')


    def segOnePicture(self,img):
        palette = get_palette(self.cfg.class_num)
        # 数据获取
        ori_img = img  # 用来处理的图
        image = self.preprocess(ori_img)
        im_shape = ori_img.shape[:2]

        # 模型预测
        result = self.exe.run(program=self.test_prog, feed={self.feed_name[0]: image}, fetch_list=self.fetch_list,
                              return_numpy=True)
        parsing = np.argmax(result[0][0], axis=0)
        parsing = cv2.resize(parsing.astype(np.uint8), im_shape[::-1])

        # 预测结果
        output_im = PILImage.fromarray(np.asarray(parsing, dtype=np.uint8))
        output_im.putpalette(palette)
        res = cv2.cvtColor(np.asarray(output_im) * 255, cv2.COLOR_RGB2BGR)  # PIL转cv
        return res


    def preprocess(self, img):
        # 图像预处理
        img = cv2.resize(img, self.cfg.input_size).astype(np.float32)
        img -= np.array(self.cfg.MEAN)
        img /= np.array(self.cfg.STD)
        img = img.transpose((2, 0, 1))
        img = np.expand_dims(img, axis=0)
        return img

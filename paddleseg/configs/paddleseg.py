# -*- coding: utf-8 -*-
from utils.util import AttrDict, merge_cfg_from_args, get_arguments
import os
import sys
sys.path.append("softwareOfPaddleDetection/")

args = get_arguments()
cfg = AttrDict()
with open("connfig.txt","r") as cof:
    reader = cof.readlines()
    reader = [line.rstrip("\n") for line in reader]
    cfg.gpu = int(reader[1])

    # 模型加载路径
    cfg.model_path = reader[2]

    # 预测类别数
    cfg.class_num = 19
    # 均值, 图像预处理减去的均值
    cfg.MEAN = 127.5, 127.5, 127.5
    # 标准差，图像预处理除以标准差
    cfg.STD =  127.5, 127.5, 127.5
    # 待预测图像输入尺寸

    cfg.input_size = int(reader[3].split(" ")[0]),int(reader[3].split(" ")[1])


merge_cfg_from_args(args, cfg)

# -*- coding: utf-8 -*-
from utils.util import AttrDict, merge_cfg_from_args, get_arguments
import os
import sys
sys.path.append("softwareOfPaddle/")

args = get_arguments()
cfg = AttrDict()
with open("connfig.txt","r") as cof:
    reader = cof.readlines()
    reader = [line.rstrip("\n") for line in reader]
    cfg.gpu = int(reader[1])
    cfg.model_path = reader[2]
    cfg.run_mode = "fluid"


merge_cfg_from_args(args, cfg)

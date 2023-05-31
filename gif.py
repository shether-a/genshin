import imageio
import glob
import os
import argparse
import re
import cv2
import _pickle as pickle
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb
# 导入os模块

'''


f=open('./result/ecg/chfdb_chf13_45590/f_beta.pkl','rb')
inf=pickle.load(f)
print(inf)

'''



'''
def tryint(s):
    try:
        return int(s)
    except:
        return s

def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]
'''
parser = argparse.ArgumentParser(description='PNG to GIF')
parser.add_argument('--pngpath', type=str, default=r'E:/code/genshin/dataset/png',
                     help='file path ')
parser.add_argument('--gifpath', type=str, default=r'E:/code/genshin/dataset/gif',
                     help='file path ')
args = parser.parse_args()

# -*- coding: UTF-8 -*-
import os

# dirs = []

# for item in os.scandir(args.pngpath):
#     if item.is_dir():
#         dirs.append(item.path)
# os.listdir()方法获取文件夹名字，返回数组
dir_name_list = os.listdir(args.pngpath)
# 转为转为字符串
# dir_names = str(dir_name_list)
print(dir_name_list)
for dir in dir_name_list:
    images = []
    filenames = glob.glob('E:/code/genshin/dataset/png/'+dir+'/*')
    # # print(filenames)
    # filenames.sort(key=os.path.getmtime)
    # print(filenames)
    print(filenames)
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave(args.gifpath+'/'+dir+'.gif',images,duration=0.04)


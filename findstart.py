#Take the last three frames of the video
# -*- coding:utf-8 -*-
__author__ = 'Microcosm'

import cv2
import time
import math
import os
import os.path as osp
import py_faster_rcnn_board.tools.demo1 as demo1
import shutil
import Test1

def findstart(totalFrameNumber,eye_datas):
    #vc = cv2.VideoCapture('/home/shiyan/zk/vision_test/video/video.wmv')


    delta=4.0/5#阈值，判断是否在最后1/6时间内绝80%都是看不到画
    minimumcontinuoushigh=35;#最少需要增加的帧数，从后向前检测，如果满足条件则定位，为了区分单眼测试和双眼测试
    #board_count=0;记录包含板子的帧的个数
    #picture_count=0;记录找到画的帧的个数
#if vc.isOpened():

    #totalFrameNumber = vc.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
    #此参数在主判断程序中
    print totalFrameNumber
    boardnumber=0;
    picturenumber=0;
    c = int(totalFrameNumber)

    doubleeyenumber=0;#记录双眼的个数
    label= [0]*(int(totalFrameNumber));#空的记录标签，记录双眼的标记。
    while (c>0):
        if c==1:
            print 'hahahah'
        print str(c) + 'cccccccccccccc'
    # vc.set(cv2.cv.CV_CAP_PROP_POS_FRAMES,c )
    # rval, frame = vc.read()

        eyeposition = [];  # 记录画的号码
        eyescores = [];
        eyecoors = [];
        for f in range(len(eye_datas)):  # 结果中照片的个数
            if eye_datas[f][0] == (str(c) + '.jpg'):
                p = 1
                if len(eye_datas[f]) > 1:
                    for j in range(len(eye_datas[f]) - 1):
                        if eye_datas[f][j + 1][4] == 'eye':
                            eyeposition.append(j + 1)
                            eyescores.append(eye_datas[f][j+1][5])
                            coor = (
                                eye_datas[f][j + 1][0], eye_datas[f][j + 1][1], eye_datas[f][j + 1][2],
                                eye_datas[f][j + 1][3])
                            eyecoors.append(coor)
                    if len(eyecoors) == 2:
                        doubleeyenumber=doubleeyenumber+1;
                        label[c-1]=1;
                        break;
        c=c-1;

    f=open('label.txt','w')
    for i in label:
       f.writelines(str(i));
    f.close();
    #判断那里是双眼的结束点
    sequence=[];
    for j in range(int(totalFrameNumber)-minimumcontinuoushigh,minimumcontinuoushigh,-1):
        sequence=label[j:j+minimumcontinuoushigh];
        if (float(sum(sequence))/minimumcontinuoushigh)>delta:
            return (j+minimumcontinuoushigh)






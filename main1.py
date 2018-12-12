# -*- coding:utf-8 -*-

import cv2
import shutil
import os
import os.path as osp
import py_faster_rcnn_board.tools.demo1 as demo1
import py_faster_rcnn_head.tools.demo2 as demo2
import py_faster_rcnn_eye.tools.demo3 as demo3
import py_faster_rcnn_lens.tools.demo4 as demo4
import Test1
import Best2,Uncoorperate2,NAN,Ordinary2,countothermark
from multiprocessing import Pool
from main import *
import findstart
import gc

if __name__=='__main__':
    video_dir=os.path.join(osp.dirname(__file__), 'video')
    for rt,dirs,files in os.walk(video_dir):
        for file in files:
            video_name=file
            with open('result.txt', 'a') as f:
                f.write('\n')
                f.write(video_name)

            # video_name='video.wmv'
            im_dir=os.path.join(osp.dirname(__file__), 'frame')
            head_dir = os.path.join(osp.dirname(__file__), 'head')
            eye_dir = os.path.join(osp.dirname(__file__), 'eye')
            cut_dir= os.path.join(osp.dirname(__file__), 'cut')
            if not os.path.exists(im_dir):
                os.mkdir(im_dir)
            vc = cv2.VideoCapture(os.path.join(video_dir,video_name))
            if vc.isOpened():
                totalFrameNumber = vc.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)

                totalFrameNumber=Test1.interception_video(video_dir,video_name,im_dir,totalFrameNumber)
                print totalFrameNumber

                numpy=True
                for root, dirs, files in os.walk(im_dir):
                    if len(files)==0:
                        numpy=False


                if numpy:
                    print 'demo1~~~~~~~~~~~~~~~~~~~~~'
                    board_datas = []
                    board_datas=demo1.main()
                    gc.collect()
                    print 'demo2~~~~~~~~~~~~~~~~~~~~~'
                    head_datas = demo2.main()
                    gc.collect()
                    if not os.path.exists(head_dir):
                        os.mkdir(head_dir)
                    NAN.getHead(im_dir, head_dir, head_datas)
                    numpy = True
                    for root, dirs, files in os.walk(head_dir):
                        if len(files) == 0:
                            numpy = False
                    if numpy:
                        print 'demo3~~~~~~~~~~~~~~~~~~~~~'
                        eye_datas = demo3.main()
                        gc.collect()
                        if not os.path.exists(eye_dir):
                            os.mkdir(eye_dir)
                        NAN.getEye(head_dir, eye_dir, eye_datas)
                        numpy = True
                        for root, dirs, files in os.walk(eye_dir):
                            if len(files) == 0:
                                numpy = False
                        if numpy:
                            print 'demo4~~~~~~~~~~~~~~~~~~~~~'
                            eyelet_datas = demo4.main()
                            gc.collect()
                            totalFrameNumber = findstart.findstart(totalFrameNumber, eye_datas)
                            if totalFrameNumber==None or totalFrameNumber==0:
                                print video_name + ':\t不能判断'
                                with open('result.txt', 'a') as f:
                                    f.write('\n')
                                    f.write(video_name + ':\t' + '不能判断')
                            else:
                                result1=Uncoorperate2.Unordinary(totalFrameNumber,board_datas,head_datas,eye_datas,eyelet_datas)
                                #result1=False
                                if result1[1]:
                                    print video_name+': Unordinary'
                                    with open('result.txt','a') as f:
                                        f.write('\n')
                                        f.write(video_name+':\tUnordinary')
                                else:
                                    resultother=countothermark.countother(totalFrameNumber,board_datas, head_datas, eye_datas, eyelet_datas,result1[0])
                                    if resultother:
                                        print video_name + ': Unordinary'
                                        with open('result.txt', 'a') as f:
                                            f.write('\n')
                                            f.write(video_name + ':\tUnordinary')
                                    else:
                                        result2=NAN.Cross_eyed(eye_dir, eyelet_datas, im_dir,result1[2],totalFrameNumber)
                                        if result2 != "no_cross_eyed":
                                            print video_name+':\tUnordinary'
                                            with open('result.txt', 'a') as f:
                                                f.write('\n')
                                                f.write(video_name + ':\t'+result2)
                                        else:
                                            result3=NAN.is_NAN(eye_dir, board_datas, eyelet_datas,totalFrameNumber)
                                            if result3:
                                                print video_name+": NAN"
                                                with open('result.txt', 'a') as f:
                                                    f.write('\n')
                                                    f.write(video_name + ':\tNAN')
                                            else:
                                                result4=Best2.best(totalFrameNumber,board_datas,eye_datas)
                                                if result4=='best':
                                                    print video_name+': best'
                                                    with open('result.txt', 'a') as f:
                                                        f.write('\n')
                                                        f.write(video_name + ':\tbest')
                                                else:
                                                    result5=Ordinary2.ordinary(totalFrameNumber,board_datas,head_datas,eye_datas,eyelet_datas)
                                                    if result5=='0':
                                                        print video_name+': >0.05'
                                                        with open('result.txt', 'a') as f:
                                                            f.write('\n')
                                                            f.write(video_name + ':\t>0.05')
                                                    else:
                                                        if result5=='1':
                                                            print video_name+': <0.05'
                                                            with open('result.txt', 'a') as f:
                                                                f.write('\n')
                                                                f.write(video_name + ':\t<0.05')
                                                        else:
                                                            print video_name+': '+str(result5)
                                                            with open('result.txt', 'a') as f:
                                                                f.write('\n')
                                                                f.write(video_name + ':\t'+str(result5))
                        else:
                            print 'no eye'
                    else:
                        print 'no head'
                else:
                    print 'no frame'
            else:
                print 'cant find video'
            shutil.rmtree(im_dir)
            os.mkdir(im_dir)
            shutil.rmtree(head_dir)
            os.mkdir(head_dir)
            shutil.rmtree(eye_dir)
            os.mkdir(eye_dir)
            shutil.rmtree(cut_dir)
            os.mkdir(cut_dir)
            gc.collect()
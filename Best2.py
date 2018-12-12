#Take the last three frames of the video
# -*- coding:utf-8 -*-
__author__ = 'Microcosm'

import cv2
import time
import math
import os
import os.path as osp
import py_faster_rcnn_board.tools.demo1 as demo1
import py_faster_rcnn_head.tools.demo2 as demo2
import py_faster_rcnn_eye.tools.demo3 as demo3
import shutil
import Test1
import findstart,NAN

def best(totalFrameNumber,board_datas,eye_datas):
    #vc = cv2.VideoCapture('/home/shiyan/zk/vision_test/video/video.wmv')
    threshold=5#阈值，观察视频最后的一部分进行是否>0.21的判断
    step=0.25
    sigma=0.8#阈值，判断是否在最后1/6时间内绝80%都是看不到画
    #board_count=0;记录包含板子的帧的个数
    #picture_count=0;记录找到画的帧的个数
#if vc.isOpened():

    #totalFrameNumber = vc.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
    #此参数在主判断程序中
    print totalFrameNumber
    boardnumber=0;
    picturenumber=0;
    c=totalFrameNumber

    # c = findstart.findstart(totalFrameNumber,eye_datas)
    # if c==None:
    #     return '不能判断'
    # totalFrameNumber=c
    flag = True
    while (flag):

        print str(c) + 'cccccccccccccc'

    # vc.set(cv2.cv.CV_CAP_PROP_POS_FRAMES,c )
    # rval, frame = vc.read()

        #cv2.imwrite('./frame/' + str(c) + '.jpg', frame)#将这张照片放入该放的文件夹中，比如判断是否视力>0.21文件夹下的原图文件夹
        #c = c - 1
        #cv2.waitKey(1)
        #此处调用demo.py不断识别板子和画
        #tempresult=demo1.main() #找到板子和画
        ifcontinue=0;
        for f in range(len(board_datas)):#结果中照片的个数
            boardposition = [];  # 记录画的号码
            boardscores = [];
            boardcoors = [];
            if board_datas[f][0]==(str(c)+'.jpg'):

                if  len(board_datas[f]) >1:
                    for j in range(len(board_datas[f]) - 1):
                        if board_datas[f][j + 1][4] == 'noboard':
                            boardposition.append(j + 1)
                            boardscores.append(board_datas[f][j][5])
                            coor = (
                                board_datas[f][j + 1][0], board_datas[f][j + 1][1], board_datas[f][j + 1][2],
                                board_datas[f][j + 1][3])
                            boardcoors.append(coor)
                    maxposition = 0;
                    maxvalue = 0;
                    for t in range(len(boardscores)):  # 如果有多个板子，我们去置信度最大的一个
                        if boardscores[t] > maxvalue:
                            maxposition = t;
                            maxvalue = boardscores[t]
                    if maxvalue != 0:#如果找到了noboard
                        #os.remove('./frame/' + str(c+1) + '.jpg')
                        if c <= math.floor((totalFrameNumber ) * (1 - 1.0/threshold)):
                            if boardnumber==0 & threshold>2.0:
                                threshold=threshold-step;
                            else:
                                flag=False;
                        ifcontinue=1;#1表示需要continue
                        break;
                    else:
                        break;
        if ifcontinue==1:
            c = c - 1;
            continue;


        #记录找到板子和找到画的帧各有多少
        #boxnumber=len(tempresult[0])
        for f in range(len(board_datas)):
            position=[];#记录板子的号码
            scores=[];
            coors=[];
            #[i][0]是照片名，[i][j]是本张照片第j个框的信息，其中包括左上角横纵坐标，宽高还有类别名和分数
            #注意是一张一张照片送给模型检测
            if board_datas[f][0]==(str(c)+'.jpg'):
                if len(board_datas[f])>1:
                    for j in range(len(board_datas[f])-1):
                        if board_datas[f][j+1][4]=='board':
                            position.append(j+1)
                            scores.append(board_datas[f][j+1][5])
                            coor=(board_datas[f][j+1][0],board_datas[f][j+1][1],board_datas[f][j+1][2],board_datas[f][j+1][3]);
                            coors.append(coor)
                    maxposition=0;
                    maxvalue=0;
                    for t in range(len(scores)):#如果有多个板子，我们去置信度最大的一个
                        if scores[t]>maxvalue:
                            maxposition=t;
                            maxvalue=scores[t]
                    if  maxvalue!=0:
                        boardnumber=boardnumber+1
                        if c <= math.floor((totalFrameNumber) * (1 - 1.0/threshold)):
                            if boardnumber==0 & threshold>2.0:
                                threshold=threshold-step;
                            else:
                                flag=False;
                        #ifcontinue = 1;
                        break;
                    else:
                        if c <= math.floor((totalFrameNumber) * (1 - 1.0/threshold)):
                            if boardnumber==0 & threshold>2.0:
                                threshold=threshold-step;
                            else:
                                flag=False;
                        #ifcontinue = 1;
                        break;
                else:
                    if c <= math.floor((totalFrameNumber) * (1 - 1.0/threshold)):
                        if boardnumber == 0 & threshold > 2.0:
                            threshold = threshold - step;
                        else:
                            flag = False;
                    #ifcontinue = 1;
                    break;
        # if ifcontinue==1:
        #     c=c-1
        #     continue;

        for f in range(len(board_datas)):
            pictureposition = [];  # 记录画的号码
            picturescores = [];
            picturecoors = [];
            if board_datas[f][0]==(str(c)+'.jpg'):
                if len(board_datas[f])>1:
                    for j in range(len(board_datas[f])-1):
                        if (board_datas[f][j+1][4]=='picture') | (board_datas[f][j+1][4]=='maxpicture'):
                            pictureposition.append(j+1)
                            picturescores.append(board_datas[f][j][5])
                            coor=(board_datas[f][j+1][0],board_datas[f][j+1][1],board_datas[f][j+1][2],board_datas[f][j+1][3]);
                            picturecoors.append(coor)
                    maxposition = 0;
                    maxvalue = 0;
                    for t in range(len(picturescores)):#如果有多个板子，我们去置信度最大的一个
                        if picturescores[t]>maxvalue:
                            maxposition=t;
                            maxvalue=picturescores[t]
                    if maxvalue!=0:
                        picturenumber=picturenumber+1
                        if c <= math.floor((totalFrameNumber) * (1 - 1.0/threshold)):
                            if boardnumber==0 & threshold>2.0:
                                threshold=threshold-step;
                            else:
                                flag=False;
                        ifcontinue=1;
                        break;
                    else:
                        if c <= math.floor((totalFrameNumber) * (1 - 1.0/threshold)):
                            if boardnumber==0 & threshold>2.0:
                                threshold=threshold-step;
                            else:
                                flag=False;
                        ifcontinue=1;
                        break;
                else:
                    if c <= math.floor((totalFrameNumber) * (1 - 1.0/threshold)):
                        if boardnumber == 0 & threshold > 2.0:
                            threshold = threshold - step;
                        else:
                            flag = False;
                    ifcontinue = 1;
                    break;
        if ifcontinue==1:
            c=c-1;
            continue;

        # if c <= math.floor((totalFrameNumber - 3)*(1-threshold)):
        #     flag = False
        #os.remove('./frame/' + str(c+1) + '.jpg');
    print "picturenumber:" + str(picturenumber)
    print "boardnumber:" + str(boardnumber)
    print "sigma:" + str(sigma)
    print "threshold:" + str(1.0/threshold)
    print "totalFrameNumber:" + str(totalFrameNumber)

    if (boardnumber-picturenumber)>sigma*boardnumber:
        return 'best'
    else:
        return 'not best'

    # vc.release()



if __name__=='__main__':
    video_dir=os.path.join(osp.dirname(__file__), 'video')
    video_name='video.wmv'
    im_dir=os.path.join(osp.dirname(__file__), 'frame')
    head_dir = os.path.join(osp.dirname(__file__), 'head')
    eye_dir = os.path.join(osp.dirname(__file__), 'eye')
    if not os.path.exists(im_dir):
        os.mkdir(im_dir)
    vc = cv2.VideoCapture(os.path.join(video_dir,video_name))
    if vc.isOpened():
        totalFrameNumber = vc.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
        shutil.rmtree(eye_dir)
        os.mkdir(eye_dir)
        shutil.rmtree(head_dir)
        os.mkdir(head_dir)
        shutil.rmtree(im_dir)
        os.mkdir(im_dir)
        Test1.interception_video(video_dir,video_name,im_dir)
        numpy=True
        for root, dirs, files in os.walk(im_dir):
            if len(files)==0:
                numpy=False


        if numpy:
            print 'demo1~~~~~~~~~~~~~~~~~~~~~'
            board_datas = []
            board_datas=demo1.main()
            print 'demo2~~~~~~~~~~~~~~~~~~~~~'
            head_datas = demo2.main()
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
                if not os.path.exists(eye_dir):
                    os.mkdir(eye_dir)
                NAN.getEye(head_dir, eye_dir, eye_datas)
                numpy = True
                for root, dirs, files in os.walk(eye_dir):
                    if len(files) == 0:
                        numpy = False
                if numpy:
                    result1=best(totalFrameNumber,board_datas,eye_datas)
                    print result1

        else:
            print 'no frame'
    else:
        print 'cant find video'
    shutil.rmtree(eye_dir)
    os.mkdir(eye_dir)
    shutil.rmtree(head_dir)
    os.mkdir(head_dir)
    # shutil.rmtree(im_dir)
    # os.mkdir(im_dir)

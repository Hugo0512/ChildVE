#Take the last three frames of the video
# -*- coding:utf-8 -*-
__author__ = 'Microcosm'

import cv2
import shutil
import os
import os.path as osp
from PIL import Image
import py_faster_rcnn_board.tools.demo1 as demo1
import py_faster_rcnn_head.tools.demo2 as demo2
import py_faster_rcnn_eye.tools.demo3 as demo3
import py_faster_rcnn_lens.tools.demo4 as demo4
import Test1
import NAN
import Best2

def Unordinary(totalFrameNumber,board_datas,head_datas,eye_datas,lenlet_datas):
    # vc = cv2.VideoCapture(os.path.join(osp.dirname(__file__), 'video','video.wmv'))
    # if vc.isOpened():

        #totalFrameNumber = vc.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
        #print totalFrameNumber
        isUncoorperate=0

        #所有用到的阈值
        threshold1 = 0.7;
        threshold2 = 0.1;
        threshold3 = 0.3
        threshold4 = 0.9;
        threshold5 = 0.1

        picturetime = 0;  # 记录出现画的次数
        lenstime = 0;  # 记录出现眼睛方向对的次数
        eyetime = 0;  # 记录找不到眼睛的次数
        headtime = 0;  # 记录找不到脑袋的次数
        noboardtime=0;#记录没有出现板子的次数
        boardtime=0;#放板子的帧数是一个基准，所以要检测
        directthreshold = 2.0 / 5
        c = int(totalFrameNumber)
        flag = True
        while (flag):
            # p=0
            print str(c) + 'vvvvvvvvvvvv'
            if c==0:
                print str(c)+'vvvvvvvvvvvv'
                break;
            # vc.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, c)
            # rval, frame = vc.read()
            # cv2.imwrite('./frame/' + str(c) + '.jpg', frame)
            # cv2.waitKey(1)
            # c=40
            #result1 = demo1.main()
            # 记录板子的最大分数的号码
            ifcontinue=0;#记录需要continue否？1代表需�?
            for f in range(len(board_datas)):  # 结果中照片的个数
                boardposition = [];  # 记录画的号码
                boardscores = [];
                boardcoors = [];
                if board_datas[f][0] == (str(c) + '.jpg'):
                    #p=1
                    if len(board_datas[f]) > 1:
                        for j in range(len(board_datas[f]) - 1):
                            if board_datas[f][j + 1][4] == 'noboard':
                                boardposition.append(j + 1)
                                boardscores.append(board_datas[f][j+1][5])
                                coor = (
                                    board_datas[f][j + 1][0], board_datas[f][j + 1][1], board_datas[f][j + 1][2],
                                    board_datas[f][j + 1][3])
                                boardcoors.append(coor)
                        maxposition = 0;
                        maxvalue = 0;
                        for t in range(len(boardscores)):  # 如果有多个板子，我们去置信度最大的一�?
                            if boardscores[t] > maxvalue:
                                maxposition = t
                                maxvalue = boardscores[t]
                        if maxvalue != 0:
                            # os.remove('./frame/' + str(c+1) + '.jpg')
                            noboardtime = noboardtime + 1;
                            #ifcontinue = 1;  # 1表示需要continue
                            break;
                        else:
                            break;
                    else:
                        #ifcontinue = 1;  # 1表示需要continue
                        break;
            # if ifcontinue == 1:
            #     c = c - 1;
            #     continue;
            # if ifcontinue == 1:
            #     c = c - 1;
            #     continue;

            for f in range(len(board_datas)):
                boardposition = [];  # 记录板子的号�?
                boardscores = [];
                boardcoors = [];
                boardlastposition = [];
                if board_datas[f][0]==(str(c)+'.jpg'):
                    if len(board_datas[f]) > 1:
                        for j in range(len(board_datas[f]) - 1):
                            if board_datas[f][j + 1][4] == 'board':
                                boardposition.append(j)
                                boardscores.append(board_datas[f][j + 1][5])
                                coor = (board_datas[f][j + 1][0], board_datas[f][j + 1][1], board_datas[f][j + 1][2], board_datas[f][j + 1][3]);
                                boardcoors.append(coor)
                        maxposition = 0;
                        maxvalue = 0;
                        for t in range(len(boardscores)):  # 如果有多个板子，我们取置信度最大的一�?
                            if boardscores[t] > maxvalue:
                                maxposition = t;
                                maxvalue = boardscores[t]
                        for t in range(len(boardscores)):
                            if t == maxposition:
                                boardlastposition = boardcoors[t]
                        if len(boardlastposition)==0:
                            # shutil.rmtree('frame')
                            # os.mkdir('frame')
                            # shutil.rmtree('head')
                            # os.mkdir('head')
                            # shutil.rmtree('eye')
                            # os.mkdir('eye')
                            #ifcontinue=1;
                            break;
                        else:
                            boardtime=boardtime+1;
                            break;
                    else:

                        #ifcontinue=1;
                        break
            # if ifcontinue==1:
            #     c = c - 1
            #     continue;

            for f in range(len(board_datas)):
                pictureposition = [];  # 记录画的号码
                picturescores = [];
                picturecoors = [];
                picturelastposition = []
                if board_datas[f][0]==(str(c)+'.jpg'):
                    if len(board_datas[f]) > 1:
                        for j in range(len(board_datas[f]) - 1):
                            print board_datas[f][j + 1][4]
                            if board_datas[f][j + 1][4] == 'picture' or board_datas[f][j + 1][4] == 'maxpicture':
                                pictureposition.append(j + 1)
                                picturescores.append(board_datas[f][j + 1][5])
                                coor = (board_datas[f][j + 1][0], board_datas[f][j + 1][1], board_datas[f][j + 1][2], board_datas[f][j + 1][3]);
                                picturecoors.append(coor)
                        maxposition = 0;
                        maxvalue = 0;
                        for t in range(len(picturescores)):  # 如果有多个板子，我们取置信度最大的一�?
                            if picturescores[t] > maxvalue:
                                maxposition = t;
                                maxvalue = picturescores[t]
                        for t in range(len(picturescores)):
                            if t == maxposition:
                                picturelastposition = picturecoors[t]
                        if len(picturelastposition)==0:

                            # ifcontinue = 1;
                            break;
                        else:
                            picturetime=picturetime+1;
                            break;
                    else:
                        # shutil.rmtree('frame')
                        # os.mkdir('frame')
                        # shutil.rmtree('head')
                        # os.mkdir('head')
                        # shutil.rmtree('eye')
                        # os.mkdir('eye')
                        # c = c - 1

                        # ifcontinue = 1;
                        break;
            # if ifcontinue==1:
            #     c=c-1;
            #     continue;
            # 记录脑袋的位置，坐标�?
            for f in range(len(head_datas)):
                headposition = [];  # 记录脑袋的号�?
                headscores = [];
                headcoors = [];
                headlastposition = []
                if head_datas[f][0]==(str(c)+'.jpg'):
                    if len(head_datas[f]) > 1:
                        for j in range(len(head_datas[f]) - 1):
                            if head_datas[f][j + 1][4] == 'head':
                                headposition.append(j + 1)
                                headscores.append(head_datas[f][j + 1][5])
                                coor = (head_datas[f][j + 1][0], head_datas[f][j + 1][1], head_datas[f][j + 1][2], head_datas[f][j + 1][3]);
                                headcoors.append(coor)
                        maxposition = 0;
                        maxvalue = 0;
                        for t in range(len(headscores)):  # 如果有多个头，我们取置信度最大的一�?
                            if headscores[t] > maxvalue:
                                maxposition = t;
                                maxvalue = headscores[t]
                        for t in range(len(headscores)):
                            if t == maxposition:
                                headlastposition = headcoors[t]
                        if len(headlastposition)==0:#没找到脑�?
                            # ifcontinue=1;

                            break;
                        else:
                            headtime = headtime + 1
                            break;
                    else:
                        # shutil.rmtree('frame')
                        # os.mkdir('frame')
                        # shutil.rmtree('head')
                        # os.mkdir('head')
                        # shutil.rmtree('eye')
                        # os.mkdir('eye')
                        # ifcontinue=1;
                        break
            # if ifcontinue==1:
            #     c = c - 1
            #     continue;
            # 将人脸截�?
            # originalimage = Image.open("./frame/" + str(c) + ".jpg")  # 存入相应文件夹，比如测试是否视力大于0.21的文件夹下的脑袋文件�?
            # headlastposition = (headlastposition[0], headlastposition[1], headlastposition[0] + headlastposition[2], headlastposition[1] + headlastposition[3])
            #
            # temphead = originalimage.crop(headlastposition)
            # temphead.save('./cut/' + str(c) + '.jpg')
            # head = cv2.imread('./cut/' + str(c) + '.jpg')
            # width, height = head.shape[:2]
            # shutil.rmtree('cut')
            # os.mkdir('cut')
            # largerhead = cv2.resize(head, (3 * width, 3 * height), interpolation=cv2.INTER_CUBIC)
            # cv2.imwrite("./head/" + str(c) + ".jpg", largerhead)
            # eyeresult = demo3.main()
            count = 0;  # 记录本次对象识别识别到的眼睛个数
            eyeposition = []  # 记录眼睛的号�?
            eyescores = []
            eyecoors = []
            eyelastposition = []
            for f in range(len(eye_datas)):
                tempname=eye_datas[f][0];
                if tempname==(str(c)+'.jpg'):#找到了的�?
                    # count=count+1;
                    if len(eye_datas[f]) > 1:
                        for j in range(len(eye_datas[f]) - 1):
                            if eye_datas[f][j + 1][4] == 'eye':
                                eyeposition.append(j + 1)
                                eyescores.append(eye_datas[f][j + 1][5])
                                coor = (
                                    eye_datas[f][j + 1][0], eye_datas[f][j + 1][1], eye_datas[f][j + 1][2], eye_datas[f][j + 1][3]);
                                eyecoors.append(coor)
                        count=len(eyeposition)
                        maxposition = 0
                        maxvalue = 0
                        if count!=0:
                            eyetime = eyetime + 1;
                        break;
                    else:
                        # shutil.rmtree('frame')
                        # os.mkdir('frame')
                        # shutil.rmtree('head')
                        # os.mkdir('head')
                        # shutil.rmtree('eye')
                        # os.mkdir('eye')

                        # ifcontinue=1;
                        break;
            # if ifcontinue==1:
            #
            #     c = c - 1;
            #     continue;

            # if len(eyecoors) > 2:  # 多个眼睛
            #     # 对数据排�?然后删除多余�?
            #     for m in range(len(eyeposition) - 1):
            #         for n in range(m + 1, len(eyeposition)):
            #             if eyescores[m] < eyescores[n]:
            #                 temp = eyescores[m]
            #                 eyescores[m] = eyescores[n]
            #                 eyescores[n] = temp
            #                 temp = eyecoors[m]
            #                 eyecoors[m] = eyecoors[n]
            #                 eyecoors[n] = temp
            #     eyecoors=eyecoors[:2]
            #count=len(eyecoors);#眼睛数量
            # originaleyeimage = Image.open("./head/" + str(c) + ".jpg")  # 之前的脑袋图
            # for q in eyecoors:
            #     count = count + 1
            #     q=(q[0],q[1],q[0]+q[2],q[1]+q[3])
            #     cropeye = originaleyeimage.crop(q)
            #     cropeye.save('./cut/cropeye.jpg')
            #     eye = cv2.imread('./cut/cropeye.jpg')
            #     height, width = eye.shape[:2]
            #     largereye = cv2.resize(eye, (3 * width, 3 * height), interpolation=cv2.INTER_CUBIC)
            #     cv2.imwrite("./eye/eye" + str(count) + ".jpg", largereye)  # 对眼睛编�?1,2
            #     shutil.rmtree('cut')
            #     os.mkdir('cut')
            # picturestate = 0;  # 1代表左，2代表�?
            # if len(picturelastposition)!=0 & len(boardlastposition)!=0:
            #     if (0.5 * picturelastposition[2] + picturelastposition[0]) < (boardlastposition[0] + boardlastposition[2] * 0.5):
            #         picturestate = 1
            #     else:
            #         picturestate = 2
            # else:
            #     c=c-1;
            #     continue;

            # lensresult = demo4.main()
            count1=0;
            lensposition = [];  # 记录晶状体的号码
            lensscores = [];
            lenscoors = [];
            lenslastposition = [];
            for p in range(len(lenlet_datas)):
                tempname=lenlet_datas[p][0];
                if tempname==(str(c)+'_eye1.jpg') or tempname== (str(c)+'_eye2.jpg'):#找到了眼睛图片的名字
                    count1 = count1 + 1;
                    if len(lenlet_datas[p]) > 1:  # 识别到了眼珠
                        for j in range(len(lenlet_datas[p]) - 1):
                            if lenlet_datas[p][j+1][4]== 'lens':
                                lensposition.append(j + 1)
                                lensscores.append(lenlet_datas[p][j + 1][5])
                                coor = (lenlet_datas[p][j + 1][0], lenlet_datas[p][j + 1][1], lenlet_datas[p][j + 1][2],
                                        lenlet_datas[p][j + 1][3]);
                                lenscoors.append(coor)
                if count1==count:
                    break;
                        # maxposition = 0
                        # maxvalue = 0
                        # 一个眼睛只能要一个眼�?
                        # for m in range(len(lensposition)):
                        #     if lensscores[m] > maxvalue:
                        #         maxvalue = lensscores[m];
                        #         maxposition = m;
                        # for t in range(len(lenscoors)):
                        #     if t == maxposition:
                        #         lenslastposition = lenscoors[t]
                                # 判断眼睛位置和板子位置的相对关系
                        # im = cv2.imread('./eye/'+tempname)  # 文件名就在p[0]中，路径在eye文件夹中
                        # imagewidth, imageheight = im.shape[:2]
                        # xmin, ymin, lenswidth, lensheight = lenslastposition[:4]
            if len(lensposition)!=0:
                lenstime=lenstime+1;
                    #     if picturestate == 1:
                    #         if (xmin + 0.5 * lenswidth) < imagewidth * 0.5:
                    #             # 此时看到
                    #             lenstime=lenstime+1;
                    #             break
                    #         else:
                    #             uncount = uncount + 1;
                    #             if uncount == count:
                    #                 break;
                    #             continue
                    # # else:
                    # #     continue;
                    #     elif picturestate == 2:
                    #         if (xmin + 0.5 * lenswidth) > imagewidth * 0.5:
                    #             # 此时看到
                    #             lenstime=lenstime+1;
                    #             break
                    #         else:
                    #             uncount = uncount + 1;
                    #             if uncount == count:
                    #                 break;
                    #             continue
                    #     # else:
                    #     #     # shutil.rmtree('frame')
                    #     #     # os.mkdir('frame')
                    #     #     # shutil.rmtree('head')
                    #     #     # os.mkdir('head')
                    #     #     # shutil.rmtree('eye')
                    #     #     # os.mkdir('eye')
                    #     #     c = c - 1
                    #     #     ifcontinue=1;
                    #     #     if c == 0:
                    #     #         flag = False
                    #     #     break;
                    # else:
                    #     #c = c - 1;
                    #     continue;

            # if ifcontinue:
            #     c=c-1;
            #     continue
            c=c-1
        print 'boardtime:'+str(boardtime)
        print 'lenstime:'+str(lenstime)
        print 'noeyetime:'+str(eyetime)
        print 'noheadtime:'+str(headtime)
        print 'picturetime:'+str(picturetime)
        print 'noboardtime:'+str(noboardtime)
        print 'totalFrameNumber:'+str(totalFrameNumber)
        if (lenstime<(totalFrameNumber*threshold1)) | (eyetime<(threshold2*totalFrameNumber)) | (headtime<(totalFrameNumber*threshold3))  | ((float(boardtime)/totalFrameNumber)<threshold5) | ((float(noboardtime)/totalFrameNumber)>threshold4):
            print '此人不配合'
            return picturetime,True,eyetime
            # return True
        else:
            print '此人配合'
            return picturetime,False,eyetime
            # return False
            # shutil.rmtree('frame')
            # os.mkdir('frame')
            # shutil.rmtree('head')
            # os.mkdir('head')
            # shutil.rmtree('eye')
            # os.mkdir('eye')
        # vc.release()
        # # 清空文件夹内的所有文�?
        # shutil.rmtree('frame')
        # os.mkdir('frame')
        # shutil.rmtree('head')
        # os.mkdir('head')
        # shutil.rmtree('eye')
        # os.mkdir('eye')
        # shutil.rmtree('last')
        # os.mkdir('last')
    # else:
    #     rval = False
    #     print rval


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
        print totalFrameNumber
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
                    print 'demo4~~~~~~~~~~~~~~~~~~~~~'
                    eyelet_datas = demo4.main()
                    result1=Unordinary(totalFrameNumber,board_datas,head_datas,eye_datas,eyelet_datas)
                    if result1:
                        print 'Unordinary'
                    else:
                        print 'ordinary'
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

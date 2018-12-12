# Take the last three frames of the video
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
import Best2, Uncoorperate2, NAN, findstart
from twoclass.myself.vision_test.five_fold_cross_twoclass.get_result_five_fold_cross import *


def countother(totalFrameNumber,board_datas, head_datas, eye_datas, lenlet_datas,picturetime):
    # vc = cv2.VideoCapture(os.path.join(osp.dirname(__file__), 'video','video.wmv'))
    # if vc.isOpened():
    see=0;
    nosee=0;
    # totalFrameNumber = vc.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
    # print totalFrameNumber
    isOrdinary = 0
    # directthreshold = 2.0 / 5
    # c = findstart.findstart(totalFrameNumber,eye_datas)
    c = int(totalFrameNumber)
    threshold1=0.3
    threshold2=0.8
    # if c==None:
    #     return '不能判断'
    flag = True
    while (c>0):
        p = 0
        print str(c) + 'vvvvvvvvvvvv'
        if c == 0:
            print str(c) + 'vvvvvvvvvvvv'
        # vc.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, c)
        # rval, frame = vc.read()
        # cv2.imwrite('./frame/' + str(c) + '.jpg', frame)
        # cv2.waitKey(1)
        # c=40
        # result1 = demo1.main()
        # 记录板子的最大分数的号码
        ifcontinue = 0;  # 记录需要continue否？1代表需�?
        for f in range(len(board_datas)):  # 结果中照片的个数
            boardposition = [];  # 记录画的号码
            boardscores = [];
            boardcoors = [];
            # print 'sddfdfdfdfdd'+board_datas[f][0]
            # print 'cccccccccccc'+str(c)+ '.jpg'
            if board_datas[f][0] == (str(c) + '.jpg'):
                p = 1
                # print 'ttttttttttttttttiiii'+str(p)
                if len(board_datas[f]) > 1:
                    for j in range(len(board_datas[f]) - 1):
                        if board_datas[f][j + 1][4] == 'noboard':
                            boardposition.append(j + 1)
                            boardscores.append(board_datas[f][j + 1][5])
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

                        ifcontinue = 1;  # 1表示需要continue
                        break;
                else:

                    ifcontinue = 1;  # 1表示需要continue
                    break;
        if ifcontinue == 1:
            c = c - 1;
            continue;
        if p == 0:
            c = c - 1;
            continue;

        for f in range(len(board_datas)):
            boardposition = [];  # 记录板子的号�?
            boardscores = [];
            boardcoors = [];
            boardlastposition = [];
            if board_datas[f][0] == (str(c) + '.jpg'):
                if len(board_datas[f]) > 1:
                    for j in range(len(board_datas[f]) - 1):
                        if board_datas[f][j + 1][4] == 'board':
                            boardposition.append(j)
                            boardscores.append(board_datas[f][j + 1][5])
                            coor = (board_datas[f][j + 1][0], board_datas[f][j + 1][1], board_datas[f][j + 1][2],
                                    board_datas[f][j + 1][3]);
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
                    if len(boardlastposition) == 0:
                        # shutil.rmtree('frame')
                        # os.mkdir('frame')
                        # shutil.rmtree('head')
                        # os.mkdir('head')
                        # shutil.rmtree('eye')
                        # os.mkdir('eye')

                        ifcontinue = 1;
                        break;
                    else:

                        break;
                else:

                    ifcontinue = 1;
                    break
        if ifcontinue == 1:
            c = c - 1
            continue;

        for f in range(len(board_datas)):
            pictureposition = [];  # 记录画的号码
            picturescores = [];
            picturecoors = [];
            picturelastposition = []
            if board_datas[f][0] == (str(c) + '.jpg'):
                if len(board_datas[f]) > 1:
                    for j in range(len(board_datas[f]) - 1):
                        print board_datas[f][j + 1][4]
                        if board_datas[f][j + 1][4] == 'picture':
                            pictureposition.append(j + 1)
                            picturescores.append(board_datas[f][j + 1][5])
                            coor = (board_datas[f][j + 1][0], board_datas[f][j + 1][1], board_datas[f][j + 1][2],
                                    board_datas[f][j + 1][3]);
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
                    if len(picturelastposition) == 0:

                        ifcontinue = 1;
                        break;
                    else:

                        break;
                else:
                    # shutil.rmtree('frame')
                    # os.mkdir('frame')
                    # shutil.rmtree('head')
                    # os.mkdir('head')
                    # shutil.rmtree('eye')
                    # os.mkdir('eye')

                    ifcontinue = 1;
                    break;
        if ifcontinue == 1:
            c = c - 1;
            continue;
        # 记录脑袋的位置，坐标�?
        for f in range(len(head_datas)):
            headposition = [];  # 记录脑袋的号�?
            headscores = [];
            headcoors = [];
            headlastposition = []
            if head_datas[f][0] == (str(c) + '.jpg'):
                if len(head_datas[f]) > 1:
                    for j in range(len(head_datas[f]) - 1):
                        if head_datas[f][j + 1][4] == 'head':
                            headposition.append(j + 1)
                            headscores.append(head_datas[f][j + 1][5])
                            coor = (head_datas[f][j + 1][0], head_datas[f][j + 1][1], head_datas[f][j + 1][2],
                                    head_datas[f][j + 1][3]);
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
                    if len(headlastposition) == 0:  # 没找到脑�?
                        ifcontinue = 1;

                        break;
                    else:

                        break;
                else:
                    # shutil.rmtree('frame')
                    # os.mkdir('frame')
                    # shutil.rmtree('head')
                    # os.mkdir('head')
                    # shutil.rmtree('eye')
                    # os.mkdir('eye')
                    ifcontinue = 1;

                    break
        if ifcontinue == 1:
            c = c - 1
            continue;
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
            tempname = eye_datas[f][0];
            if tempname == (str(c)+'.jpg'):  # 找到了的�?
                # count=count+1;
                if len(eye_datas[f]) > 1:
                    for j in range(len(eye_datas[f]) - 1):
                        if eye_datas[f][j + 1][4] == 'eye':
                            eyeposition.append(j + 1)
                            eyescores.append(eye_datas[f][j + 1][5])
                            coor = (
                                eye_datas[f][j + 1][0], eye_datas[f][j + 1][1], eye_datas[f][j + 1][2],
                                eye_datas[f][j + 1][3]);
                            eyecoors.append(coor)
                    # = len(eyeposition)
                    #对眼睛按照分数排序，只取前2个
                    if len(eyescores)>2:
                        for index in range(len(eyescores)):
                            for index1 in range(index+1,len(eyescores)):
                                if eyescores[index1]<eyescores[index]:
                                    temp=eyescores[index1]
                                    eyescores[index1] =eyescores[index]
                                    eyescores[index]=temp
                                    temp = eyecoors[index1]
                                    eyecoors[index1] = eyecoors[index]
                                    eyecoors[index] = temp
                    eyecoors[2:]=[];
                    eyescores[2:]=[];
                    count=len(eyescores)
                    # if len(eyescores)==0:
                    #     ifcontinue = 1;
                    #     break;
                else:
                    ifcontinue = 1;
                    break;

                        # shutil.rmtree('frame')
                        # os.mkdir('frame')
                        # shutil.rmtree('head')
                        # os.mkdir('head')
                        # shutil.rmtree('eye')
                        # os.mkdir('eye')

        if ifcontinue == 1:
            c = c - 1;
            continue;

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
        # count=len(eyecoors);#眼睛数量
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

        picturestate = 0;  # 1代表左，2代表�?
        if (0.5 * picturelastposition[2] + picturelastposition[0]) < (
            boardlastposition[0] + boardlastposition[2] * 0.5):
            picturestate = 1
        else:
            picturestate = 2

        # lensresult = demo4.main()
        uncount = 0;  # 记录眼睛位置不对的个�?
        miss = 0
        for p in range(len(lenlet_datas)):
            tempname = lenlet_datas[p][0];
            miss = miss + 1;
            if miss == len(lenlet_datas):
                ifcontinue = 1;
            if tempname== (str(c)+'_eye1.jpg') or tempname== (str(c)+'_eye2.jpg'):  # 找到了眼睛图片的名字
                if len(lenlet_datas[p]) > 1:  # 识别到了眼珠
                    lensposition = [];  # 记录晶状体的号码
                    lensscores = [];
                    lenscoors = [];
                    lenslastposition = [];
                    for j in range(len(lenlet_datas[p]) - 1):
                        if lenlet_datas[p][j + 1][4] == 'lens':
                            lensposition.append(j + 1)
                            lensscores.append(lenlet_datas[p][j + 1][5])
                            coor = (lenlet_datas[p][j + 1][0], lenlet_datas[p][j + 1][1], lenlet_datas[p][j + 1][2],
                                    lenlet_datas[p][j + 1][3]);
                            lenscoors.append(coor)
                    maxposition = 0
                    maxvalue = 0
                    # 一个眼睛只能要一个眼�?
                    for m in range(len(lensposition)):
                        if lensscores[m] > maxvalue:
                            maxvalue = lensscores[m];
                            maxposition = m;
                    for t in range(len(lenscoors)):
                        if t == maxposition:
                            lenslastposition = lenscoors[t]
                            # 判断眼睛位置和板子位置的相对关系
                    im = cv2.imread('./eye/' + tempname)  # 文件名就在p[0]中，路径在eye文件夹中
                    imageheight, imagewidth = im.shape[:2]
                    xmin, ymin, lenswidth, lensheight = lenslastposition[:4]

                    if picturestate == 1:
                        if (xmin + 0.5 * lenswidth) < imagewidth * 0.5:
                            # 此时看到
                            #flag = False
                            print "此人视力小于0.21"

                            isOrdinary = 1
                            # 把板子上的画截出来存放在另外一个文件夹�?
                            # originalimage = Image.open("./frame/" + str(c) + ".jpg")  # 之前的完整图
                            # picturelastposition = (picturelastposition[0], picturelastposition[1],
                            #                        picturelastposition[0] + picturelastposition[2],
                            #                        picturelastposition[1] + picturelastposition[3])
                            # picture = originalimage.crop(picturelastposition)
                            # picture.save("./last/lastpicture" + ".jpg")
                            # # 此处调用caffe分类
                            # IMAGE_FILE = osp.abspath(osp.join(osp.dirname(__file__)))
                            # IMAGE_FILE = IMAGE_FILE + '/last/lastpicture' + '.jpg'
                            # result = get_result_five_fold_cross(IMAGE_FILE)
                            # print str(c) + 'vvvvvvvvvvvv'
                            # return result
                            see=see+1;
                            ifcontinue = 1
                            break
                        else:

                            # os.remove("./eye/eye" + str(count) + ".jpg")
                            uncount = uncount + 1;

                            if uncount == count:
                                nosee=nosee+1;
                                ifcontinue = 1;
                                break;
                            continue
                            # else:
                            #     continue;
                    elif picturestate == 2:
                        if (xmin + 0.5 * lenswidth) > imagewidth * 0.5:
                            # 此时看到
                            print "此人视力小于0.21"

                            # 把板子上的画截出来存放在另外一个文件夹�?
                            # originalimage = Image.open("./frame/" + str(c) + ".jpg")  # 之前的完整图
                            # picturelastposition = (picturelastposition[0], picturelastposition[1],
                            #                        picturelastposition[0] + picturelastposition[2],
                            #                        picturelastposition[1] + picturelastposition[3])
                            # picture = originalimage.crop(picturelastposition)
                            # picture.save("./last/lastpicture" + ".jpg")
                            # # 此处调用caffe分类
                            # IMAGE_FILE = osp.abspath(osp.join(osp.dirname(__file__)))
                            # IMAGE_FILE = IMAGE_FILE + '/last/lastpicture' + '.jpg'
                            # result = get_result_five_fold_cross(IMAGE_FILE)
                            # print str(c) + 'vvvvvvvvvvvv'
                            # return result
                            see=see+1;
                            ifcontinue=1
                            break;
                        else:
                            # os.remove("./eye/eye" + str(count) + ".jpg")
                            uncount = uncount + 1;

                            if uncount == count:
                                ifcontinue = 1;
                                nosee+nosee+1;
                                break;
                            continue
                            # else:
                            #     # shutil.rmtree('frame')
                            #     # os.mkdir('frame')
                            #     # shutil.rmtree('head')
                            #     # os.mkdir('head')
                            #     # shutil.rmtree('eye')
                            #     # os.mkdir('eye')
                            #     c = c - 1
                            #     ifcontinue=1;
                            #     if c == 0:
                            #         flag = False
                            #     break;
                else:
                    continue;
        if ifcontinue:
            c = c - 1;
            continue
    print 'seeeeeeeeeeeeeeeeeeeeeeeeeeeee:'+str(see)
    print 'nnnnnnnnnnnnnnnnnnnnnnnnnnosee:'+str(nosee)
    if (see < (picturetime * threshold1)) | (nosee > (threshold2 * picturetime)):
        print '此人不配合'
        return True
    else:
        print '此人配合'
        return False

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


if __name__ == '__main__':
    video_dir = os.path.join(osp.dirname(__file__), 'video_test')
    video_name = 'video.avi'
    im_dir = os.path.join(osp.dirname(__file__), 'frame')
    head_dir = os.path.join(osp.dirname(__file__), 'head')
    eye_dir = os.path.join(osp.dirname(__file__), 'eye')
    if not os.path.exists(im_dir):
        os.mkdir(im_dir)
    vc = cv2.VideoCapture(os.path.join(video_dir, video_name))
    if vc.isOpened():
        totalFrameNumber = vc.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
        print totalFrameNumber
        totalFrameNumber = Test1.interception_video(video_dir, video_name, im_dir, totalFrameNumber)
        numpy = True
        for root, dirs, files in os.walk(im_dir):
            if len(files) == 0:
                numpy = False

        if numpy:
            print 'demo1~~~~~~~~~~~~~~~~~~~~~'
            board_datas = []
            board_datas = demo1.main()
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
                    result4=Uncoorperate2.Unordinary(totalFrameNumber,board_datas,head_datas,eye_datas,eyelet_datas)
                    if result4[1]:
                        print "不配合1"
                    else:

                        result5 = countother(totalFrameNumber, board_datas, head_datas, eye_datas, eyelet_datas,result4[0])
                        if result5:
                            print video_name + '不配合'
                        else:
                            print video_name + '配合'
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

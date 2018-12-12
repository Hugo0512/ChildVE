# -*- coding:utf-8 -*-
#!/usr/bin/env python




import cv2,os
import os.path as osp
import py_faster_rcnn_board.tools.demo1 as demo1
import py_faster_rcnn_head.tools.demo2 as demo2
import py_faster_rcnn_eye.tools.demo3 as demo3
import py_faster_rcnn_lens.tools.demo4 as demo4
import Test2,Test1
import shutil

def getMaxboard(board_datas,totalFrameNumber):
    im_names = []
    for t in range(int(totalFrameNumber)):
        for i in range(len(board_datas)):
            boxs_num = len(board_datas[i])
            # bbbbox=board_datas[i]
            im_name = board_datas[i][0]
            if im_name==str(t) + '.jpg':
                for j in range(1, boxs_num):

                    boxes_data = board_datas[i][j]
                    boxes_class = boxes_data[4]

                    if boxes_class == "maxpicture":
                        # im_names.append(im_name)
                        if boxs_num>=4:
                            for x in range(1, boxs_num):
                                boxes_data1 = board_datas[i][x]
                                boxes_class1 = boxes_data1[4]
                                if boxes_class1 == "picture":
                                    if boxes_data[2]>boxes_data1[2] and boxes_data[3]>boxes_data1[3]:
                                        del board_datas[i][x]
                                        im_names.append(im_name)
                                    else:del board_datas[i][j]
                                    # print '333333333333333333333'
                                    # print board_datas[i]
                                    break
                        else: im_names.append(im_name)


                break

    return im_names

def getPicture(board_datas,totalFrameNumber):

    im_names = []
    for t in range(int(totalFrameNumber)):
        for i in range(len(board_datas)):
            boxs_num = len(board_datas[i])
            im_name = board_datas[i][0]
            if im_name == str(t) + '.jpg':
                for j in range(1, boxs_num):

                    boxes_data = board_datas[i][j]
                    boxes_class = boxes_data[4]

                    if boxes_class == "picture":
                        im_names.append(im_name)
                break

    return im_names


def getHead(im_dir,head_dir,head_datas):
    #get head picture and magnified three times
    # print str(len(head_datas))+" uuuuuuuuuuuuuuuuuuuuuuuuuuuuu"
    # head_datas=demo2.main()
    for i in range(len(head_datas)):
        boxs_num=len(head_datas[i])
        im_name=head_datas[i][0]

        boxes_score=0
        boxes=[]
        for j in range(1,boxs_num):
            boxes_data=head_datas[i][j]
            if boxes_score<boxes_data[5]:

                boxes=(boxes_data[0],boxes_data[1],boxes_data[2],boxes_data[3])
                boxes_score =boxes_data[5]

        # im_dir="H:/xiaochengxu/"
        # head_dir = "H:/xiaochengxu/head"
        if len(boxes)!=0:
            Test2.magnified3(im_dir,im_name,boxes,head_dir)
    return head_datas

    # get eye picture and magnified three times,get eyelet
def getEye(im_dir,eye_dir,eye_datas):
    # eye_datas = demo3.main()
    for i in range(len(eye_datas)):
        boxs_num = len(eye_datas[i])
        im_name = eye_datas[i][0]

        max_score1=0
        max_score2=0
        boxes1=[]
        boxes2=[]
        for j in range(1,boxs_num):

            boxes_data = eye_datas[i][j]
            if max_score1<boxes_data[5]:
                max_score2=max_score1
                boxes2 =boxes1
                max_score1=boxes_data[5]
                boxes1 = (boxes_data[0], boxes_data[1], boxes_data[2], boxes_data[3])
            else:
                if max_score2<boxes_data[5]:
                    max_score2=boxes_data[5]
                    boxes2=(boxes_data[0], boxes_data[1], boxes_data[2], boxes_data[3])


            # im_dir = "H:/xiaochengxu/"
            # eye_dir = "H:/xiaochengxu/head"
        if len(boxes1)!=0:
            Test2.cut_eye(im_dir, im_name, boxes1, eye_dir,1)
        if len(boxes2)!=0:
            Test2.cut_eye(im_dir, im_name, boxes2, eye_dir,2)
    # eyelet_datas=demo4.main()
    return eye_datas


def eyeDirection(eye_dir,eyelet_data):
    im=cv2.imread(eye_dir)
    if len(eyelet_data)>1:
        max_score = 0
        boxes=()
        for i in range(1, len(eyelet_data)):
            if max_score < eyelet_data[i][5]:
                max_score=eyelet_data[i][5]
                boxes = (eyelet_data[i][0], eyelet_data[i][1], eyelet_data[i][2], eyelet_data[i][3])

        height, width = im.shape[:2]
        # max_width=(width/2)*0.9
        # min_width=(width/2)*(1+0.1)
        eyelet_width=boxes[0] +boxes[2]/ 2
        if eyelet_width<(width*0.5):
            result="left"
            return result
        else:
            # if eyelet_width>min_width:
            result="right"
            return result
            # else:
            #     result="centre"
            #     return result
    else:
        return "none"




def picture_position(im_data):
    #os.path.join(im_dir,im_data[0])
    if len(im_data)>1:
        for i in range(1,len(im_data)):

            if im_data[i][4]=="noboard":
                #print "NONE"
                return "NONE"

            elif(im_data[i][4]=="board"):
                for j in range(1,len(im_data)):
                    if((im_data[j][4]=="picture")or(im_data[j][4]=="maxpicture")):
                        lowright_horizonal_board=im_data[i][0]+im_data[i][2]
                        lowright_ordinate_board=im_data[i][1]+im_data[i][3]
                        lowright_horizonal_picture=im_data[j][0]+im_data[j][2]
                        lowright_ordinate_picture=im_data[j][1]+im_data[j][3]
                        if((im_data[i][0]<im_data[j][0]<lowright_horizonal_picture<lowright_horizonal_board+30)&
                            (im_data[i][1]-30<im_data[j][1]<lowright_ordinate_picture<lowright_ordinate_board+30)):
                            board_center=(im_data[i][0]+im_data[i][2]/2,im_data[i][1]+im_data[i][3]/2)
                            picture_center=(im_data[j][0]+im_data[j][2]/2,im_data[j][1]+im_data[j][3]/2)
                            if(picture_center[0]<board_center[0]):
                                #print "left"
                                return "left"
                            elif(picture_center[0]>board_center[0]):
                                #print "right"
                                return "right"
                        else:

                            continue
                    else:
                        continue
            else:
                continue
        #print "NONE"
        return "NONE"

    else:
        return "NONE"



def Cross_eyed(eye_dir,eyelet_datas,im_dir,eyetime,totalFrameNumber):
    threshold1=0.6
    im_names = []
    for root, dirs, files in os.walk(im_dir):
        for file in files:
            print file
            position=file.find('.')
            name=file[:position]
            if os.path.splitext(file)[1] == '.jpg' and int(name)<=totalFrameNumber:
                im_names.append(file)

    num=0
    for im_name in im_names:

        eye_names =[]
        for root, dirs, files in os.walk(eye_dir):
            for eye_name in files:
                if (eye_name==os.path.splitext(im_name)[0]+'_eye1.jpg') or (eye_name==os.path.splitext(im_name)[0]+'_eye2.jpg'):
                    eye_names.append(eye_name)
        if len(eye_names)>1:

            eye_name1=eye_names[0]
            for i in range(len(eyelet_datas)):
                if eye_name1==eyelet_datas[i][0]:
                    eyelet_data=eyelet_datas[i]
            eye_dir1=os.path.join(eye_dir,eye_name1)
            result1=eyeDirection(eye_dir1,eyelet_data)
            # print eye_name1+result1+"xxxxxxxxxxxxxxxx"

            eye_name2 = eye_names[1]
            for i in range(len(eyelet_datas)):
                if eye_name2 == eyelet_datas[i][0]:
                    eyelet_data = eyelet_datas[i]
            eye_dir2 = os.path.join(eye_dir, eye_name2)
            result2 = eyeDirection(eye_dir2, eyelet_data)
            # print eye_name2 + result2 + "xxxxxxxxxxxxxxxx"

            if result1!=result2 and result1!="none" and result2!="none":
                num=num+1
                # print im_name+"ppppppppppppppppppppppppppp"
    # print str(num)+"zzzzzzzzzzzzzzzzzzzzz"
    # print str(len(im_names)) + "zzzzzzzzzzzzzzzzzzzzz"
    if len(im_names)!=0:
        if float(num)/float(eyetime)>threshold1:
            return "cross_eyed"
        else:
            return "no_cross_eyed"
    else:
        return "no_eye"


def seeBoard(eye_dir,board_data,eyelet_datas):
    picture_result=picture_position(board_data)
    im_name=board_data[0]

    eye_names = []
    for root, dirs, files in os.walk(eye_dir):
        for eye_name in files:
            im_name1=im_name.split('.')
            if (eye_name == im_name1[0] + '_eye1.jpg') or (eye_name == im_name1[0] + '_eye2.jpg'):
                eye_names.append(eye_name)
    for eye_name in eye_names:
        eye_dir1 = os.path.join(eye_dir, eye_name)
        i=0
        while eye_name!=eyelet_datas[i][0] and i<164:
            i=i+1
        eyelet_data = eyelet_datas[i]
        if eyeDirection(eye_dir1, eyelet_data)==picture_result:
            return True
    return False


def is_NAN(eye_dir, board_datas, eyelet_datas,totalFrameNumber):
    #threshold2=0.2
    max_names=getMaxboard(board_datas,totalFrameNumber)
    n=0
    # print max_names
    for max_name in max_names:
        i=0
        while max_name!=board_datas[i][0]:
            i=i+1
        board_data=board_datas[i]
        if seeBoard(eye_dir, board_data, eyelet_datas):
            n=n+1
        print max_name+"ggggggggggggggggggggg"
    print 'n='+str(n)
    if len(max_names)!=0:
        #if float(n)/float(len(max_names))<threshold2:
        if n==0:
            return True
        else:
            picture_Names=getPicture(board_datas,totalFrameNumber)
            m=0
            for picture_Name in picture_Names:
                j=0
                while picture_Name!=board_datas[j][0]:
                    j=j+1
                board_data=board_datas[j]
                if seeBoard(eye_dir, board_data, eyelet_datas):
                    m=m+1
                    print picture_Name+'5555555555555'
            print 'm='+str(m)
            # with open('result.txt', 'a') as f:
            #     f.write('\n')
            #     f.write('n='+str(n)+'\t'+'m='+str(m))
            if m==0:
                return True
            else:return False



    else:
        return False

if __name__=='__main__':
    video_dir=os.path.join(osp.dirname(__file__), 'video')
    video_name='CC1220黄科辉3m20150319vou：NA.wmv'
    im_dir=os.path.join(osp.dirname(__file__), 'frame')
    head_dir = os.path.join(osp.dirname(__file__), 'head')
    eye_dir = os.path.join(osp.dirname(__file__), 'eye')
    if not os.path.exists(im_dir):
        os.mkdir(im_dir)
    vc = cv2.VideoCapture(os.path.join(video_dir, video_name))
    if vc.isOpened():
        totalFrameNumber = vc.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
        # totalFrameNumber = findstart.findstart(totalFrameNumber, eye_datas)
        totalFrameNumber = Test1.interception_video(video_dir, video_name, im_dir, totalFrameNumber)
        # totalFrameNumber=1
        print os.path.getsize(im_dir)
        print os.listdir(im_dir)
        numpy=True
        for root, dirs, files in os.walk(im_dir):
            if len(files)==0:
                numpy=False


        if numpy:
            print 'demo1~~~~~~~~~~~~~~~~~~~~~'
            board_datas = []
            board_datas=demo1.main()



            print 'demo2~~~~~~~~~~~~~~~~~~~~~'
            head_datas=demo2.main()
            if not os.path.exists(head_dir):
                os.mkdir(head_dir)
            getHead(im_dir,head_dir,head_datas)
            numpy = True
            for root, dirs, files in os.walk(head_dir):
                if len(files) == 0:
                    numpy = False
            if numpy:
                print 'demo3~~~~~~~~~~~~~~~~~~~~~'
                eye_datas=demo3.main()
                if not os.path.exists(eye_dir):
                    os.mkdir(eye_dir)
                getEye(head_dir,eye_dir,eye_datas)
                numpy = True
                for root, dirs, files in os.walk(eye_dir):
                    if len(files) == 0:
                        numpy = False
                if numpy:
                    print 'demo4~~~~~~~~~~~~~~~~~~~~~'
                    eyelet_datas=demo4.main()
                    result=Cross_eyed(eye_dir, eyelet_datas, im_dir)
                    print result+"bbbbbbbbbbbb"

                    if result!="no_cross_eyed":
                        print result
                    else:

                        if is_NAN(eye_dir, board_datas, eyelet_datas,totalFrameNumber):
                            print "NAN"
                        else:
                            print "no_NAN"

                else:print "no eye"

            else:print "no head"

        else:
            print "no frame"
    else:
        print 'cant find video'
    # shutil.rmtree(eye_dir)
    # os.mkdir(eye_dir)
    # shutil.rmtree(head_dir)
    # os.mkdir(head_dir)
    # shutil.rmtree(im_dir)
    # os.mkdir(im_dir)

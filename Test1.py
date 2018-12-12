#Take the video every frame from start
# -*- coding:utf-8 -*-
__author__ = 'Microcosm'

import os
import os.path as osp
import cv2
import shutil
import matplotlib.image as mpimg



def interception_video(video_dir,video_name,picture_dir,totalFrameNumber):
    video=os.path.join(video_dir,video_name)
    vc = cv2.VideoCapture(video)
    c=1
    #picture_name=video_name[0:len(video_name)-4]
    # for root,dirs,files in os.walk(picture_dir):
    #     if picture_name in dirs:
    #         path = os.path.join(picture_dir,picture_name)
    #         shutil.rmtree(path)


    # picture_dir=os.path.join(picture_dir,picture_name)
    #os.mkdir(picture_dir)
    # totalFrameNumber = vc.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
    if vc.isOpened():
        #rval,frame = vc.read()

        timeF = 1
        shutil.rmtree(picture_dir)
        os.mkdir(picture_dir)
        i=0
        while c<=totalFrameNumber:
            rval, frame = vc.read()
            #cv2.imshow("ddd",frame)
            if (c % timeF == 0):
                name=os.path.join(picture_dir,str(c))
                if frame!=None:
                    cv2.imwrite(name + '.jpg', frame)
                else:
                    i=i+1

            c = c + 1
            cv2.waitKey(1)

        vc.release()
        return totalFrameNumber-i
    else:
        return 0


if __name__=='__main__':
    im_dir = os.path.join(osp.dirname(__file__), 'frame')
    head_dir = os.path.join(osp.dirname(__file__), 'head')
    eye_dir = os.path.join(osp.dirname(__file__), 'eye')
    for rt,dirs,files in os.walk(im_dir):
        for file in files:
            frame=os.path.join(im_dir,file)
            picture=cv2.imread(frame)
            if picture==None:
                print file










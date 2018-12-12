
# -*- coding:utf-8 -*-
#!/usr/bin/python

from PIL import Image
#form PIL import Image
#from PIL.Image import core as image
import cv2,os
import shutil
import os.path as osp
#import nump as np
#import sys
#import os.path


#IMAGE_PATH = sys.arg[1]
#IMAGE_x1 = sys.arg[2]
#IMAGE_y1 = sys.arg[3]
#IMAGE_x2 = sys.arg[4]
#IMAGE_y2 = sys.arg[5]
def magnified3(im_dir,im_name,box,dir):
    im = Image.open(im_dir+"/"+im_name)
    #box = (100,100,400,400)
    im_name=os.path.splitext(im_name)[0]
    box=(box[0],box[1],box[0]+box[2],box[1]+box[3])
    resign = im.crop(box)

    dir1=osp.abspath(osp.join(dir,'..',"cut"))
    dir2=osp.join(dir1,im_name+"_cut.jpg")
    if not os.path.exists(dir1):
        os.mkdir(dir1)
    resign.save(dir2)


    img = cv2.imread(dir2)
    height,width = img.shape[:2]
    res = cv2.resize(img,(3*width,3*height),interpolation = cv2.INTER_CUBIC)

    cv2.imwrite(dir+"/"+im_name+".jpg",res)
    print im_name+" lllllllllllllllllllllllllllllllll"
    shutil.rmtree(dir1)
    os.mkdir(dir1)


def cut_eye(im_dir,im_name,box,dir,num):
    im = Image.open(im_dir + "/" + im_name)
    # box = (100,100,400,400)
    im_name = os.path.splitext(im_name)[0]
    box = (box[0], box[1], box[0] + box[2], box[1] + box[3])
    resign = im.crop(box)
    dir1=osp.abspath(osp.join(dir, '..'))
    dir1 = os.path.join(dir1, "cut", im_name + "_cut.jpg")
    resign.save(dir1)

    img = cv2.imread(dir1)
    height, width = img.shape[:2]
    res = cv2.resize(img, (3 * width, 3 * height), interpolation=cv2.INTER_CUBIC)

    cv2.imwrite(dir + "/" + im_name + "_eye"+str(num)+".jpg", res)
    print im_name + "_eye"+str(num) + " ttttttttttttttttttt"
    # shutil.rmtree(dir1)
    # os.mkdir(dir1)


if __name__=='__main__':
    im_name="IM020998"
    box=(100,100,400,400)
    dir="H:/xiaochengxu"
    magnified3(im_name,box,dir)












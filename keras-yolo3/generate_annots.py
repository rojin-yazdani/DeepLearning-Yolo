import glob
import numpy as np
from random import shuffle

# Loading train images
images_path = "E:/Projects/keras-yolo3-master/Dataset/"
images = glob.glob(images_path + "*.jpg")
#images.sort()
shuffle(images)
num_of_train_imgs = int(1.0 * len(images))-1
count_wrong_files=0
ftrain=open("drone_annots_train.txt", "w")
ftest=open("drone_annots_test.txt", "w")
for k in range(len(images)): 
    img=images[k]
    line = img.replace("\\","/")
    
    box_file_name=line[0:len(img)-4]+".txt"
    fb=open(box_file_name, "r")
    nums=fb.read()    
    nums=nums.replace("\n","").replace(","," ").split(' ')    
    if len(nums) >4 :
        print('######## more than one BB'+line)
    x=float(nums[len(nums)-4])
    y=float(nums[len(nums)-3])
    w=float(nums[len(nums)-2])
    h=float(nums[len(nums)-1])
    x1=int(x-(w/2))
    y1=int(y-(h/2))
    x2=int(x+(w/2))
    y2=int(y+(h/2))    
    #if x1>0 and y1>0 and x1<x2 and y1<y2 and y2<=416 and x2<=416:
    if x1>0 and y1>0 and x1<x2 and y1<y2:
        l=str(x1) + ',' + str(y1) + ',' + str(x2) + ',' + str(y2) + ',0'
        line += (" " + l)
        if k <= num_of_train_imgs:
            ftrain.write(line + '\n')    
        else:
            ftest.write(line + '\n')
    else:
        count_wrong_files+=1
        print("wrong data:"+line) 
print("count_wrong_files:"+str(count_wrong_files))
    
   
ftrain.close()
ftest.close()
'''
for k in range(len(images)): 
    img=images[k]
    line = img.replace("\\","/")
    
    box_file_name=line[0:len(img)-4]+".txt"
    fb=open(box_file_name, "r")
    nums=fb.read()    
    nums=nums.replace("\n","").replace(","," ").split(' ')    
    for i in range(0,len(nums)):
        if (i+1)%4 == 0:
            x=float(nums[i-3])
            y=float(nums[i-2])
            w=float(nums[i-1])
            h=float(nums[i])
            l=str(int(x-(w/2))) + ',' + str(int(y-(w/2))) + ',' + str(int(x+(w/2))) + ',' + str(int(y+(w/2))) + ',0'
            #l=str(int(float(nums[i-3]))) + ',' + str(int(float(nums[i-2]))) + ',' + str(int(float(nums[i-1]))) + ',' + str(int(float(nums[i]))) + ',0'
            line += (" " + l)    
    if k <= num_of_train_imgs:
        ftrain.write(line + '\n')    
    else:
        ftest.write(line + '\n')
    
ftrain.close()
ftest.close()
'''
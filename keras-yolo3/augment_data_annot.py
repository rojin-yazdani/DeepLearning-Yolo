import cv2
import imgaug as ia
import glob
from yolo3 import sequence


INPUT_DIR = 'Dataset'
OUTPUT_DIR = 'augdat'
AUGMENT_SIZE = 6

fh = open("drone_annots_train.txt", "r")
fo = open("drone_augdat_annots_train.txt", "w")
cnt = 0

while True:
    line = fh.readline()
    cnt+=1
    if not line:
        break;
    nums = line.replace("\n","").replace(","," ").split(' ')
    imgName = nums[len(nums)-6]
    x1 = int(nums[len(nums)-5])
    y1 = int(nums[len(nums)-4])
    x2 = int(nums[len(nums)-3])
    y2 = int(nums[len(nums)-2])
    sp = imgName.replace("/"," ").replace("\\"," ").replace("."," ").split(' ')
    seq = sequence.get()
    image = cv2.imread(imgName)    
    for i in range(AUGMENT_SIZE):
        outfile = '%s/%s-%02d.%s' % (OUTPUT_DIR, sp[len(sp)-2], i, sp[len(sp)-1])    
        seq_det = seq.to_deterministic()
        #print("x1={},y1={},x2={},y2={},img={},outfile={}".format(x1,y1,x2,y2,imgName,outfile))     
        _bbs = []
        bb = ia.BoundingBox(x1,y1,x2,y2,label=0)    
        _bbs.append(bb)
        bbs = ia.BoundingBoxesOnImage(_bbs, shape=image.shape)
        image_aug = seq_det.augment_images([image])[0]
        bbs_aug = seq_det.augment_bounding_boxes([bbs])[0].remove_out_of_image().cut_out_of_image()
        cv2.imwrite(outfile, image_aug)
        #writer = Writer(outfile,(x2-x1),(y2-y1))
        for bb in bbs_aug.bounding_boxes:
            #writer.addObject(bb.label,int(bb.x1),int(bb.y1),int(bb.x2),int(bb.y2))   
            outfileInfo = outfile + " " + str(int(bb.x1)) + "," + str(int(bb.y1)) + "," + str(int(bb.x2)) + "," + str(int(bb.y2)) + ",0\n"
            fo.write(outfileInfo)
        #writer.save('%s.xml' % outfile.split('.')[0])
fo.close()
fh.close()


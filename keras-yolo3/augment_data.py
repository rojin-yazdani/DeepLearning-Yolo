import glob
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

# Loading train images
images_path = "E:/Projects/keras-yolo3-master/Dataset/"
images = glob.glob(images_path + "*.jpg")
#images.sort()
ftrain=open("drone_annots_train.txt", "w")
ftest=open("drone_annots_test.txt", "w")
#for k in range(len(images)): 
for k in range(10): 
    img=images[k]
    line = img.replace("\\","/")    

    img = load_img(images[k])  # this is a PIL image
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `preview/` directory
    i = 0
    for batch in datagen.flow(x, batch_size=1,
                          save_to_dir='augdat', save_prefix='cat', save_format='jpeg'):
        i += 1
        if i > 20:
            break  # otherwise the generator would loop indefinitely    
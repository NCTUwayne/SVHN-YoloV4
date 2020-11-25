import os
import cv2
import numpy

head_path = '/home/wayne/darknet-master/data/'
train_path = 'train'
test_path = 'test'
img_path = 'image'
# file = os.listdir(train_path)
file = os.listdir(test_path)
# file.sort()
num_list = [i for i in range(1, 13069)]
# fl = open('train.txt', 'w')
fl = open('test.txt', 'w')

for num in num_list:
    img = str(num) + '.png'
    # name = os.path.join(head_path, img_path)
    name = os.path.join(head_path, test_path)
    name = name + '/' + img + '\n'
    fl.write(name)
fl.close()

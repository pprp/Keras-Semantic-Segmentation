import os
import shutil
from os.path import join

train_file = "data/VOC2007/ImageSets/Segmentation/train.txt"
test_file = "data/VOC2007/ImageSets/Segmentation/val.txt"

jpg_src = "data/VOC2007/JPEGImages"
label_src = "data/VOC2007/SegmentationClass"

train_jpg_dst = "data/train_image"
train_label_dst = "data/train_label"

test_jpg_dst = "data/test_image"
test_label_dst = "data/test_label"

def mk(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

mk(train_jpg_dst)
mk(train_label_dst)
mk(test_jpg_dst)
mk(test_label_dst)



f_train = open(train_file, "r")
f_test = open(test_file, "r")

f_train_content = f_train.readlines()
f_test_content = f_test.readlines()

for line in f_train_content:
    line = line[:-1] + ".png"
    # copy image
    shutil.copy(join(jpg_src, line), join(train_jpg_dst, line))
    # copy label
    shutil.copy(join(label_src, line), join(train_label_dst, line))

for line in f_test_content:
    line = line[:-1] + ".png"
    # copy image
    shutil.copy(join(jpg_src, line), join(test_jpg_dst, line))
    # copy label
    shutil.copy(join(label_src, line), join(test_label_dst, line))

f_train.close()
f_test.close()
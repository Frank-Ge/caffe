import os
import re

path = "//home//frank//repos//py-R-FCN//caffe//include//caffe//layers//"

for fileName in os.listdir(path):
    if re.search("cudnn", fileName):
        print(fileName)
        dotLoc = str.find(fileName, '.')
        newName = fileName[:dotLoc] + '_original' + fileName[dotLoc:]
        os.rename(os.path.join(path, fileName), os.path.join(path, newName))

a = 10

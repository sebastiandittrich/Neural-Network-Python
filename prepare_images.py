from wand.image import Image
import os
import json
import sys

images = []
output = []
path = sys.argv[1]

for filename in os.listdir(path):
    if '.png' in filename:
        img = Image(filename=path + filename)
        img_array = []
        for y in range(img.height):
            for x in range(img.width):
                img_array.append((img[x,y].red + img[x,y].green + img[x,y].blue)/3)
        images.append(img_array)
        if 'a' in filename:
            output.append([1,0,0])
            print(filename + ' is a')
        elif 'b' in filename:
            output.append([0,1,0])
            print(filename + ' is b')
        elif 'c' in filename:
            output.append([0,0,1])
            print(filename + ' is c')
        else:
            output.append([0,0,0])
            print(filename + ' is nothing')

open(path + 'input.json', 'w').write(json.dumps(images))
open(path + 'output.json', 'w').write(json.dumps(output))
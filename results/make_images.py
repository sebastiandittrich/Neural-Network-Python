from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import os
import json
import sys

path = sys.argv[1]

raw_images = json.loads(open('results/'+path).read())

j = 0
for raw_image in raw_images:
    j = j + 1
    draw = Drawing()
    img_matrix = []
    image = Image(height=8, width=8)

    for i in range(8):
        img_matrix.append(raw_image[8*i:8*(i+1)])
    for raw_row in range(len(img_matrix)):
        for raw_pixel in range(len(img_matrix[0])):
            draw.fill_color = Color('srgb(' + str(img_matrix[raw_row][raw_pixel]*255) + ', ' + str(img_matrix[raw_row][raw_pixel]*255) + ', ' + str(img_matrix[raw_row][raw_pixel]*255) + ')')
            draw.color(raw_pixel, raw_row, 'point')
    
    draw(image)
    image.save(filename='results/images/' + str(j) + '.png')

# for filename in os.listdir(path):
#     if '.png' in filename:
#         img = Image(filename=path + filename)
#         img_array = []
#         for y in range(img.height):
#             for x in range(img.width):
#                 img_array.append((img[x,y].red + img[x,y].green + img[x,y].blue)/3)
#         images.append(img_array)
#         if 'a' in filename:
#             output.append([1,0,0])
#             print(filename + ' is a')
#         elif 'b' in filename:
#             output.append([0,1,0])
#             print(filename + ' is b')
#         elif 'c' in filename:
#             output.append([0,0,1])
#             print(filename + ' is c')
#         else:
#             output.append([0,0,0])
#             print(filename + ' is nothing')

# open(path + 'input.json', 'w').write(json.dumps(images))
# open(path + 'output.json', 'w').write(json.dumps(output))
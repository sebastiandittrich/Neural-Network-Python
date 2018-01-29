from sklearn.neural_network import MLPClassifier
import json
from scipy import misc
import numpy as np
import time
import sys
import os

def im_to_array(path):
    return misc.imread(name=path, mode='L')

def prepareimage(array):
    return np.array(misc.imresize(array, (64,64))).flatten().tolist()

def prepare(path):
    x = []
    y = []
    for folder in os.listdir(path):
        cury = json.loads(open(path + '/' + folder + '/output.json', 'r').read())
        for filename in os.listdir(path + '/' + folder):
            if filename != 'output.json':
                im = im_to_array(path + '/' + folder + '/' + filename)
                # Normal
                x.append(prepareimage(im))
                y.append(cury)
                
                # #Rotate
                # x.append(prepareimage(misc.imrotate(im, 45)))
                # y.append(cury)
                # x.append(prepareimage(misc.imrotate(im, 90)))
                # y.append(cury)
                # x.append(prepareimage(misc.imrotate(im, 135)))
                # y.append(cury)
                # x.append(prepareimage(misc.imrotate(im, 180)))
                # y.append(cury)
                # x.append(prepareimage(misc.imrotate(im, 225)))
                # y.append(cury)
                # x.append(prepareimage(misc.imrotate(im, 270)))
                # y.append(cury)
                # x.append(prepareimage(misc.imrotate(im, 315)))
                # y.append(cury)
    return x, y

img_in, output = prepare('traindata')

open('sample.json', 'w').write(json.dumps(img_in))

print(len(img_in), len(img_in[0]))
print(len(output))

nn = MLPClassifier(activation='relu', solver='lbfgs', hidden_layer_sizes=(12), verbose=True)

nn.fit(img_in, output)

while True:
    os.system('scp pi@raspberrypi:/media/pi/UUI1/toffifee/current.jpg . 1>/dev/null 2>&1')
    im = im_to_array('current.jpg')
    pred = nn.predict([prepareimage(im)])[0]
    if pred == 0:
        sys.stdout.write('\rDunkel     ')
    elif pred == 1:
        sys.stdout.write('\rHell     ')
    else:
        sys.stdout.write('\rNothing     ')
    # sys.stdout.write('\r'+str(pred))
    time.sleep(0.5)
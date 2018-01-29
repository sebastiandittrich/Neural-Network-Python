from NeuralNetwork import NeuralNetwork
import json

img_in = json.loads(open('traindata/writing/output.json', 'r').read())
out = json.loads(open('traindata/writing/input.json', 'r').read())

nn = NeuralNetwork([3,64,64,64])
nn.train(img_in,out, 60000)
nn.save_weights('3x64^3_weights_writing.json')
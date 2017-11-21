from NeuralNetwork import NeuralNetwork
import json

img_in = json.loads(open('traindata/input.json', 'r').read())
out = json.loads(open('traindata/output.json', 'r').read())

nn = NeuralNetwork([64*64,64*64,64*64,3])
nn.train(img_in,out, 60000, True)
nn.save_weights('64x64_weights.json')
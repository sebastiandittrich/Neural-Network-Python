from NeuralNetwork import NeuralNetwork
import json

print('Open Input File...')
test_img = [[1,0,1], [1,1,0], [0,1,1], [1,1,1], [0,0,0]]

print('Initialize Neural Network...')
nn = NeuralNetwork('3x64^3_weights_writing.json')
print('Thinking...')
open('results/writing.json', 'w').write(json.dumps(nn.think(test_img).tolist()))

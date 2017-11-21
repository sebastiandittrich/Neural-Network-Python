from NeuralNetwork import NeuralNetwork
import json

print('Open Input File...')
test_img = json.loads(open('tests/input.json', 'r').read())

print('Initialising Neural Network...')
nn = NeuralNetwork('64x64_weights.json')
print('Thinking...')
res = nn.think(test_img)
i = 0
for img in res:
    i = i + 1
    print('\n----- Picture ' + str(i) + ' -----')
    print('A: ' + str(int(img[0]*100)) + '%    ' + 'B: ' + str(int(img[1]*100)) + '%    ' + 'C: ' + str(int(img[2]*100)) + '%')
from NeuralNetwork import NeuralNetwork
import json

english_words = ['Warum']
words = []

for word in english_words:
    words.append([])
    for char in word:
        for bit in bin(ord(char))[2:]:
            words[-1].append(int(bit))
        
for layer in words:
    while len(layer) < 7*20:
        layer.append(0)

print('Initialising Neural Network...')
nn = NeuralNetwork('languages.json')
print('Thinking...')
res = nn.think(words)
print(res)
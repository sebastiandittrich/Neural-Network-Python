from NeuralNetwork import NeuralNetwork

german_words = ['Hallo', 'ich', 'bin', 'Basti', 'und', 'habe', 'gerade', 'langeweile']
english_words = ['Hello', 'i', 'am', 'the', 'boss', 'and', 'have', 'forgotten', 'everything']
languages = []
words = []

for word in german_words:
    words.append([])
    for char in word:
        for bit in bin(ord(char))[2:]:
            words[-1].append(int(bit))
    languages.append([0])

for word in english_words:
    words.append([])
    for char in word:
        for bit in bin(ord(char))[2:]:
            words[-1].append(int(bit))
    languages.append([1])
        
for layer in words:
    while len(layer) < 7*20:
        layer.append(0)


nn = NeuralNetwork([7*20,100,70,1])
nn.train(words, languages, 15000, True)
nn.save_weights('languages.json')
import numpy as np
import json
import sys

class NonLinear:
    @staticmethod
    def sigmoid(x, deriv = False):
        if(deriv==True):
            return x*(1-x)
        return 1/(1+np.exp(-x))

    @staticmethod
    def softmax(x, deriv = False):
        if deriv is True:
            pass
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum(axis=0)

class NeuralNetwork:
    def __init__(self, dimensions, mutate_rate = 0):
        self.mutate_rate = mutate_rate
        if type(dimensions) is str:
            self.load_weights(dimensions)
        else:
            self.__weights = []
            self.__dimensions = dimensions
            self.randomize_weights()

    def load_weights(self, filename):
        self.__weights = json.loads(open(filename, 'r').read())

    def set_weights(self, weights):
        self.__weights = weights

    def get_weights(self):
        return self.__weights

    def save_weights(self, filename):
        prepared_weights = []
        for weight in self.get_weights():
            prepared_weights.append(weight.tolist())
        open(filename, 'w').write(json.dumps(prepared_weights))

    def randomize_weights(self):
        # np.random.seed(1)
        # self.__weights.append(np.array([[0.1,0.2,0.3], [0.4,0.5,0.6], [0.15,0.14,0.13]]))
        # self.__weights.append(np.array([[0.1,0.2,0.3], [0.4,0.5,0.6], [0.15,0.14,0.13]]))
        # self.__weights.append(np.array([[0.45], [0.134], [0.145]]))
        self.__weights = []
        for iter in range(len(self.__dimensions)):
            if iter < len(self.__dimensions) - 1:
                self.__weights.append(2*np.random.random((self.__dimensions[iter],self.__dimensions[iter+1])) - 1)

    def encrypt(self, input, all = False):
        layers = [input]
        for weights in self.get_weights():
            layers.append(NonLinear.sigmoid(np.dot(layers[-1], weights)))
        if all is True: return layers 
        else: return layers[-1]

word = 'HA'

nn = NeuralNetwork((7*len(word), 500, 500, 256))
nn.load_weights('weights.json')

array = [bin(ord(i))[2:] for i in word]

ar = []
for i in array:
    for j in i:
        ar.append(int(j))

print(ar)

raw_enc = nn.encrypt(ar)

enc_arr = []
for i in raw_enc:
    enc_arr.append(int(round(i.item(),0)))

print(enc_arr)

bin_str = '0b'

for i in enc_arr:
    bin_str += str(i)

print(hex(int(bin_str, base=2)))
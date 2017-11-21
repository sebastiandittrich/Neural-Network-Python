import numpy as np
import json
import sys

class NonLinear:
    @staticmethod
    def sigmoid(x, deriv = False):
        if(deriv==True):
            return x*(1-x)
        return 1/(1+np.exp(-x))

class NeuralNetwork:
    def __init__(self, dimensions):
        if type(dimensions) is str:
            self.load_weights(dimensions)
        else:
            self.__weights = []
            self.__dimensions = dimensions
            self.randomize_weights()

    def load_weights(self, filename):
        self.__weights = json.loads(open(filename, 'r').read())

    def get_weights(self):
        return self.__weights

    def save_weights(self, filename):
        prepared_weights = []
        for weight in self.get_weights():
            prepared_weights.append(weight.tolist())
        open(filename, 'w').write(json.dumps(prepared_weights))

    def randomize_weights(self):
        np.random.seed(1)
        # self.__weights.append(np.array([[0.1,0.2,0.3], [0.4,0.5,0.6], [0.15,0.14,0.13]]))
        # self.__weights.append(np.array([[0.1,0.2,0.3], [0.4,0.5,0.6], [0.15,0.14,0.13]]))
        # self.__weights.append(np.array([[0.45], [0.134], [0.145]]))
        self.__weights = []
        for iter in range(len(self.__dimensions)):
            if iter < len(self.__dimensions) - 1:
                self.__weights.append(2*np.random.random((self.__dimensions[iter],self.__dimensions[iter+1])) - 1)

    def think(self, input, all = False):
        layers = [input]
        for weights in self.get_weights():
            layers.append(NonLinear.sigmoid(np.dot(layers[-1], weights)))
        if all is True: return layers 
        else: return layers[-1]

    def get_layer_error(self, next_layer_delta, next_weights):
        return np.array(next_layer_delta).dot(np.array(next_weights).T)

    def get_layer_delta(self, layer, next_layer_delta, next_weights):    
        return self.get_layer_error(next_layer_delta, next_weights) * NonLinear.sigmoid(layer, True)

    def get_last_layer_delta(self, layer, last_layer_error):
        return last_layer_error * NonLinear.sigmoid(layer, True)

    def train(self, input, output, iterations, noisy = False):
        output = np.array(output)
        for iter in range(iterations):
            # Calculate output
            layers = self.think(input, True)

            # Array to store layer deltas
            layer_deltas = []

            last_layer = layers[-1]
            last_layer_delta = self.get_last_layer_delta(last_layer, output - last_layer)
            
            # Insert this delta to the first position of the delta array
            layer_deltas.insert(0, last_layer_delta)

            # Reversing layers for better working
            layers.reverse()

            # Getting Deltas for all layers
            for iter2 in range(len(layers)):
                if iter2 > 0 and iter2 < len(layers) - 1:
                    # layer = layers[iter2]
                    # next_layer_delta = layer_deltas[0]
                    # next_weights = self.get_weights()[-(iter2)]
                    # layer_delta = self.get_layer_delta(layers[iter2], layer_deltas[0], self.get_weights()[-(iter2)])
                    layer_deltas.insert(0, self.get_layer_delta(layers[iter2], layer_deltas[0], self.__weights[-(iter2)]))
            
            # Restore original order
            layers.reverse()

            # Changing weights
            for index in range(len(self.__weights)):
                self.__weights[index] += np.dot(np.array(layers[index]).T, layer_deltas[index])

            if noisy is True:
                sys.stdout.write('\r' + str(int(iter)) + ' Iterations')

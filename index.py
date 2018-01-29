import json
import numpy as np

# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        ret = x*(1-x)
        return ret
    ret = 1/(1+np.exp(-x))
    return ret
    
# input dataset
X = np.array([  [0,0,1],
                [1,1,1],
                [1,0,1],
                [0,1,1], ])
    
# output dataset            
y = np.array([[0,0,1,1]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
# syn0 = 2*np.random.random((3,3)) - 1
# syn1 = 2*np.random.random((3,3)) - 1
# syn2 = 2*np.random.random((3,1)) - 1

syn0 = np.array([[0.1,0.2,0.3], [0.4,0.5,0.6], [0.15,0.14,0.13]])
syn1 = np.array([[0.1,0.2,0.3], [0.4,0.5,0.6], [0.15,0.14,0.13]])
syn2 = np.array([[0.45], [0.134], [0.145]])

def think(l0, syn0):
    return nonlin(np.dot(l0,syn0))

def get_layer_error(next_layer_delta, next_weights):
    return np.array(next_layer_delta).dot(np.array(next_weights).T)

def get_layer_delta(layer, next_layer_delta, next_weights = None):
    if next_weights is None:
        return next_layer_delta * nonlin(layer, True)
    print('Layer Error: ')
    print(get_layer_error(next_layer_delta, next_weights))
    print('Derivate of NonLinear: ')
    print(nonlin(layer, True))
    print('Ergebnis:')
    print(get_layer_error(next_layer_delta, next_weights) * nonlin(layer, True))
    return get_layer_error(next_layer_delta, next_weights) * nonlin(layer, True)

for iter in range(15000):
    l0 = X

    # forward propagation
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
    l3 = nonlin(np.dot(l2, syn2))

    # how much did we miss?
    l3_error = y - l3


    # multiply how much we missed by the 
    # slope of the sigmoid at the values in l1
    l3_delta = get_layer_delta(l3, l3_error)
    print('\nL3 Delta')
    print(l3_delta)

    l2_delta = get_layer_delta(l2, l3_delta, syn2)
    print('L2 Delta')
    print(l2_delta)
    l1_delta = get_layer_delta(l1, l2_delta, syn1)



    # update weights
    syn0 += np.dot(l0.T,l1_delta)
    syn1 += np.dot(l1.T, l2_delta)
    syn2 += np.dot(l2.T, l3_delta)

    # if iter % 3000 == 0:
    #     print('L1: ' + str(l3))
    #     print('Error: ' + str(l1_error))
    #     print('Delta: ' + str(l1_delta))
    #     print('New Weights: ' + str(syn0))

l1 = nonlin(np.dot([0,1,1], syn0))
l2 = nonlin(np.dot(l1, syn1))
l3 = nonlin(np.dot(l2, syn2))
print([[0,1,1], l1, l2, l3])

open('storage.json', 'w').write(json.dumps([syn0.tolist(), syn1.tolist(), syn2.tolist()]))
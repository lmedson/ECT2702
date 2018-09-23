import numpy as np

weights, bias, learn_rate = [0.4, -0.6, 0.6], 0.5, 0.4
d=-1

def fit(weights,inputs,bias,learn_rate):
    aux = np.multiply(weights,inputs)
    u = np.sum(aux) - bias

    if(u>=0):
        category = 1
        print("Classe 1")
    else:
        print("Classe -1")
        category = -1

    for i in range(len(weights)):
        weights[i] = weights[i] + (learn_rate * inputs[i]) * (d - category)
    new_bias = bias + learn_rate * -1 * (d - category)
    print(new_bias)
    print(category)
    return (category, weights, new_bias)


sample = [[0,0,1],[1,1,0]]
sample_outputs = [1,-1]
inputs = [[1,1,1],[0,0,0],[1,0,0],[0,1,1]]

fit(weights,sample[0],bias,learn_rate) 
fit(weights,sample[1],bias,learn_rate)

for i in range(len(inputs)):
    fit(weights,inputs[i],bias,learn_rate) 
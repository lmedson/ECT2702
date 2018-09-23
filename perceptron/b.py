import numpy as np

weights, bias, learn_rate = [0.4, -0.6, 0.6], 0.5, 0.4

def fit(weights,inputs,bias,learn_rate,d):
        # print(weights,inputs)
        aux = np.multiply(weights,inputs)
        # print(aux)
        u = np.sum(aux) - bias
        # print(u)
        if(u>=0):
            category = 1
            # print("Classe 1")
        else:
            # print("Classe -1")
            category = -1
        #new_weights = lambda weights:for i in range(len(weights)):weights[i] = weights[i] + tx_aprend * vetor[i] * (d - y
        for i in range(len(weights)):
            weights[i] = weights[i] + (learn_rate * inputs[i]) * (d - category)

        new_bias = bias + learn_rate * -1 * (d - category)
        print(new_bias)
        return (category, weights, new_bias)


sample = [[0,0,1],[1,1,0]]
sample_outputs = [1,-1]

fit(weights,sample[0],bias,learn_rate,sample_outputs[0]) 
fit(weights,sample[1],bias,learn_rate,sample_outputs[1]) 

inputs = [[1,1,1],[0,0,0],[1,0,0],[0,1,1]]

# fit(weights,[1,1,1],bias,learn_rate) 
# fit(weights,[0,0,0],bias,learn_rate) 
# fit(weights,[1,0,0],bias,learn_rate) 
# fit(weights,[0,1,1],bias,learn_rate) 

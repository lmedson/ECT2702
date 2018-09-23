import numpy as np

weights, bias, learn_rate = [0.4, -0.6, 0.6], 0.5, 0.4


class Perceptron:

    def __init__(self, sample, outputs, learn_rate,bias, epochs=1000):
        self.sample = sample
        self.outputs = outputs
        self.learn_rate = learn_rate
        self.epochs = epochs
        self.bias = bias
        self.num_sample = len(sample)
        self.num_atributes = len(sample[0])
        self.weights = []
        
    def fit(self,weights,inputs,bias,learn_rate):
        print(weights,inputs)
        aux = np.multiply(weights,inputs)
        u = np.sum(aux) - bias
        d = -1
        #print(u)
        if(u>=0):
            category = 1
            print("Classe 1")
        else:
            print("Classe -1")
            category = -1
        #new_weights = lambda weights:for i in range(len(weights)):weights[i] = weights[i] + tx_aprend * vetor[i] * (d - y
        for i in range(len(weights)):
            weights[i] = weights[i] + learn_rate * inputs[i] * (d - category)

        new_bias = bias + learn_rate * -1 * (d - category)
        return (category, weights, new_bias)


sample = [[0,0,1],[1,1,0]]
outputs = [1,-1]
inputs = [[1,1,1],[0,0,0],[1,0,0],[0,1,1]]
perceptron = Perceptron(sample, outputs,bias,learn_rate)
perceptron.fit(weights,[0,0,1],bias,learn_rate) 
perceptron.fit(weights,[1,1,0],bias,learn_rate) 

perceptron.fit(weights,[1,1,1],bias,learn_rate) 
perceptron.fit(weights,[0,0,0],bias,learn_rate) 
perceptron.fit(weights,[1,0,0],bias,learn_rate) 
perceptron.fit(weights,[0,1,1],bias,learn_rate) 

# print(perceptron.category)

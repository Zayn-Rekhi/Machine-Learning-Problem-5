import numpy as np

"""
[Species, area, Country, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006]

"""

def sigmoid(x): return 1/1+np.exp(-x)

def divOfSigmoid(x): return sigmoid(x) * (1 - sigmoid(x))

class Quadratic(object):
    pass

class CrossEntropy(object):
    pass


class network():
    def __init__(self, shape, initializeType, costFunction):
        self.size = len(shape)
        self.shape = shape
        self.cost = costFunction
        if initializeType == "default":
            self.def_initializer()
        elif initializeType == "large":
            self.large_initializer()
    def def_initializer(self):
        """
        This is going to initialize all of the weights and biases
        using the gaussian form of distribution. This Initialization
        is special since we squash down the gaussians by dividing them
        by the square root of the n-1 layer.
        """
        self.weights = [np.random.rand(y, x)/np.sqrt(x) for x, y in zip(self.shape[:-1], self.shape[1:])]
        self.biases = [np.random.randn(x, 1) for x in self.shape[1:]]

    def large_initializer(self):
        """
        This is going to initialize all of the weights and biases
        using the gaussian form of distribution.
        """
        self.weights = [np.random.rand(y, x) for x, y in zip(self.shape[:-1], self.shape[1:])]
        self.biases = [np.random.randn(x, 1) for x in self.shape[1:]]

    def SGD(self, data, epochs, learning_rate=0.1, data_index=100):
        """
        Takes in all of the data and feeds it to the functions that
        process all of it.
        """
        for epoch in range(epochs):
            for dataIndexer in range(0, len(data), data_index):
                feed = data[dataIndexer:dataIndexer+data_index]
                self.update_batch(feed, learning_rate)
                break

    def update_batch(self, data, learning_rate):
        nabla_w = [np.zeros(np.shape(ls)) for ls in self.weights]
        nabla_b = [np.zeros(np.shape(ls)) for ls in self.biases]

        for x, y in data:
            new_weights, new_biases = self.backprop(x, y)

    def backprop(self, x, y):
        nabla_w = [np.zeros(np.shape(ls)) for ls in self.weights]
        nabla_b = [np.zeros(np.shape(ls)) for ls in self.biases]

        value = x
        cost = []
        costNoSig = []
        for weight, bias in zip(self.weights, self.biases):
            computedCost = np.dot(weight, value) + bias
            costNoSig.append(computedCost)
            value = sigmoid(computedCost)
            cost.append(value)
        
        

        

        return None, None



import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

# average1 = []
# average2 = []

# for x in range(0, 1000):
#     array = np.random.randn(5000,5000)
#     value = sigmoid(array)
#     average1.append(np.average(value))
#     value = sigmoid(array/np.sqrt(5000))
#     average2.append(np.average(value))

# print(np.average(average1))
# print(np.average(average2))

shape = [20, 30, 30, 5]
weights = [np.random.randn(x, y)/np.sqrt(y) for x, y in zip(shape[:-1], shape[1:])]
weights1 = [np.random.randn(x, y) for x, y in zip(shape[:-1], shape[1:])]

print(sigmoid(weights[2]))
print(sigmoid(weights1[2]))
# biases = [np.random.randn(x, 1) for x in shape[1:]]

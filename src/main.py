from data import read_data
from network import network, Quadratic, CrossEntropy
import numpy as np

all_data = read_data()
net = network(shape=[11, 100, 100, 12601], initializeType="default", costFunction=Quadratic())
net.SGD(all_data, 100)
import numpy as np
from src import network
net = network.Network([784, 30, 10])
from src import mnist_loader
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
mini_batch = training_data[0:30]
net.SGD(training_data, 30, 10, 3, test_data)
#actMy = net.backprop(mini_batch)
#x = np.asarray([_x.ravel() for _x, _y in mini_batch]).transpose()
# transform to (output x batch_size) matrix
#y = np.asarray([_y.ravel() for _x, _y in mini_batch]).transpose()
#actGood = net.different(x, y)
#print("End")
from src import mnist_loader
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
net1 = network2.Network([784, 30, 10])
net1.SGD(training_data, 30, 10, 3.0, "L1", 5, validation_data, False, True, False, False)


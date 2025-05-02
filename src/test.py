from src import network
net = network.Network([784, 30, 10])
from src import mnist_loader
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
mini_batch = training_data[0:30]
net.backprop(mini_batch)

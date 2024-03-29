# Imports the Pytorch neural network library
import torch.nn as nn

# A class for generating the feed forward neural network
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        # Allows the class to be called elsewhere
        super(NeuralNet, self).__init__()

        # The two hidden layers of the network
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)

        # No activation or softmax (not using 1-hot encoding)
        return out
from lib.Neuron import Neuron
from time import time
import random


class Layer:
    def __init__(self, inputSize: int, layerSize: int):
        self.inputSize = inputSize
        self.size = layerSize
        self.neurons = []
        self.__initNeurons()

    def __createRandom(self, mode):
        if mode == "weights":
            weights = []
            for i in range(self.inputSize):
                weights.append(random.rand(i + time()))
            print(weights)
            return weights

        elif mode == "bias":
            return random.rand(time())

    def __initNeurons(self):
        for i in range(self.size):
            print(f"{i}. Neurons weights: ", end="")
            newNeuron = Neuron(self.inputSize, self.__createRandom("weights"),
                               self.__createRandom("bias"))

            self.neurons.append(newNeuron)

    def next(self, inputs):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.next(inputs))
        return outputs

    def __len__(self):
        return self.size
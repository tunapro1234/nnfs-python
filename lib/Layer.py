from lib.Neuron import Neuron
from time import time
import random


class Layer:
    def __init__(self, inputSize: int, layerSize: int):
        self.inputSize = inputSize
        self.size = layerSize
        self.neurons = []
        self.__initNeurons()

    def __initNeurons(self):
        for i in range(self.size):
            print(f"{i}. Neurons weights: ", end="")
            newNeuron = Neuron(self.inputSize, self.__createRandom("weights"),
                               self.__createRandom("bias"))

            self.neurons.append(newNeuron)

    def __createRandom(self, mode):
        if mode == "weights":
            weights = []
            for i in range(self.inputSize):
                random.seed(i + time())
                weights.append(random.random() * 20)

            print(weights)
            return weights

        elif mode == "bias":
            random.seed(time())

            return random.random() * 20

    def run(self, inputs):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.run(inputs))
        return outputs

    def __len__(self):
        return self.size
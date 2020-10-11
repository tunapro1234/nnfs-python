from lib.Layer import Layer


class NeuralNetwork:
    def __init__(self, inputSize: int, layerSizes):
        # yapf: disable
        self.layerSizes = [layerSizes] if type(layerSizes) == int else layerSizes
        self.inputSize = inputSize

        self.layers = []
        self.__initLayers()

    def __initLayers(self):
        for i, layerSize in enumerate(self.layerSizes):
            inputSize = self.inputSize if i == 0 else self.layerSizes[i - 1]
            newLayer = Layer(inputSize, layerSize)
            self.layers.append(newLayer)

    def run(self, input):
        nextInput = input
        for layer in self.layers:
            nextInput = layer.run(nextInput)
        return nextInput
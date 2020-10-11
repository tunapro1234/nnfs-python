from lib.Layer import Layer

class NeuralNetwork:
    def __init__(self, layerSizes:list):
        self.layers = []
        for layerSize in layerSizes:
            newLayer = Layer()
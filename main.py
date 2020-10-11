from lib.NeuralNetwork import NeuralNetwork

inputLayerSize = 8

X = [list(range(inputLayerSize))]
network = NeuralNetwork(len(X[0]), [8, 6])

for input in X:
    output = network.run(input)
    print(output)
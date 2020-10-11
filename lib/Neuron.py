class Neuron:
    def __init__(self,
                 inputSize: int,
                 weigths: list,
                 bias,
                 activationFunction="ReLU"):

        self.inputSize = inputSize
        self.weigths = weigths
        self.bias = bias

        if activationFunction == "ReLU":
            self.actFunc = self.actRelu

        elif activationFunction == "empty":
            self.actFunc = lambda input: input

        else:
            raise TypeError(
                f"Activation Function: '{self._actFunc}' not found")

    def next(self, inputs):
        if len(inputs) != len(self.weigths):
            raise ValueError("Inputs length must be equal to weigths length")

        final = 0
        for input, weight in zip(inputs, self.weigths):
            final += input * weight
        final += self.bias

        return self.actFunc(final)

    def actRelu(self, input):
        return max(0, input)
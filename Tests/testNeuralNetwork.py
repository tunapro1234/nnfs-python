from lib.NeuralNetwork import NeuralNetwork
import unittest


class TestNeuralNetwork(unittest.TestCase):
    def test_repr(self):
        network = NeuralNetwork(8, [3, 2])
        result = repr(network)

        correctResult = ""
        correctResult += "o o\n"
        correctResult += "o o\n"
        correctResult += "o  "

        self.assertEqual(result, correctResult)

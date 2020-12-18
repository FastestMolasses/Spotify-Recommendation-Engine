import numpy as np

# Included to get reproducible outputs
np.random.seed(0)


class Layer:
    def __init__(self, batchCount: int, neuronsCount: int):
        self.batchCount = batchCount
        self.weights = np.random.rand(batchCount, neuronsCount)
        self.biases = np.zeros((1, neuronsCount))

    def forward(self, inputs: np.array) -> float:
        self.outputs = np.dot(inputs, self.weights) + self.biases
        self.outputs = [Layer.sigmoid(i) for i in self.outputs]

    def getMSE(self, correct: np.array) -> float:
        return np.square(np.subtract(self.output, correct)).mean()

    @staticmethod
    def sigmoid(x: np.array) -> float:
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def sigmoidDeriv(x: np.array):
        return Layer.sigmoid(x) * (1 - Layer.sigmoid(x))


class NeuralNetwork:
    def __init__(self, batchCount: int):
        # 12 possible inputs
        self.inputLayer = Layer(batchCount, 12)
        self.hiddenLayer1 = Layer(12, 12)
        self.hiddenLayer2 = Layer(12, 12)
        # 2 possible outputs
        self.outputLayer = Layer(12, 2)

    def feedForward(self, batchInputs: np.array):
        self.inputLayer.forward(batchInputs)
        self.hiddenLayer1.forward(self.inputLayer.outputs)
        self.outputLayer.forward(self.hiddenLayer1.outputs)
        print(self.outputLayer.outputs)


if __name__ == '__main__':
    batchCount = 1
    neuronCount = 12
    inputs = np.random.rand(batchCount, batchCount)
    n = NeuralNetwork(batchCount)
    n.feedForward(inputs)

import random as rd
import numpy as np
import copy

class ADN :
    def __init__(self, weights = None, bias = None):
        self.weights = copy.deepcopy(weights)
        self.bias = copy.deepcopy(bias)
        self.layerssize = [16, 8, 4]

        if weights == None :
            self.setWeights()
        if bias == None :
            self.setBias()
    
    def setWeights(self):
        self.weights = []
        precNodes = 32

        for nodes in self.layerssize:
            layer = []
            for j in range(precNodes):
                node = [rd.gauss(0, 0.5) for i in range(nodes)]
                layer.append(node)
            self.weights.append(np.matrix(layer))
            precNodes = nodes
    
    def setBias(self):
        self.bias = []
        for layer in self.weights:
            nbrBias = np.size(layer, 1)
            self.bias.append(np.array([rd.gauss(0, 0.5) for i in range(nbrBias)]))

    def getOutput(self, input): #avec input la vision du serpent récupérée dans trainer.py
        weights = []
        for layer in range(len(self.bias)):
            weights.append(np.vstack((self.weights[layer], self.bias[layer])))
        
        outputs = np.matrix([input])
        for layerWeights in weights:
            outputs = self.addBias(outputs)
            outputs = outputs.dot(layerWeights)
            outputs[outputs < 0] = 0  # Relu function
        return outputs

    def addBias(self, val):
        return np.column_stack((val, np.matrix([[1]])))

    def mix(self, other, mutationRate):
        newWeights = self.crossover(self.weights, other.weights)
        newBias = self.crossover(self.bias, other.bias)
        newAdn = ADN(newWeights, newBias)
        newAdn.mutate(mutationRate)
        return newAdn

    def crossover(self, adn1, adn2):
        res = []
        for layer in range(len(adn1)):
            res.append(self.crossLayer(adn1[layer], adn2[layer]))
        return res

    def crossLayer(self, layer1, layer2):
        lineCut = rd.randint(0, np.size(layer1, axis=0) - 1)
        if len(layer1.shape) == 1:  # the layer is only one dimension   
            return np.hstack((layer1[:lineCut], layer2[lineCut:]))
        columnCut = rd.randint(0, np.size(layer1, axis=1) - 1)
        res = np.vstack(
            (
                layer1[:lineCut],
                np.hstack(
                    (layer1[lineCut, :columnCut], layer2[lineCut, columnCut:])
                ),
                layer2[lineCut + 1 :],
            )
        )
        return res

    def mutate_layer(self, layer, mutationRate=0.01):
        with np.nditer(layer, op_flags=["readwrite"]) as it:
            for x in it:
                if rd.random() < mutationRate:
                    x[...] += min(max(rd.gauss(0, 0.5), -1), 1)

    def mutate(self, mutationRate=0.01):
        # Mutation of the weights
        for layer in self.weights:
            self.mutate_layer(layer, mutationRate)

        # Mutation of the bias
        for layer in self.bias:
            self.mutate_layer(layer, mutationRate)


if __name__ == "__main__" : 
    adn = ADN()
    adn.getOutput([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
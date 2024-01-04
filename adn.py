import random as rd
import numpy as np

class ADN :
    def __init__(self):
        self.weights = []
        self.bias = []
        self.layerssize = [16, 8, 4]

        self.setWeights()
        self.setBias()
    
    def setWeights(self):
        precNodes = 32

        for nodes in self.layerssize:
            layer = []
            for j in range(precNodes):
                node = [rd.gauss(0, 0.5) for i in range(nodes)]
                layer.append(node)
            self.weights.append(layer)
            precNodes = nodes
    
    def setBias(self):
        for layer in self.weights:
            nbrBias = np.size(layer, 1)
            self.bias.append([rd.gauss(0, 0.5) for i in range(nbrBias)])

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
        """
        Add one element to the column vector to take into account the bias.
        val (list): the column vector
        """
        return np.column_stack((val, np.matrix([[1]])))



if __name__ == "__main__" : 
    adn = ADN()
    adn.getOutput([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
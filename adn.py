import random as rd
import numpy as np
import copy

class ADN :
    def __init__(self, weights = None, bias = None): #Initialise les poids et les biais du réseau de neurones
        self.weights = copy.deepcopy(weights)
        self.bias = copy.deepcopy(bias)
        self.layerssize = [20, 12, 4]

        if weights == None :
            self.setWeights()
        if bias == None :
            self.setBias()
    
    def setWeights(self): # Initialise les poids du réseau de neurones
        self.weights = []
        precNodes = 32

        for nodes in self.layerssize:
            layer = []
            for j in range(precNodes):
                node = [rd.gauss(0, 1) for i in range(nodes)]
                layer.append(node)
            self.weights.append(np.matrix(layer))
            precNodes = nodes
    
    def setBias(self): # Initialise les biais du réseau de neurones
        self.bias = []
        for layer in self.weights:
            nbrBias = np.size(layer, 1)
            self.bias.append(np.array([rd.gauss(0, 1) for i in range(nbrBias)]))

    def relu(self, x): # Fonction d'activation relu
        return np.maximum(0, x)
 
    def sigmoid(self, x): # Fonction d'activation sigmoid 
        return 1 / (1 + np.exp(-x))
    
    def tanh(self, x): # Fonction d'activation tanh
        return np.tanh(x)

    def getOutput(self, input): #avec input la vision du serpent récupérée dans trainer.py, c'est la fonction de "fast forward"
        output = input
        for i in range(len(self.weights)):
            output = self.relu(np.dot(output, self.weights[i]) + self.bias[i])
        return output

    def mix(self, other, mutationRate): # Fonctions de croisement et de mutation
        newWeights = self.crossover(self.weights, other.weights)
        newBias = self.crossover(self.bias, other.bias)
        newAdn = ADN(newWeights, newBias)
        newAdn.mutate(mutationRate)
        return newAdn

    def crossover(self, adn1, adn2): # Fonction de croisement des poids et des biais
        res = []
        for layer in range(len(adn1)):
            res.append(self.crossLayer(adn1[layer], adn2[layer]))
        return res

    def crossLayer(self, layer1, layer2): # Fonction de croisement des poids et des biais
        lineCut = rd.randint(0, np.size(layer1, axis=0) - 1)
        if len(layer1.shape) == 1: 
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

    def mutate_layer(self, layer, mutationRate=0.01): # Fonction pour choisir aléatoirement les poids et les biais à muter
        with np.nditer(layer, op_flags=["readwrite"]) as it:
            for x in it:
                if rd.random() < mutationRate:
                    x[...] += min(max(rd.gauss(0, 0.5), -1), 1)

    def mutate(self, mutationRate=0.01): #lance la mutation des poids et des biais
        for layer in self.weights:
            self.mutate_layer(layer, mutationRate)

        for layer in self.bias:
            self.mutate_layer(layer, mutationRate)
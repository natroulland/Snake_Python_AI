from math import exp, tanh

def sigmoide(x):
    return 1/(1+exp(-x))

def tangente(x):
    return 1.7159*tanh((2/3)*x)
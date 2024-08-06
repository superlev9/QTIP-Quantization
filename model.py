import numpy as np

class Model:
    def __init__(self, weights):
        self.weights = weights
    
    def get_weights(self):
        return self.weights
    
    def set_weights(self, weights):
        self.weights = weights

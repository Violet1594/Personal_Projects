from sklearn.linear_model import LinearRegression
import numpy as np
import itertools
import math

class PatternPredictor:
    def __init__(self):
        self.model = LinearRegression()

    def train_model(self, X, y):
        self.model.fit(X, y)

    def predict_next(self, sequence):
        last_two = np.array(sequence[-2:]).reshape(1, -1)  # Use the last two values
        return self.model.predict(last_two)[0]

    def evaluate_model(self, X_test, y_test):
        return self.model.score(X_test, y_test)
    
    def generate_combinations(self, elements, r):
        return list(itertools.combinations(elements, r))
    
    def generate_permutations(self, elements):
        return list(itertools.permutations(elements))
    
    def generate_binomial_coefficients(self, n, k_max):
        return [math.comb(n, k) for k in range(k_max + 1)]
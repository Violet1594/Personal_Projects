import numpy as np

import itertools
import math

class SequenceGenerator:
    def generate_arithmetic_sequence(self, start, diff, length):
        return [start + i * diff for i in range(length)]
    
    def generate_fibonacci_sequence(self, length):
        sequence = [1, 1]
        for i in range(2, length):
            sequence.append(sequence[-1] + sequence[-2])
        return sequence
    
    def generate_geometric_sequence(self, start, ratio, length):
        return [start * (ratio ** i) for i in range(length)]
    
    def generate_combinations(self, elements, r):
        # Generates all combinations of `r` elements from `elements`
        return list(itertools.combinations(elements, r))
    
    def generate_permutations(self, elements):
        # Generates all permutations of `elements`
        return list(itertools.permutations(elements))
    
    def generate_binomial_coefficients(self, n, k_max):
        # Generates binomial coefficients (n choose k) for k in range(k_max + 1)
        return [math.comb(n, k) for k in range(k_max + 1)]
    
    def generate_training_data(self, sequence, window_size=2):
        X, y = [], []
        for i in range(len(sequence) - window_size):
            X.append(sequence[i:i + window_size])
            y.append(sequence[i + window_size])
        return X, y
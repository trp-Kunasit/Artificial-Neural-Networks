"""
Teerapong Kunasit
Problem: 6
"""
import numpy as np

def activation(w, b, x):
    return np.matmul(w, x) + b
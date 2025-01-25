"""
Teerapong Kunasit
Problem: 4
"""
import numpy as np

def act(w, x):
    exp_x = np.exp(-np.abs(x))
    return np.matmul(w, exp_x)
"""
Teerapong Kunasit
Problem: 3
"""
import numpy as np

def hf(x):
    return 1 / (1 + np.power(2, -x))

def netz(c, x):
    return c * hf(x)  
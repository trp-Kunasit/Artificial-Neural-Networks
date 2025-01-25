"""
Teerapong Kunasit
Problem: 5
"""
import numpy as np

def acth(w, x):
    tanh_x = np.tanh(x) 
    return np.matmul(w, tanh_x)
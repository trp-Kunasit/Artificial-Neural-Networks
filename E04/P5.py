import numpy as np

def polyM(x, w):
    """Evaluate degree-M polynomial"""
    return float(sum(w[i, 0] * (x ** i) for i in range(len(w))))

def polyM_MSE(XY, w):
    """Calculate mean squared error"""
    errors = np.array([polyM(x, w) - y for x, y in XY])
    return float(np.mean(errors ** 2))

def polyM_grad(XY, w):
    """Calculate gradient of MSE"""
    N = XY.shape[0]
    M = w.shape[0]
    grad = np.zeros((M, 1))
    
    for x, y in XY:
        error = polyM(x, w) - y
        for i in range(M):
            grad[i, 0] += 2 * error * (x ** i)
            
    return grad / N

def polyM_traingd(XY, w0, lr, epochs):
    """Train using gradient descent"""
    w = w0.copy()
    for _ in range(epochs):
        grad = polyM_grad(XY, w)
        w -= lr * grad
    return w

if __name__ == "__main__":
    DX = [0.000, 0.111, 0.222, 0.333, 0.444, 0.556, 0.667, 0.778, 0.889, 1]
    DY = [-0.028, 0.988, 1.387, 1.625, 1.089, 0.713, 0.328, 0.535, 1.112, 2.004]
    DXY = np.array([DX, DY]).T
    w = np.array([1, 2, 1.5, -0.3, 1.2]).reshape((-1,1))
    print('polyM =', polyM(3, w))
    print('polyM_MSE =', polyM_MSE(DXY, w))
    print('polyM_grad =\n', polyM_grad(DXY, w))
    w0 = w
    wt3 = polyM_traingd(DXY, w0, lr=1e-2, epochs=3)
    print('wt3 =\n', wt3)
import numpy as np

def polyM(x, w):
  
    y = sum(w[i, 0] * (x ** i) for i in range(w.shape[0]))
    return y

def polyM_MSE(XY, w):
    X = XY[:,0]
    Y = XY[:,1]

    predict_X = polyM(Y, w)

    result = np.mean((X-predict_X)**2)

    return result

def polyM_grad(XY, w):
    N = len(XY)
    M = len(w)
    grad = np.zeros(M)

    for i in range(N):
        X = XY[i:,0]
        Y = XY[i:,1]
        error = polyM(X, w) - Y
        for j in range(M + 1):
            grad[j, 0] += (2 / N) * error * (X ** j)

    return grad

def polyM_traingd(XY, w0, lr, epochs):
   
    w = w0.copy()
    for epoch in range(epochs):
        grad = polyM_grad(XY, w)
        w -= lr * grad
    return w


if __name__ == "__main__":
    DX = [0.000, 0.111, 0.222, 0.333, 0.444, 0.556, 0.667, 0.778, 0.889, 1]
    DY = [-0.028, 0.988, 1.387, 1.625, 1.089, 0.713, 0.328, 0.535, 1.112, 2.004]
    DXY = np.array([DX, DY]).T
    w = np.array([1, 2, 1.5, -0.3, 1.2]).reshape((-1, 1))

    print('polyM =', polyM(3, w))
    print('polyM_MSE =', polyM_MSE(DXY, w))
    print('polyM_grad =\n', polyM_grad(DXY, w))

    w0 = w
    wt3 = polyM_traingd(DXY, w0, lr=1e-2, epochs=3)
    print('wt3 =\n', wt3)

import numpy as np

def polyM(x, w):
    len = w.shape[0]
    y = 0
    for i in range(len):
        y += w[i, 0] * x ** i
    return y

def polyM_MSE(xy, w):
    x = xy[:,0]
    y = xy[:,1]

    result = np.mean((polyM(x, w) - y) ** 2)
    return result

def polyM_grad(xy, w):
    x = xy[:,0]
    y = xy[:,1]
    len_w = len(w)
    result = np.zeros((len_w, 1))
    for i in range(len_w):
        result[i] = np.mean(2 * (polyM(x, w) - y) * x ** i)

    return result

def polyM_traingd(xy, w0, lr, epochs):
    w = w0
    for i in range(epochs):
        w = w - lr * polyM_grad(xy, w)
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
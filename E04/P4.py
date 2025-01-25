import numpy as np

def poly1(x, w):
    return w[0, 0] + w[1, 0] * x

def poly1_MSE(HQ, w):
    
    N = HQ.shape[0]
    errors = [(poly1(x, w) - y)**2 for y, x in HQ]
    return np.mean(errors)

def poly1_grad(HQ, w):
    N = HQ.shape[0]
    grad = np.zeros((2, 1))
    for y, x in HQ:
        error = poly1(x, w) - y
        grad[0, 0] += error
        grad[1, 0] += error * x
    return (2 / N) * grad

def poly1_traingd(HQ, w0, lr, epochs):
    w = w0.copy()
    for _ in range(epochs):
        grad = poly1_grad(HQ, w)
        w -= lr * grad
    return w

def approx_head(Q):
    Pipe = np.array([[20.545, 28.500, 30.142, 35.603], [160, 256, 272, 320]]).T

    Q_train = Pipe[:, 1]
    H_train = Pipe[:, 0]
    mu_Q = Q_train.mean()
    sigma_Q = Q_train.std()
    q_train = (Q_train - mu_Q) / sigma_Q

    HQ = np.column_stack((H_train, q_train))

    w0 = np.random.random((2, 1))

    lr = 1e-2
    epochs = 1000
    w_trained = poly1_traingd(HQ, w0, lr, epochs)

    q = (Q - mu_Q) / sigma_Q
    H_pred = poly1(q, w_trained)
    return H_pred

if __name__ == "__main__":
    Pipe = np.array([[20.545, 28.500, 30.142, 35.603], [160, 256, 272, 320]]).T
    w = np.array([2, 0.1]).reshape((2,1))
    
    print('poly1 =', poly1(160, w))
    print('poly1_MSE =\n', poly1_MSE(Pipe, w))
    print('poly1_grad =\n', poly1_grad(Pipe, w))

    w0 = np.random.random(2).reshape((2,1))
    lr = 0.00001
    epochs = 500
    w_gd = poly1_traingd(Pipe, w0, lr, epochs)
    print('poly1_traingd =\n', w_gd)
    
    for Q in Pipe[:,1]:
        H = approx_head(Q)
        print('Q = {:.3f} , H ~ {:.3f}'.format(Q,H))
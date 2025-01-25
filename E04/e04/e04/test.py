import numpy as np 

def poly1(x, w):
    return w[0, 0] + w[1, 0] * x

def poly1_MSE(HQ, w):
    H, Q = HQ[:, 0], HQ[:, 1]
    return np.mean((poly1(Q, w) - H)**2)

def poly1_grad(HQ, w):
    H, Q = HQ[:, 0], HQ[:, 1]
    Xn = poly1(Q, w)
    grad_w0 = -2 * np.mean(H - Xn)
    grad_w1 = -2 * np.mean((H - Xn) * Q)
    return np.array([[grad_w0], [grad_w1]])

def poly1_traingd(HQ, w0, lr, epochs):
    w = w0.copy()
    for _ in range(epochs):
        grad = poly1_grad(HQ, w)
        w -= lr * grad
    with open("traingd", "w+") as f:
        for i in range(len(w)):
            f.write("{}".format(w[i, 0]))
            if i != len(w) - 1: 
                f.write(",")
    #np.save("train.npy", w)
    return w

def poly_traingd(HQ, w0, lr, epochs):
    w = w0.copy()
    for _ in range(epochs):
        grad = poly1_grad(HQ, w)
        w -= lr * grad
    with open("traingd", "w+") as f:
        for i in range(len(w)):
            f.write("{}".format(w[i, 0]))
            if i != len(w) - 1: 
                f.write(",")
    #np.save("train.npy", w)
    return w

def approx_head(Q):
    with open("traingd", "r+") as f:
        lines = f.read()
        initIN = np.array(lines.split(","))
        initIN = np.float64(initIN).reshape(-1, 1)
    #initIN = np.load("train.npy")

    w_opt = np.array([[4.0], [0.09999]])
    return poly1(Q, w_opt)

if __name__ == "__main__":
    Pipe = np.array([[20.545, 28.500, 30.142, 35.603], [160, 256, 272, 320]]).T 
    w = np.array([2, 0.1]).reshape((2,1)) 
    print('poly1 =', poly1(160, w)) 
    print('poly1_MSE =\n', poly1_MSE(Pipe, w)) 
    print('poly1_grad =\n', poly1_grad(Pipe, w)) 
    w0 = np.random.random(2).reshape((2,1)) 
    lr = 0.00001
    epochs = 500 
    # print("-------->", w0, "<------------")
    w_gd = poly1_traingd(Pipe, w0, lr, epochs) 
    print('poly1_traingd =\n', w_gd) 

    for Q in Pipe[:,1]: 
        H = approx_head(Q) 
        print('Q = {:.3f} , H ~ {:.3f}'.format(Q,H))
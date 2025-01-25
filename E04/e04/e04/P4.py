import numpy as np

def poly1(x, w):
    return (w[0, 0] + w[1, 0]*x)

def poly1_MSE(HQ, w):
    H = HQ[:,0]
    Q = HQ[:,1]

    predict_H = poly1(Q, w)

    result = np.mean((H-predict_H)**2)

    return result

def poly1_grad(HQ, w):
    # https://mccormickml.com/2014/03/04/gradient-descent-derivation/
    H = HQ[:,0]
    Q = HQ[:,1]

    predict_H = poly1(Q, w)

    result = np.zeros((2,1))
    grad1 = np.mean(predict_H - H)
    grad2 = np.mean((predict_H - H) * Q)
    # multiply 2 because it one half
    result[0] = 2 * grad1
    result[1] = 2 * grad2
    
    return result

def poly1_traingd(HQ, w0, lr, epochs):
    w = w0
    H = HQ[:,0]
    Q = HQ[:,1]

    for i in range(epochs):
        w = w - lr * poly1_grad(HQ, w)

    with open('save_w.txt', 'w') as f:
        f.write(str(w[0,0]) + '\n')
        f.write(str(w[1,0]))
    
    # weights = polyfit(Q, H)
    # with open('save_w2.txt', 'w') as f:
    #     f.write(str(w[0,0]) + '\n')
    #     f.write(str(w[1,0]))

    return w
    
def approx_head(Q):
    w = np.array([[5.5], [0.092]])
    # with open('save_w2.txt', 'r') as f:
    #     data = f.readlines()
    #     w0 = data[0].strip()
    #     w1 = data[1].strip()
    #     w.fill(float(w0))
    #     w.fill(float(w1))
    H = poly1(Q, w)
    # H = polyvalue(Q, w).item()
    return H

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
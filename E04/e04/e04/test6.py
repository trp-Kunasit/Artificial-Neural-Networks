import numpy as np

def polyM(x, w):
    ans = 0
    for i in range(len(w)):
        ans += w[i, 0] * (x ** i)
    return np.float64(ans)

def polyM_MSE(DXY, w):
    DX, DY = DXY[:, 0], DXY[:, 1]
    return np.mean((polyM(DX, w) - DY)**2)

def polyM_grad(DXY, w):
    DX, DY = DXY[:, 0], DXY[:, 1]
    ans = np.zeros_like(w)

    for i in range(len(w)):
        ans[i, 0] = -2 * np.mean((DY - np.array([polyM(xi, w) for xi in DX])) * (DX ** i))

    return ans

def polyM_traingd(XY, w0, lr, epochs):
    w = w0.copy()
    for _ in range(epochs):
        grad = polyM_grad(XY, w)
        w -= lr * grad
    return w

def normalize(Q):
    mu, sigma = np.mean(Q), np.std(Q)
    return (Q - mu) / sigma, mu, sigma

def denormalize(q, mu, sigma):
    return q * sigma + mu

# 3. Deployable function
def pump_head(Q):
    # Load saved model parameters
    # w_opt = np.load("pump_weights.npy")  # Trained weights

    # mu, sigma = np.load("pump_norm_params.npy")  # Normalization parameters
    # print(w_opt)
    # print(mu)
    # print(sigma)

    # # part use 
    w_opt = np.array([[40.68372592],[-9.33611682],[-3.52221897],[-0.77113024],[-0.05608777],[ 0.06242701]])
    mu, sigma = 350.0, 87.69192333232017

    # normalize
    q = (Q - mu) / sigma

    return polyM(q, w_opt)

if __name__ == "__main__":
    TrainQH = np.load("P6_TrainQHv4.npy")
    Q, H = TrainQH[:, 0], TrainQH[:, 1]

    # Normalize flow rate
    q, mu, sigma = normalize(Q)
    norm_data = np.column_stack((q, H))

    # Train polynomial model
    degree = 5  # Degree of the polynomial
    w0 = np.random.random((degree + 1, 1))  # Initial random weights
    lr = 0.01  # Learning rate
    epochs = 20000  # Number of epochs
    w_opt = polyM_traingd(norm_data, w0, lr, epochs)

    # Save the trained model
    np.save("pump_weights.npy", w_opt)
    np.save("pump_norm_params.npy", [mu, sigma])

    # Test the deployable function
    test_Q = 205
    predicted_H = pump_head(test_Q)
    print(f"For Q = {test_Q}, Predicted H = {predicted_H:.3f}")

    temp = 0
    print(len(Q))
    for i in range(len(Q)):
        temp += (H[i] - pump_head(Q[i])) ** 2
    print("temp = ", temp)

    test_Q = 203.8
    predicted_H = pump_head(test_Q)
    print(f"For Q = {test_Q}, Predicted H = {predicted_H:.3f}")
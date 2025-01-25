import numpy as np

def loss(uvec):
    A = np.array([[2,1],[1.5,3]])
    b = np.array([[-7],[9]])
    return float(uvec.T @ A @ uvec + b.T @ uvec)

def grad(uvec):
    A = np.array([[2,1],[1.5,3]])
    b = np.array([[-7],[9]])
    return (A + A.T)@uvec + b
    
def minimizer(u0, lr, N):
    u = u0
    for _ in range(N):
        g = grad(u)
        u = u - lr*g
    return u

if __name__ == "__main__":
    import numpy as np
    u0 = np.array([[0],[0]])
    uz = minimizer(u0, lr=0.1, N=500)
    print('type=', type(uz))
    print('shape=', uz.shape)
    print(': u*=', uz)
    print(': loss(u*)=', loss(uz))
    print(': grad(u*)=', grad(uz))

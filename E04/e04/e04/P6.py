import numpy as np

def pump_head(Q):
    Q0 = Q
    file = np.load('P6_TrainQHv4.npy')
    Q_f = file[:, 0]
    H = file[:, 1]

    mean = np.mean(Q_f)
    std = np.std(Q_f)

    q = (Q_f - mean) / std
    q0 = (Q0 - mean) / std
    w = np.polyfit(q, H, 5)

    predict_H = np.polyval(w, q0)  
    return predict_H

if __name__ == "__main__":
    TrainQH = np.load('P6_TrainQHv4.npy')
    print('Q =', (3*"{:.1f} ;").format(*TrainQH[:3, 0]), "...") 
    print('H =', (3*"{:.1f} ;").format(*TrainQH[:3, 1]), "...") 
    Q = 205
    H = pump_head(Q) 
    print('For Q =', Q, '; H =', H) 
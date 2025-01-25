import numpy as np

def predict_wellbeing(w, k, s, t, p, h):

    table1 = np.array([
        [8, 5, 5, 5, 5, 5],  # Anan
        [8, 8, 7, 8, 7, 7],  # Bhucha
        [6, 9, 6, 6, 6, 6],  # Chandra
        [6, 6, 8, 6, 6, 6],  # Denchai
        [6, 6, 6, 9, 6, 6],  # Ekkamol
        [8, 8, 8, 8, 6, 8],  # Feungfa
        [7, 7, 7, 7, 7, 5]   # Gluaykai
    ])

    table2 = np.array([5.69, 7.61, 6.81, 6.18, 6.33, 7.72, 6.68])
    weights, _, _, _ = np.linalg.lstsq(table1, table2, rcond=None)
    print("weights", weights)

    return weights[0]*w + weights[1]*k + weights[2]*s + weights[3]*t + weights[4]*p + weights[5]*h

if __name__ == "__main__":
    yhat = predict_wellbeing(8, 7, 6, 8, 6, 7)

    print(yhat) 
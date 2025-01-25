import numpy as np

def train_model():
    X = np.array([
        [8, 5, 5, 5, 5, 5],   
        [8, 8, 7, 8, 7, 7],   
        [6, 9, 6, 6, 6, 6],   
        [6, 6, 8, 6, 6, 6],   
        [6, 6, 6, 9, 6, 6],   
        [8, 8, 8, 8, 6, 8],   
        [7, 7, 7, 7, 7, 5]    
    ])
    y = np.array([5.69, 7.61, 6.81, 6.18, 6.33, 7.72, 6.68])  # Actual well-being

    X_with_intercept = np.hstack([np.ones((X.shape[0], 1)), X])

    weights = np.linalg.inv(X_with_intercept.T @ X_with_intercept) @ X_with_intercept.T @ y
    return weights

weights = train_model()

def predict_wellbeing(w, k, s, t, p, h):
    factors = np.array([1, w, k, s, t, p, h])  
    predicted_score = np.dot(weights, factors)
    return predicted_score

if __name__ == "__main__":
 yhat = predict_wellbeing(8, 7, 6, 8, 6, 7)
 print(yhat)

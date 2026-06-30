import numpy as np

class LogisticRegressionFromScratch:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.lr = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = None

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        num_samples, num_features = X.shape
        # Initialize weights and bias to zeros
        self.weights = np.zeros(num_features)
        self.bias = 0

        # Gradient Descent
        for i in range(self.iterations):
            # Approximate y with linear combination, then apply sigmoid
            linear_model = np.dot(X, self.weights) + self.bias
            y_predicted = self._sigmoid(linear_model)

            # Compute gradients
            dw = (1 / num_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / num_samples) * np.sum(y_predicted - y)

            # Update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            
            # Optional: Print loss every 100 iterations to track convergence
            if i % 100 == 0:
                loss = - (1 / num_samples) * np.sum(y * np.log(y_predicted + 1e-15) + (1 - y) * np.log(1 - y_predicted + 1e-15))
                print(f"Iteration {i}: Loss = {loss:.4f}")

    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_predicted = self._sigmoid(linear_model)
        # Convert probabilities to binary class (0 or 1)
        return [1 if i > 0.5 else 0 for i in y_predicted]

# --- Verification & Dummy Data ---
if __name__ == "__main__":
    print("--- Testing Logistic Regression Implementation ---")
    
    # Dummy Dataset: Hours Studied vs Pass (1) or Fail (0)
    # Features: [Hours Studied, Sleep Hours]
    X_train = np.array([[2, 5], [3, 6], [5, 7], [7, 8], [8, 9], [9, 6]])
    y_train = np.array([0, 0, 0, 1, 1, 1])

    # Train model
    model = LogisticRegressionFromScratch(learning_rate=0.1, iterations=500)
    model.fit(X_train, y_train)

    # Predict
    predictions = model.predict(X_train)
    
    # Calculate Accuracy
    accuracy = np.mean(predictions == y_train) * 100
    
    print("\n--- Results ---")
    print(f"Target:      {list(y_train)}")
    print(f"Predictions: {predictions}")
    print(f"Final Model Accuracy: {accuracy:.2f}%")
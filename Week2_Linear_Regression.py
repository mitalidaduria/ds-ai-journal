# =====================================================================
# LINEAR REGRESSION FROM SCRATCH & SKLEARN COMPARISON
# We're finding the straight line through our data points that 
# minimises the average squared distance between the line and each point. 
# The slope tells us: for each additional hour, how does the predicted 
# transaction amount change?
# =====================================================================

import numpy as np  # Import NumPy for efficient matrix math and array operations
from sklearn.linear_model import LinearRegression  # Import sklearn's built-in model to cross-check our work

# --- STEP 1: PREPARE DUMMY DATA ---
# X represents the independent variable: 'hour-of-day' (e.g., 9 AM, 12 PM, 3 PM, 6 PM)
X = np.array([[9], [12], [15], [18]]) 
# y represents the dependent variable: 'payment transaction amount' in dollars
y = np.array([15, 30, 45, 55]) 

# --- STEP 2: LINEAR REGRESSION FROM SCRATCH (THE NORMAL EQUATION) ---
# To include the intercept (bias term), we must add a column of 1s to our input matrix X
X_bias = np.c_[np.ones((X.shape[0], 1)), X] 

# Calculate the optimal parameters (theta) using the closed-form Normal Equation: theta = (XᵀX)⁻¹Xᵀy
# X_bias.T transposes the matrix; np.linalg.inv computes the matrix inverse; @ performs matrix multiplication
theta = np.linalg.inv(X_bias.T @ X_bias) @ X_bias.T @ y 

# Extract the intercept (the value of y when X is 0) which is the first element in our theta array
intercept_scratch = theta[0] 
# Extract the slope (coefficient) which is the second element in our theta array
slope_scratch = theta[1] 

# Generate predictions using our scratch-built model coefficients
y_pred_scratch = X_bias @ theta 

# Calculate the Total Sum of Squares (TSS) - measures total variance in the actual target values
tss = np.sum((y - np.mean(y)) ** 2) 
# Calculate the Residual Sum of Squares (RSS) - measures variance left unexplained by our line
rss = np.sum((y - y_pred_scratch) ** 2) 
# Calculate the R² score (Coefficient of Determination) to evaluate the goodness of fit
r2_scratch = 1 - (rss / tss) 

# --- STEP 3: REPLICATE WITH SKLEARN ---
# Initialize the standard scikit-learn Linear Regression model instance
model = LinearRegression() 
# Train the model using the original X (sklearn automatically handles the bias/intercept column)
model.fit(X, y) 

# Extract the calculated slope (coefficient) from the trained sklearn model
slope_sklearn = model.coef_[0] 
# Extract the calculated intercept from the trained sklearn model
intercept_sklearn = model.intercept_ 
# Calculate the R² score using sklearn's built-in evaluation metric
r2_sklearn = model.score(X, y) 

# --- STEP 4: PRINT AND VERIFY RESULTS ---
print("--- FROM SCRATCH RESULTS ---")
print(f"Slope (Coefficient): {slope_scratch:.4f}")
print(f"Intercept:           {intercept_scratch:.4f}")
print(f"R² Score:            {r2_scratch:.4f}\n")

print("--- SKLEARN RESULTS ---")
print(f"Slope (Coefficient): {slope_sklearn:.4f}")
print(f"Intercept:           {intercept_sklearn:.4f}")
print(f"R² Score:            {r2_sklearn:.4f}\n")

# Check if both implementations yield identical results within a tiny decimal tolerance
if np.allclose([slope_scratch, intercept_scratch, r2_scratch], [slope_sklearn, intercept_sklearn, r2_sklearn]):
    print("SUCCESS: Your from-scratch math matches sklearn perfectly!")
else:
    print("ERROR: The results do not match. Check your matrix operations.")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
import joblib

# 1. Create a dummy dataset (e.g., predicting a basic binary outcome)
data = pd.DataFrame({
    'transaction_amount': [15.5, 25.0, None, 100.5, 5.0],
    'merchant_category': ['retail', 'food', 'retail', None, 'food'],
    'is_fraud': [0, 0, 1, 1, 0]
})

X = data[['transaction_amount', 'merchant_category']]
y = data['is_fraud']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Define preprocessing for numeric columns (impute missing -> scale)
numeric_features = ['transaction_amount']
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# 3. Define preprocessing for categorical columns (impute missing -> one-hot encode)
categorical_features = ['merchant_category']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# 4. Combine them into a single preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])
# 5. Create the final pipeline: Preprocessing + Model
production_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

# 6. Fit the pipeline on the training data
print("Training the pipeline...")
production_pipeline.fit(X_train, y_train)

# Evaluate on test data
accuracy = production_pipeline.score(X_test, y_test)
print(f"Initial Pipeline Accuracy: {accuracy * 100}%")
# 7. Save the pipeline using joblib
model_filename = 'fraud_pipeline_v1.pkl'
joblib.dump(production_pipeline, model_filename)
print(f"Pipeline serialized and saved to {model_filename}")

# 8. Load the pipeline to simulate a production serving environment
loaded_pipeline = joblib.load(model_filename)

# 9. Verify identical predictions
original_predictions = production_pipeline.predict(X_test)
loaded_predictions = loaded_pipeline.predict(X_test)

print("\n--- Production Verification ---")
print(f"Original predictions: {original_predictions}")
print(f"Loaded predictions:   {loaded_predictions}")
assert (original_predictions == loaded_predictions).all(), "Mismatch detected!"
print("Success: Loaded pipeline predictions are identical to the original.")
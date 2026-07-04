from sklearn.metrics import confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# 1. Generate Synthetic Fraud Data
X, y = make_classification(n_samples=1000, n_classes=2, weights=[0.95, 0.05], random_state=42)

# Include X in the split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Build and Train Classifier
clf = DecisionTreeClassifier().fit(X_train, y_train)
y_pred = clf.predict(X_test)

# 3. Manual Calculation (To see how numbers are computed)
tp = sum((y_test == 1) & (y_pred == 1))
fp = sum((y_test == 0) & (y_pred == 1))
tn = sum((y_test == 0) & (y_pred == 0))
fn = sum((y_test == 1) & (y_pred == 0))

print(f"Manual Calculation -> TP: {tp}, FP: {fp}, TN: {tn}, FN: {fn}")

# 4. Compare with sklearn
cm = confusion_matrix(y_test, y_pred)
print("Sklearn Confusion Matrix:\n", cm)
print("\nClassification Report:\n", classification_report(y_test, y_pred))
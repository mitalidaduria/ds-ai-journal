import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# 1. Generate Synthetic Fraud Data
X, y = make_classification(n_samples=1000, n_classes=2, weights=[0.95, 0.05], random_state=42)

# Include X in the split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 1. Train the model and get predictions FIRST
clf = RandomForestClassifier(n_estimators=100, random_state=42).fit(X_train, y_train)
y_pred = clf.predict(X_test) # <--- Now y_pred exists!
y_pred_new = (clf.predict_proba(X_test)[:, 1] > 0.2).astype(int)

# 2. NOW perform your manual calculations using y_pred
tp = sum((y_test == 1) & (y_pred == 1))
fp = sum((y_test == 0) & (y_pred == 1))
tn = sum((y_test == 0) & (y_pred == 0))
fn = sum((y_test == 1) & (y_pred == 0))

# 3. THEN print and plot
print(f"Manual Calculation -> TP: {tp}, FP: {fp}, TN: {tn}, FN: {fn}")
# ... rest of your code ...

# 4. Compare with sklearn
cm = confusion_matrix(y_test, y_pred)
print("Sklearn Confusion Matrix:\n", cm)
print("\nClassification Report (Threshold 0.2):\n", classification_report(y_test, y_pred_new))

# 5. The Heatmap
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Fraud Detection Confusion Matrix')
plt.savefig('confusion_matrix_heatmap.png')

# Use the new predictions from threshold-tuned Random Forest
cm = confusion_matrix(y_test, y_pred_new) 

# the heatmap will reflect new, more sensitive fraud detection
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
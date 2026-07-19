import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# Synthetic complaint texts for three categories
texts = [
    "I tried to pay for my order, but my debit card was declined even though I had enough money.",
    "The checkout page kept failing and I could not complete my payment.",
    "My card was charged twice for the same purchase and I need this fixed.",
    "The payment gateway kept showing an error during checkout.",
    "I received a payment failure message after submitting my card details.",
    "My order was not placed because the transaction was rejected.",
    "Please refund my order because the item arrived damaged.",
    "I want a refund for the product because it was not as described.",
    "The package arrived late and I would like a full refund.",
    "I canceled my subscription and still have not received my refund.",
    "The wrong item was delivered and I am requesting a refund.",
    "I need a refund because the service did not work as promised.",
    "I noticed a suspicious charge on my account that I did not authorize.",
    "Someone used my card details to make a fraudulent purchase.",
    "There is unauthorized activity on my account and I believe it is fraud.",
    "I saw a charge from your company that looks like identity theft.",
    "An unknown person opened an account using my personal information.",
    "I reported a scam transaction and want this investigated immediately.",
]

labels = [
    "payment_failure",
    "payment_failure",
    "payment_failure",
    "payment_failure",
    "payment_failure",
    "payment_failure",
    "refund_request",
    "refund_request",
    "refund_request",
    "refund_request",
    "refund_request",
    "refund_request",
    "fraud_report",
    "fraud_report",
    "fraud_report",
    "fraud_report",
    "fraud_report",
    "fraud_report",
]

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    texts,
    labels,
    test_size=0.25,
    random_state=42,
    stratify=labels,
)

# Convert text to TF-IDF features
vectorizer = TfidfVectorizer(stop_words="english")
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train logistic regression classifier
clf = LogisticRegression(max_iter=1000, random_state=42)
clf.fit(X_train_tfidf, y_train)

# Evaluate the model
predictions = clf.predict(X_test_tfidf)
print("Classification Report:\n")
print(classification_report(y_test, predictions))

# Print top 10 most important words for each category based on model coefficients
feature_names = vectorizer.get_feature_names_out()
print("\nTop 10 words for each category:\n")
for class_name, class_index in zip(clf.classes_, range(len(clf.classes_))):
    coef_scores = clf.coef_[class_index]
    top_words = sorted(
        zip(feature_names, coef_scores),
        key=lambda x: x[1],
        reverse=True,
    )[:10]
    print(f"{class_name}:")
    for word, score in top_words:
        print(f"  {word}: {score:.4f}")
    print()

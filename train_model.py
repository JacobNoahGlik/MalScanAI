from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import json

# Example format: [{"features": {"strcpy": 1, "open": 2}, "label": "ransomware"}, ...]
data = json.load(open("training_data.json"))
X = [list(d['features'].values()) for d in data]
y = [d['label'] for d in data]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
print(classification_report(y_test, clf.predict(X_test)))
joblib.dump(clf, "../model/classifier.pkl")

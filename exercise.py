import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib

X = pd.read_csv('./x',header=None)
y = pd.read_csv('./y',header=None)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

model = LogisticRegression()
model.fit(X_train, y_train)

joblib.dump(model, "model.m")

expected = y_test
predicted = model.predict(X_test)

print('MODEL')
print(model)
print('RESULT')
print(metrics.classification_report(expected, predicted))
print('CONFUSION MATRIX')
print(metrics.confusion_matrix(expected, predicted))

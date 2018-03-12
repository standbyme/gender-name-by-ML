import pandas as pd
import numpy
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

name = "奔驰"
last_four_words_in_name = name[-4:]
length_of_last_four_words_in_name = len(last_four_words_in_name)
name_vec = []
for i in range(0,4):
    if i<length_of_last_four_words_in_name:
        name_vec.append(name[i])
    else:
        name_vec.append(0)

print(name_vec)
data = numpy.array([name_vec])
# data = [[]]
X = numpy.array(data)
print(X.shape)

# model = joblib.load("model.m")

# predicted = model.predict(X)
# print(predicted[0])
# "官网上建议"[-4:]
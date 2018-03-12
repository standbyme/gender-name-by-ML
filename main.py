import pandas as pd
import numpy
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

name = "奔驰"
last_four_words_in_name = name[-4:]
length_of_last_four_words_in_name = len(last_four_words_in_name)

def word_to_vec(word):
    array = [0.12,0.56]
    return numpy.array(array)

pad = numpy.array([0,0])

def f(i):
    if i<length_of_last_four_words_in_name:
        single_word = last_four_words_in_name[i]
        word_vec = word_to_vec(single_word)
        print(word_vec)
        return word_vec
    else:
        return pad

name_vec = numpy.array(list(map(f,range(0,4)))).flatten()

data = numpy.array([name_vec])
print(data)
# data = [[]]
X = numpy.array(data)
print(X.shape)

# model = joblib.load("model.m")

# predicted = model.predict(X)
# print(predicted[0])
# "官网上建议"[-4:]
import pandas as pd
import numpy
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

pad = numpy.array([0,0])
def word_to_vec(word):
    array = [0.12,0.56]
    vec = numpy.array(array)
    return {'status':1,'vec':vec}

def main(name):
    last_four_words_in_name = name[-4:]
    length_of_last_four_words_in_name = len(last_four_words_in_name)

    def f(i):
        if i<length_of_last_four_words_in_name:
            single_word = last_four_words_in_name[i]
            word_vec = word_to_vec(single_word)
            return word_vec
        else:
            return pad

    name_vec_with_status = list(map(f,range(0,4)))
    is_successful = all(map(lambda x:x['status']==1,name_vec_with_status))
    print(is_successful)


main("奔驰dddd")
# name_vec = numpy.array().flatten()

# data = numpy.array([name_vec])
# print(data)
# data = [[]]
# X = numpy.array(data)
# print(X.shape)

# model = joblib.load("model.m")

# predicted = model.predict(X)
# print(predicted[0])
# "官网上建议"[-4:]
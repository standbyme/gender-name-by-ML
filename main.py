import pandas as pd
import numpy
import requests
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

model = joblib.load("model.m")
pad = numpy.zeros(1024)

def single_word_to_vec(single_word):
    word2vec_url = "http://127.0.0.1:1234"
    request = requests.post(word2vec_url, data = {'word':single_word})
    json_data = request.json()

    status = json_data['status']
    if status==1:
        vec_str = json_data['vec']
        vec= list(map(lambda x:float(x),vec_str.split(',')))
        return {'status':1,'vec':vec}
    else:
        return {'status':0}


def name_to_vec(name):
    last_four_words_in_name = name[-4:]
    length_of_last_four_words_in_name = len(last_four_words_in_name)
    name_vec_list = []

    for i in range(0,4):
        if i<length_of_last_four_words_in_name:
            single_word = last_four_words_in_name[i]
            single_word_vec = single_word_to_vec(single_word)
            status = single_word_vec['status']
            if status==1:
                vec= single_word_vec['vec']
                name_vec_list.append(vec)
            else:
                return {'status':0}
        else:
            name_vec_list.append(pad)
    
    name_vec = numpy.array(name_vec_list).flatten()
    return {'status':1,'vec':name_vec}

def main(name):
    name_vec_with_status = name_to_vec(name)
    status = name_vec_with_status['status']
    if status==0:
        return {'status':0}
    else:
        vec = name_vec_with_status['vec']
        data = numpy.array([vec])
        X = numpy.array(data)
        print(X.shape)


main('官网上建议')
# predicted = model.predict(X)
# print(predicted[0])
# "官网上建议"[-4:]
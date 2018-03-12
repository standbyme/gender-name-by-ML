import requests
import numpy

pad = numpy.zeros(1024)

def single_word_to_vec(single_word):
    # return  {'status':1,'vec': [0.1  0.5]}
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




# print(single_word_vec('王'))
print(name_to_vec('有用')['vec'].shape)
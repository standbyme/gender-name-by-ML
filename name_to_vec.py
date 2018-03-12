import requests

def single_word_vec(single_word):
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

print(single_word_vec('王'))
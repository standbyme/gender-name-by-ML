# 1
`docker login --username=thegatheringstorm registry.cn-beijing.aliyuncs.com`

password: 1234abcd
# 2
`docker run -d --name some-redis -p 6379:6379 registry.cn-beijing.aliyuncs.com/standbyme/wordvec`

`docker run -d --name some-redis-front -p 1234:1234 --link some-redis:redis registry.cn-beijing.aliyuncs.com/standbyme/wordvec_front`
# 3
`git clone https://github.com/standbyme/gender-name-by-ML.git`

`cd gender-name-by-ML`
# 4
`virtualenv --no-site-packages venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`python main.py`
# 5
`curl -l -H "Content-type: application/json" -X POST -d '{"name":"test"}' http://127.0.0.1:5000/name2gender`
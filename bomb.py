## -*- coding: utf-8 -*-
import requests, time

url = 'https://eda.yandex/api/v1/user/request_authentication_code'    
data_d = ({"phone_number": "77471395082"})
while True:
    res = requests.post(url, json=data_d)
    print(res.text)
    time.sleep(62)

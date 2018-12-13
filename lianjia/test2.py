# import hmac
# import hashlib
# import binascii
#
# def create_sha256_signature(key, message):
#     byte_key = binascii.unhexlify(key)
#     message = message.encode()
#     return hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()
#
# a = create_sha256_signature("/api/embedded_dashboard?data=%7B%22dashboard%22%3A7863%2C%22embed%22%3A%22v2%22%2C%22filters%22%3A%5B%7B%22name%22%3A%22Filter1%22%2C%22value%22%3A%22value1%22%7D%2C%7B%22name%22%3A%22Filter2%22%2C%22value%22%3A%221234%22%7D%5D%7D", "e179017a-62b0-4996-8a38-e91aa9f1")
# print(a)

import hashlib
import hmac
import base64
import random
import time


def c_signature():
    url = 'https://gateway.LianJia.com/wukong/ershoufang/search?city_id=350200&condition=&query=&order=&offset=0&limit=10'
    url_tmp1 = url.split("?")[0].split("://")[1]
    url_tmp2 = url_tmp1.split("/")[0]
    path = url_tmp1.split(url_tmp2)[1]
    host = url_tmp2.split(":")[0].upper()
    timestamp = str(int(time.time()))
    nonce = str(random.random())
    print(timestamp , nonce)
    method = 'GET'

    query_data = {
        'city_id': '350200',
        'condition': '',
        'query': '',
        'order': '',
        'offset': '0',
        'limit':  '10',
    }
    query = ''
    query_data_tmp = sorted(query_data.keys())
    for i in query_data_tmp:
        query += i + "=" + query_data[i] + "&"
    query = query.strip('&')

    c_message = ["accessKeyId=wukong", "nonce=" + nonce, "timestamp=" + timestamp,
                 "method=" + method, "path=" + path, "host=" + host]
    c_message.append("query=" + query)
    # print(c_message)

    key = 'lMl0XOUNSExcUYtw'
    message = bytes('&'.join(sorted(c_message)), 'utf-8')
    secret = bytes(key, 'utf-8')

    signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest()).decode()
    print(signature)
    return signature, timestamp, nonce


if __name__ == '__main__':
    t1 = c_signature()
    print(t1)


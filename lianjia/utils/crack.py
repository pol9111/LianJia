import hashlib, hmac, base64, random, time

def c_signature():
    """Crack the authorization of ershouf request headers"""
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
        'limit':  '50',
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

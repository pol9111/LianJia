# print(len('MjAxNzAzMjRfYW5kcm9pZD'))
# print(len('88e25777a517100db5a983ed7e3c2305e382a34c'))


import hashlib
import base64
from urllib.parse import urlparse, parse_qs

app_id = "ljwxapp:"
app_key = "6e8566e348447383e16fdd1b233dbb49"


def get_authorization(url):
    """
    根据url 动态获取authorization
    :param url:
    :return:
    """

    param = ""
    parse_param = parse_qs(urlparse(url).query, keep_blank_values=True)  # 解析url参数
    data = {key: value[-1] for key, value in parse_param.items()}  # 生成字典
    dict_keys = sorted(data.keys())  # 对key进行排序
    for key in dict_keys:  # 排序后拼接参数,key = value 模式
        param += str(key) + "=" + data[key]
    param = param + app_key  # 参数末尾添加app_key
    param_md5 = hashlib.md5(param.encode()).hexdigest()  # 对参数进行md5 加密
    authorization_source = app_id + param_md5  # 加密结果添加前缀app_id
    authorization = base64.b64encode(authorization_source.encode())  # 再次进行base64 编码
    return authorization.decode()


if __name__ in "__main__":
    url = "https://gateway.lianjia.com/wukong/ershoufang/search?city_id=350200&condition=&query=&order=&offset=0&limit=10"
    print(get_authorization(url))  # 生成加密串：bGp3eGFwcDoxYTNjMDA3MmQ0ZDA3NTM2ODVlOTJlMDQ0NmUwNDk5NQ==



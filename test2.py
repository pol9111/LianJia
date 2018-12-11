import hashlib


def GetMD5(string_):
    m = hashlib.md5()
    m.update(string_.encode('utf-8'))
    return m.hexdigest()


def GetAuthorization(dict_) -> str:
    datastr = "vfkpbin1ix2rb88gfjebs0f60cbvhedlcity_id={city_id}group_type={group_type}max_lat={max_lat}" \
              "max_lng={max_lng}min_lat={min_lat}min_lng={min_lng}request_ts={request_ts}".format(
        city_id=dict_["city_id"],
        group_type='0',
        max_lat='0',
        max_lng='0',
        min_lat='0',
        min_lng='0',
        request_ts='0')
    authorization = GetMD5(datastr)
    return authorization

d = {
    'city_id': '350200',

}
a = GetAuthorization(d)
print(a)




def generate_ershouf_url(city_id, total_page):
    """get ershouf result"""
    base_url = 'https://gateway.lianjia.com/wukong/ershoufang/search?city_id={}&con' \
          'dition=&query=&order=&offset={}&limit={}'
    url_list = []
    for offset in range(0, int(total_page)+1, 10):
        url = base_url.format(city_id, str(offset), '10')
        url_list.append(url)
    return url_list


if __name__ == '__main__':
    ershouf_urls = generate_ershouf_url('350200', 20)
    print(ershouf_urls)

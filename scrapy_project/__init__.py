import requests
from lxml.html import fromstring

if __name__ == '__main__':
    url = 'https://weixin.sogou.com/weixin'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.111 Safari/537.36 '
    }
    params = {
        "query": '林奇看盘',
        'type': '2'
    }
    response = requests.get(url=url, headers=headers, params=params)
    response.encoding = 'utf-8'
    text = response.text
    root_ = fromstring(text)
    path = root_.xpath("//div[@class='txt-box']//h3//a")

    for elements in path:
        value = elements.text_content()
        print('-------------------------')
        print(value)

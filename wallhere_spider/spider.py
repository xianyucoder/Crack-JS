import requests
from lxml import etree
import execjs


def get_jschl_answer():
    '''
    获取jschl-answer
    :return: jschl-answer
    '''
    with open('get_jschl_answer.js', 'r', encoding='utf-8') as fp:
        js = fp.read()
    jschl_answer_ctx = execjs.compile(js)
    jschl_answer = jschl_answer_ctx.call("get_jschl_answer")
    return jschl_answer


def get_param(jschl_answer):
    param_url = "https://wallhere.com/"
    data = {}
    response = requests.get(param_url).text
    content = etree.HTML(response)
    data['s'] = content.xpath('//input[@name="s"]/@value')[0]
    data['jschl_vc'] = content.xpath('//input[@name="jschl_vc"]/@value')[0]
    data['pass'] = content.xpath('//input[@name="pass"]/@value')[0]
    data['jschl_answer'] = jschl_answer
    print(data)
    return data


def get_index(data):
    headers = {
            'authority': "wallhere.com",
            'cache-control': "max-age=0,no-cache",
            'upgrade-insecure-requests': "1",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            'sec-fetch-mode': "navigate",
            'sec-fetch-user': "?1",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            'sec-fetch-site': "none",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "zh-CN,zh;q=0.9",
            # 'Postman-Token': "6fda3b1f-6640-42df-99e1-59ba38a86ed0,da4936af-6c93-4048-9f00-a30fd7d00598",
            'Host': "wallhere.com",
            'Connection': "keep-alive"
        }
    first_url = "https://wallhere.com/"
    session = requests.session()
    session.get(first_url, headers=headers)
    # cookies = requests.utils.dict_from_cookiejar(session.cookies)
    print('------------------第一次------------------', session.cookies)
    second_url = 'https://wallhere.com/cdn-cgi/l/chk_jschl'
    response = session.get(second_url, headers=headers, params=data)
    # print(response.request.url)
    print('------------------第二次------------------', session.cookies)


if __name__ == '__main__':
    jschl_answer = get_jschl_answer()
    # print(jschl_answer)
    data = get_param(jschl_answer)
    get_index(data)
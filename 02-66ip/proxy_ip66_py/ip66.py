import requests
import re
import execjs


def process_cookies():
    '''
    生成请求使用的cookie
    测试时间 : 2019-08-01
    :return:
    '''
    url_ = 'http://www.66ip.cn/areaindex_35/index.html'
    base_url = 'http://www.66ip.cn/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
    }
    res = requests.get(base_url, headers=headers)
    cookies = res.headers['Set-Cookie']
    print(res.text)
    res = re.findall('<script>(.*?)</script', res.text)[0]
    js = res.replace('{eval(', '{var params_1 = (')
    js_1 = js.replace(chr(0), chr(32))
    print(js_1)
    node = execjs.get()
    ctx = node.compile(js_1)
    bbb = ctx.eval('params_1')
    print('==================b', bbb)
    index1 = bbb.find("document.")
    index2 = bbb.find("};if((")
    js_temp_b = bbb[index1:index2].replace("document.cookie", "data2")
    other_param = 'window={};' + js_temp_b
    print(other_param)
    ctx = node.compile(other_param)
    ccc = ctx.eval('data2')
    print(ccc)
    cookies += ";" + ccc
    headers['Cookie'] = cookies
    res = requests.get(url_, headers=headers)
    if res.status_code == 200:
        res.encoding = res.apparent_encoding
        print(res.text)


if __name__ == '__main__':
    process_cookies()
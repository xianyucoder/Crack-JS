import requests
import execjs
import re
import json
import lzstring
from urllib.parse import urlencode


def get_index():
    index_url = 'https://tw.manhuagui.com/comic/2932/24867.html'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    resp = requests.get(index_url, headers=headers)
    # print(resp.text)
    return resp.text


def parse_js(html):
    text = html.replace('window["\\x65\\x76\\x61\\x6c"]', "eval")
    text = text.replace('\\x73\\x70\\x6c\\x69\\x63', "split")
    reg = re.compile(r'eval(.*?)</script>')
    code = reg.search(text).group(1)
    reg = re.compile("'(D.*?[\=]+)'")
    undecode = reg.search(code).group(1)
    x = lzstring.LZString()
    decode_str = x.decompressFromBase64(undecode)
    code = code.replace(undecode, decode_str)
    code = "function getinfo() { return " + code + "; }"
    ctx = execjs.compile(code)
    info = ctx.call("getinfo")
    reg = re.compile(r'\{.*\}')
    data = reg.search(info).group()
    json_data = json.loads(data)
    # print(json_data)
    return json_data

def get_content(comic):
    data = {
        'cid': comic['cid'],
        'md5': comic['sl']['md5']
    }
    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    # for filename in comic['files'][0]:
    #     url = 'https://i.hamreus.com' + comic['path'] + filename + '?'+urlencode(data)
    url = 'https://i.hamreus.com' + comic['path'] + comic['files'][0] + '?'+urlencode(data)
    resp = requests.get(url, headers=header)
    print(url)
    with open(comic['files'][0], 'wb') as f:
        f.write(resp.content)
        # f.close()

if __name__ == '__main__':
    html = get_index()
    comic = parse_js(html)
    get_content(comic)

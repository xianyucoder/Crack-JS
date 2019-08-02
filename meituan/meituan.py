import requests
from urllib.parse import urlencode
import execjs


def parse_token():
    originUrl = 'https://sz.meituan.com/meishi/'
    base_url = 'https://sz.meituan.com/meishi/api/poi/getPoiList?'

    params = {
        "areaId": "1056",
        "cateId": "0",
        "cityName": '深圳',
        "dinnerCountAttrId": '',
        "optimusCode": "1",
        "originUrl": originUrl,
        "page": 1,
        "partner": "126",
        "platform": "1",
        "riskLevel": "1",
        "sort": "",
        "userId": "",
        "uuid": "04dd5876-5ac5-4b29-8040-43191a5fbd14",
    }

    url = base_url + urlencode(params)
    with open('token_test.js', 'r', encoding='utf-8') as fp:
        js = fp.read()
    ctx = execjs.compile(js)
    token = ctx.call("get_token", url, originUrl)
    return token
    # print(token)


if __name__ == '__main__':
    payload = {
        "areaId": "1056",
        "cateId": "0",
        "cityName": '深圳',
        "dinnerCountAttrId": '',
        "optimusCode": "1",
        "originUrl": 'https://sz.meituan.com/meishi/',
        "page": 1,
        "partner": "126",
        "platform": "1",
        "riskLevel": "1",
        "sort": "",
        "userId": "",
        "uuid": "04dd5876-5ac5-4b29-8040-43191a5fbd14",
        "_token": parse_token()
    }
    headers = {
        "Host": "sz.meituan.com",
        "Connection": "keep-alive",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
        "Referer": "https://sz.meituan.com/meishi/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "_lxsdk_cuid=16a298e628ac8-0cdbfeff2fd6d-366f7e04-13c680-16a298e628ac8; _lxsdk=16a298e628ac8-0cdbfeff2fd6d-366f7e04-13c680-16a298e628ac8; mtcdn=K; __mta=218005161.1557886485522.1557886485522.1557887207743.2; _hc.v=506b711d-a17a-0b50-34ad-6a7d75117745.1557887238; client-id=f8e14d25-94cb-441f-9463-8ef01e5c7abe; uuid=04dd5876-5ac5-4b29-8040-43191a5fbd14; ci=59; rvct=59%2C1; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; _lxsdk_s=16aca5f317b-5ba-6ed-100%7C%7C7"
    }

    data_url = 'https://sz.meituan.com/meishi/api/poi/getPoiList?'
    resp = requests.get(url=data_url, params=payload, headers=headers)
    print(resp.text)
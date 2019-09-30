import time
from hashlib import md5
import requests


def get_sign(strTime):
    l = ["method", "orderTypeId", "orgcode", "pageNo", "pageSize", "plat", "platform", "shopId", "t", "v",
         "versionName"]
    t = {
        'method': 'ddsy.product.query.orgcode.product.list.b2c',
        'orderTypeId': '0',
        'orgcode': '010502,010503,010504,010505,010506,010507',
        'pageNo': '1',
        'pageSize': '100',
        'plat': 'H5',
        'platform': 'H5',
        'shopId': '-1',
        # 't': '2019-9-23 22:4:16',
        't': '{}'.format(strTime),
        'v': '1.0',
        'versionName': '3.2.0'
    }
    p = ''
    for i in range(0, 11):
        m = l[i]
        p += m + t.get(m)
    f = t['method'] + p + '6C57AB91A1308E26B797F4CD382AC79D'
    print(f)
    sign = md5value(f).upper()
    print(sign)
    return sign


def md5value(s):
    a = md5(s.encode()).hexdigest()
    return a

def get_product(sign,strTime):
    url = "http://product.ddky.com/product/queryOrgcodeProductListForB2C.htm"

    querystring = {"sign": sign, "method": "ddsy.product.query.orgcode.product.list.b2c",
                   "orderTypeId": "0", "orgcode": "010101,010104", "pageNo": "1", "pageSize": "100", "plat": "H5",
                   "platform": "H5", "shopId": "-1", "t": strTime, "v": "1.0", "versionName": "3.2.0",
                   "callback": "jQuery1111038253083703649504_1569245761443"}

    headers = {
        'Referer': "http://www.ddky.com/commodity.html?ddkycache=a7b19e879d2f2f279d356f5afa6d5cff",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "625b7600-902c-44df-9e8f-6c57e4d188b0,0ab39f76-32a6-412f-9b65-c6871f06269d",
        'Host': "product.ddky.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


if __name__ == '__main__':
    timeStamp = time.time()
    localTime = time.localtime(timeStamp)
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
    sign = get_sign(strTime)
    get_product(sign,strTime)




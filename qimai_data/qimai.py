import requests
import execjs
import json


with open('en.js', encoding='utf-8') as f:
    jsdata = f.read()
    jsdata = execjs.compile(jsdata)

# 只需要传入url(brand_id)和params(筛选条件)
url = 'https://api.qimai.cn/rank/indexPlus/brand_id/2'
params = {
    'brand': 'all',
    'genre': '6014',
    'device': 'iphone',
    'country': 'us',
    'date': '2018-10-02',
    'page': '1' # 1或'1'都行
}

js_params = json.dumps(params)
analysis = jsdata.call('get_analysis', url, js_params)
form = json.loads(analysis)
headers = {
    'Referer':'https://www.qimai.cn/rank',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}
html = requests.get(url, params=form, headers=headers)
print(html.json())

import requests
import re
import execjs


url = "http://www.gsxt.gov.cn/affiche-query-area-info-paperall.html"
headers = {
    # 'Cookie': "__jsluid=4f7efbfcbce6a01529ec0003981bb482; UM_distinctid=16972763956ccc-0e4c874106f6f7-36677905-13c680-16972763957a24; __jsluid_h=02dec99ec66ebb0d072094fbcc2096cd; SECTOKEN=6959647022540130109; gsxtBrowseHistory1=%0FS%04%06%1D%04%1D%10SNS%24%26%3B%22%3D%3A71%3A%3B01%3A%219%40%40DDDD5DGEALASXS%11%1A%00%1A%15%19%11SNS%E5%8C%BA%E4%B9%8E%E6%8B%B4%E6%9D%9B%E6%9D%BD%E9%98%A4%E5%84%98%E5%8E%8CSXS%11%1A%00%00%0D%04%11SNEEAFXS%02%1D%07%1D%00%00%1D%19%11SNEABFLMDFADFD%40%09; __jsl_clearance=1564905820.383|0|vzFdCeOoS3weRmIVyf2jGNOjMjI%3D; CNZZDATA1261033118=1413769021-1552399297-http%253A%252F%252Fwww.gsxt.gov.cn%252F%7C1564904187; JSESSIONID=5EE8F665B29D6AE241EC5E8677876E0D-n2:1; tlb_cookie=S172.16.12.131",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    }
session = requests.session()
response = session.get(url, headers=headers)
print(session.cookies)

# 生成cookie中的字段
res = re.findall('<script>(.*?)</script', response.text)[0]
# print(res)
js = res.replace('{eval(', '{var params_1 = (')
# print(js)
js_1 = js.replace(chr(0), chr(32))
# print(js_1)
node = execjs.get()
ctx = node.compile(js_1)
js2 = ctx.eval('params_1')
print(js2)
js3 = re.findall("document.(cookie=.+)\+';Expires", js2)[0]
other_param = 'window={};' + js3
ctx1 = node.compile(other_param)
jsl_params = ctx1.eval('cookie')
print(jsl_params)
cookies = jsl_params.split('=')
session.cookies.set(cookies[0], cookies[1])
session.get(url, headers=headers)
print(session.cookies)
cookies = requests.utils.dict_from_cookiejar(session.cookies)
querystring = {"noticeType": "21", "areaid": "100000", "noticeTitle": "", "regOrg": "110000"}
payload = "draw=1&start=0&length=10"
res = session.post(url, headers=headers,data=payload, params=querystring,cookies=cookies)
if res.status_code == 200:
    res.encoding = res.apparent_encoding
    print(res.text)
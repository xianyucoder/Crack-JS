import requests
import execjs
node = execjs.get()
file = 'baikewangjia.js'
ctx = node.compile(open(file).read())
data = ctx.eval("data")
verify_data = ctx.eval("verify")
print(data, verify_data)

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    }
url = "http://www.300600900.cn/"
session = requests.session()
session.get(url, headers=headers)
cookies = data.split('=')
session.cookies.set(cookies[0], cookies[1])
next_url = url + '?security_verify_data=' + verify_data
session.get(next_url, headers=headers)
print(session.cookies)
cookies = requests.utils.dict_from_cookiejar(session.cookies)
res = session.get(url, headers=headers, cookies=cookies)
res.encoding = res.apparent_encoding
print(res.text)

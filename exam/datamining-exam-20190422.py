import requests
import re


# 题目地址 -- http://datamining.comratings.com/exam

encoderchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
session = requests.session()
# 访问页面 获取参数和第一次访问的session
rep = session.get('http://datamining.comratings.com/exam')

session_id = rep.cookies.get_dict()['session']
# etag = rep.headers['Etag']

# 加密参数 session c1 c2
def f1(a):
    a_len = len(a)
    i, c, c2, c3 = 0, 0, 0, 0
    b = ""
    while i < a_len:
        c = ord(a[i]) & 0xff
        i += 1
        if i == a_len:

            b += encoderchars[c >> 2]
            b += encoderchars[(c & 0x3) << 4]
            b += "=="
            break

        c2 = ord(a[i])
        i += 1
        if i == a_len:

            b += encoderchars[c >> 2]
            b += encoderchars[((c & 0x3) << 4) | ((c2 & 0xf0) >> 4)]
            b += encoderchars[(c2 & 0xf) << 2]
            b += "="
            break

        c3 = ord(a[i])
        b += encoderchars[c >> 2]
        b += encoderchars[((c & 0x3) << 4) | ((c2 & 0xf0) >> 4)]
        b += encoderchars[((c2 & 0xf) << 2) | ((c3 & 0xc0) >> 6)]
        b += encoderchars[c3 & 0x3f]
        i += 1

    return b
cookie = 'session={}; c1={}; c2={};'.format(session_id,f1(session_id[1:4]),f1(session_id))
headers = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Connection': 'keep-alive',
    # 'Host': 'datamining.comratings.com',
    # 'If-None-Match':('{}'.format(etag)).encode(),
    'Cookie': cookie,
    # 'Referer': 'http://datamining.comratings.com/exam',
    # 'Upgrade-Insecure-Requests': '1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}
url = 'http://datamining.comratings.com/exam3'
rep1 = session.get(url=url,headers=headers).text
# print(rep1[0])

pattern = re.compile(r'<body>(.*?)<body>',re.DOTALL)
#用正则切出body内容
result = pattern.findall(rep1)
result1 = result[0].split('<br>')

# 用正则匹配开头的样式
pattern1 = re.compile(r'<style>(.*?)</style>',re.DOTALL)
sty1 = pattern1.findall(rep1)
pattern2 = re.compile(r'.(.*?){')
style = pattern2.findall(sty1[0])
# print(style)


data = []  #空数组，存放十个IP
for data_res in result1[1:]:
    line_array = data_res.split('\n')
    # print(line_array)
    ip_data = []  # 组成IP的四个数字存放的数组
    ip_str = ''
    for line_str in line_array:
        # print(line_str)
        pattern3 = re.compile(r'\d+')
        if style[0] not in line_str and style[1] not in line_str and 'none' not in line_str:
            ip_num = pattern3.findall(line_str)
            # print(ip_num)
            if ip_num != []:
                ip_data.append(ip_num[0])

    ip_str = '.'.join(ip_data)
    # print(ip_str)

    data.append(ip_str)
for i in data:
    print(i)
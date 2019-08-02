import requests
import execjs


if __name__ == '__main__':
    # Params
    # method = 'GETCITYWEATHER'
    method = 'GETDETAIL'

    city = '北京'
    type = 'HOUR'
    start_time = '2018-01-25 00:00:00'
    end_time = '2018-01-25 23:00:00'

    node = execjs.get()
    # Compile javascript
    file = 'aqi.js'
    ctx = node.compile(open(file).read())
    js = 'getServerData("{0}","{1}","{2}","{3}","{4}")'.format(method, city, type, start_time, end_time)
    params = ctx.eval(js)
    api = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
    response = requests.post(api, data={'d': params})
    decode_js = 'decodeData("{0}")'.format(response.text)
    decrypted_data = ctx.eval(decode_js)
    print(decrypted_data)
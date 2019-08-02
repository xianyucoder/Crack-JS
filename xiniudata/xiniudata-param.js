// 请求参数加密 请求的条件加密
var _keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    , _p = "W5D80NFZHAYB8EUI2T649RT2MNRMVE2O";
function _u_e(e) {
    if (null == e)
        return null;
    e = e.replace(/\r\n/g, "\n");
    for (var t = "", n = 0; n < e.length; n++) {
        var r = e.charCodeAt(n);
        r < 128 ? t += String.fromCharCode(r) : r > 127 && r < 2048 ? (t += String.fromCharCode(r >> 6 | 192),
            t += String.fromCharCode(63 & r | 128)) : (t += String.fromCharCode(r >> 12 | 224),
            t += String.fromCharCode(r >> 6 & 63 | 128),
            t += String.fromCharCode(63 & r | 128))
    }
    return t
}
function e2(e) {
    if (null == (e = _u_e(e)))
        return null;
    for (var t = "", n = 0; n < e.length; n++) {
        var r = _p.charCodeAt(n % _p.length);
        t += String.fromCharCode(e.charCodeAt(n) ^ r)
    }
    return t
}

function e1(e) {
    if (null == e)
        return null;
    for (var t, n, r, o, i, a, s, u = "", c = 0; c < e.length; )
        o = (t = e.charCodeAt(c++)) >> 2,
            i = (3 & t) << 4 | (n = e.charCodeAt(c++)) >> 4,
            a = (15 & n) << 2 | (r = e.charCodeAt(c++)) >> 6,
            s = 63 & r,
            isNaN(n) ? a = s = 64 : isNaN(r) && (s = 64),
            u = u + _keyStr.charAt(o) + _keyStr.charAt(i) + _keyStr.charAt(a) + _keyStr.charAt(s);
    return u
}
function sig(e) {
    return md5(e + _p).toUpperCase()
}
function test() {
    n = {"payload":{"date":[],"round":[],"location":[],"tag":[],"yellow":[],"yellow_tag":[],"domestic":"true","funding_date":[],"input":"","order":"desc","sort":76004,"page":0,"size":20}}
    var c = JSON.stringify(n),l = JSON.parse(c);
    var f = e1(e2(JSON.stringify(l.payload)))
    console.log(f)

}

test()

/*
*
from hashlib import md5
def md5value(s):
	a = md5(s.encode()).hexdigest()
	return a


hhh = 'LBcgWUQrZGATHHVgSiogJ1Z2DG9kfnZeIi0zOT8qXG1tbhkUEjonPWp7Ah8UZywsXjhZQxtoD29hbCsoOildOAhBJV8SdB0HZGM9LVUgJj1bNxQOGyYmRyhsfm8wMFwrPlsjZ1QvMj9qewIfFGc8J0IhQhYDcHYebyEgKTM3EHV1USFLU2xqeDsuKzYaf2J/AmQCGBsiNVUobGh9emdBJi1QZgICfjs='

p = 'W5D80NFZHAYB8EUI2T649RT2MNRMVE2O'

s = hhh + p
print(s)
*
*
* */

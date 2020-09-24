function strdecode(string) {
    string = base64decode(string);
    key = Gword+'ok ';
    len = key.length;
    code = '';
    for (i = 0; i < string.length; i++) {
        var k = i % len;
        code += String.fromCharCode(string.charCodeAt(i) ^ key.charCodeAt(k))
    }
    return base64decode(code)
}
var base64DecodeChars = new Array(-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1, -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1);

function base64decode(str) {
    var c1, c2, c3, c4;
    var i, len, out;
    len = str.length;
    i = 0;
    out = "";
    while (i < len) {
        do {
            c1 = base64DecodeChars[str.charCodeAt(i++) & 0xff]
        } while (i < len && c1 == -1);
        if (c1 == -1) break;
        do {
            c2 = base64DecodeChars[str.charCodeAt(i++) & 0xff]
        } while (i < len && c2 == -1);
        if (c2 == -1) break;
        out += String.fromCharCode((c1 << 2) | ((c2 & 0x30) >> 4));
        do {
            c3 = str.charCodeAt(i++) & 0xff;
            if (c3 == 61) return out;
            c3 = base64DecodeChars[c3]
        } while (i < len && c3 == -1);
        if (c3 == -1) break;
        out += String.fromCharCode(((c2 & 0XF) << 4) | ((c3 & 0x3C) >> 2));
        do {
            c4 = str.charCodeAt(i++) & 0xff;
            if (c4 == 61) return out;
            c4 = base64DecodeChars[c4]
        } while (i < len && c4 == -1);
        if (c4 == -1) break;
        out += String.fromCharCode(((c3 & 0x03) << 6) | c4)
    }
    return out
}

function run(autourl) {
    for (var i = 1; i < autourl.length; i++) {
        url = autourl[i];
        Gword = ' link@scmor.com'
        if(Gword!='') url = strdecode(url);
        var st = url.indexOf("//",1);
        var _domain = url.substring(st+1, url.length) ;
        var et = _domain.indexOf("/",1);
        surl = url.substring(0,et+st+2) ;
        console.log(surl)
    }
}

function geturl(){
    autourl = ["QSQ7XggEHBUhXDxYLwIFHwh4ZRkwXFI0Pw4jGj5ZXlI="
        , "QSQ7XggIPlUhFktUOl0GGwpodgUlA1I5KRpYBRBHW1I="
        , "QSQ7XggIPlUhFksaBzg7FQpodRkKXFI2KVEVAz5AMRkOLFMd"
        , "QSQ7XggIPlUhFktALhZYHA93bhwwNgQ1ETQ4GREcLQAPXRNIQwtUUw=="
        , "QSQ7XggIPlUhFktEOl0gGjESWAILXFM1FyRUGD4dLQUMKFJTeTQgUw=="
        , "QSQ7XggIPlUhFksdB1wOGg9nTAQLABsyPw5cAz4dLQUMKFJTeTQgUw=="
        , "QSQ7XggIPlUhFksdB1wOGiRkYlgNOT06Eis4GiscWhshXCVKQStQHTIYOl4="
        , "QSQ7XggIPlUhFktALwEdGwp4ahULXSErKTRcGT5DLRkPPFJaeV4BGAkHNRo="
        , "QSQ7XggEHBUhXUdGBwZYAAp4ZhQlAyU2ETBYBRBHWl8JXABW"
        , "QSQ7XggIPlUhFktALwE/XQlzFRYwXAcsEQ4jAz5ZXlI="
        , "QSQ7XggIPlUhFktALwEdGwp4ahULXSErKTRcGT5DLRkPPFMd"
        , "QSQ7XggIPlUhFktALwJcGTF4TF0IPV4qEQpVUg=="
        , "QSQ7XggIPlUhFktAAV1UAQlndVkmLV4oFg07Fih2BwM0ASVQRCs/FCctRg8JLEoT"
        , "QSQ7XggIPlUhFksdOTgkGg53ZhoKKQc1KRpYXBN5Vxk="
        , "QSQ7XggIPlUhFktEAigrFg9obgQKKQA1KVE/AShpWgUOFl5WQwEKGA=="
        , "QSQ7XggIPlUhFksdB1wOGjESRB0MJgQ1FyRUGD5ZXlI="];
    run(autourl)
}
geturl()


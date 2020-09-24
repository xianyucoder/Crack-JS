
function randomKey(t) {
    for (var e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=", r = 0, i = ""; r < t; ) {
        var n = Math.floor(Math.random() * e.length);
        i += e.charAt(n),
            r++
    }
    return i
}

function aesEncrypt(t, e) {
    var r = CryptoJS.enc.Utf8.parse(e)
        , n = CryptoJS.enc.Utf8.parse(t);
    return CryptoJS.AES.encrypt(n, r, {
        iv: CryptoJS.enc.Utf8.parse("0102030405060708"),
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    }).toString()
}


var CryptoJS = require("crypto-js");

function get_param() {
    var e = {
        mobile: "test",
        password: "adbc91a43e988a3b5b745b8529a90b61"
    }
    var r = randomKey(16), param = aesEncrypt(JSON.stringify(e), r);
    console.log(param)
}
get_param()
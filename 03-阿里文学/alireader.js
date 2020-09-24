decodeCont = function(t) {
    return t = function(t) {
        return t.split("").map(function(t) {
            var e, i;
            return t.match(/[A-Za-z]/) ? (e = Math.floor(t.charCodeAt(0) / 97),
                i = (t.toLowerCase().charCodeAt(0) - 83) % 26 || 26,
                String.fromCharCode(i + (0 == e ? 64 : 96))) : t
        }).join("")
    }(t),
        function(t) {
            var e, i, a, n, r, c, o, s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=", d = "", l = 0;
            for (t = t.replace(/[^A-Za-z0-9\+\/\=]/g, ""); l < t.length; )
                n = s.indexOf(t.charAt(l++)),
                    r = s.indexOf(t.charAt(l++)),
                    c = s.indexOf(t.charAt(l++)),
                    o = s.indexOf(t.charAt(l++)),
                    e = n << 2 | r >> 4,
                    i = (15 & r) << 4 | c >> 2,
                    a = (3 & c) << 6 | o,
                    d += String.fromCharCode(e),
                64 != c && (d += String.fromCharCode(i)),
                64 != o && (d += String.fromCharCode(a));
            return function(t) {
                for (var e, i = "", a = 0, n = 0, r = 0; a < t.length; )
                    n = t.charCodeAt(a),
                        n < 128 ? (i += String.fromCharCode(n),
                            a++) : n > 191 && n < 224 ? (r = t.charCodeAt(a + 1),
                            i += String.fromCharCode((31 & n) << 6 | 63 & r),
                            a += 2) : (r = t.charCodeAt(a + 1),
                            e = t.charCodeAt(a + 2),
                            i += String.fromCharCode((15 & n) << 12 | (63 & r) << 6 | 63 & e),
                            a += 3);

                return i
            }(d)
        }(t)
}

var data = decodeCont('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')
console.log(data)
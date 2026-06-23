const CryptoJS = require("crypto-js");
const { sha3_256 } = require("js-sha3")

function l(e) {
    var n = CryptoJS.enc.Utf8.parse("6f726c64")
        , t = CryptoJS.enc.Utf8.parse("01234567");
    return CryptoJS.DES.encrypt(e, n, {
        iv: t,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    }).toString()
}
// a页码
function get_data(n) {
var a = n
    , c = "symmetry_challenge"
    , s =Date.now()
    , i = "".concat(a, "_").concat(c, "_").concat(s);
XAESToken = (n = i,
    t = CryptoJS.enc.Utf8.parse("1234567890123456"),
    r = CryptoJS.enc.Utf8.parse('abcdefghijklmnop'),
    CryptoJS.AES.encrypt(n, t, {
        iv: r,
        mode: CryptoJS.mode.CTR,
        padding: CryptoJS.pad.NoPadding
    }).toString()),
  XDesToken = l(i);
var p = function (e) {
    var n = CryptoJS.enc.Utf8.parse("12345678901234567890123456789012")
        , t = CryptoJS.enc.Utf8.parse('abcdefghijklmnop');
    return CryptoJS.AES.encrypt(e, n, {
        iv: t,
        mode: CryptoJS.mode.OFB,
        padding: CryptoJS.pad.NoPadding
    }).toString()
}(i)
    , f = l(i + "_param"),
    d = '&'
    // url = "".concat(d, "aes_sign=").concat(encodeURIComponent(p), "&des_sign=").concat(encodeURIComponent(f), "&t=").concat(s)
    // console.log(`url: ${url}`   )
    return {
        aes_sign: encodeURIComponent(p),
        des_sign: encodeURIComponent(f),
        t: s,
        aestoken: XAESToken,
        destoken: XDesToken,
    }
}
// aes_sign = encodeURIComponent(p)
// des_sign = encodeURIComponent(f)
// t = s
// console.log(`aes_sign: ${p}, des_sign: ${f}, t: ${s}`)
console.log(get_data(5))
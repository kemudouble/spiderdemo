
const CryptoJS = require("crypto-js");
const { sha3_256 } = require("js-sha3")

let e = 1
    , t = 100
    , n = {}
    , s = new Set
    , a = "hash_challenge";
const o = "spiderdemo_sha_salt_2025";

function r(e, t, n) {
    const s = `${e}_${t}_${n}`
        , a = (r = s,
            c = "spiderdemo_hmac_secret_2025",
            CryptoJS.HmacSHA256(r, c).toString());
    var r, c;
    const i = function (e) {
        return CryptoJS.MD5(e).toString()
    }(s + "spiderdemo_md5_salt_2025")
        , l = function (e) {
            return CryptoJS.SHA256(e).toString()
        }(s + o)
        , u = function (e) {
            return sha3_256(e)
        }(s + o);
    return {
        hmac: a,
        md5: i,
        sha256: l,
        sha3_256: u
    }
}


function get_data(n) {
    s = "hash_challenge"
    a = Date.now()
    res=r(n, s, a)
    sign=res.sha256
    code=res.sha3_256
    t=a
    xToken=res.hmac
    xCode=res.md5
    console.log(`sign: ${sign}, code: ${code}, t: ${t}`)
    return {
        sign,
        code,
        t,
        xToken,
        xCode
    }
}
get_data(97)

// 在第一个promise中，生成签名并将其添加到URL参数中
// e.url += `${c}sign=${o.sha256}&code=${o.sha3_256}&t=${a}`
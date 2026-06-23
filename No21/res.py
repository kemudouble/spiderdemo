import requests
import execjs
with open(r"C:\Users\chujiaxiang\Desktop\ccc\spiderDemo\No21\ha.js", "r", encoding="utf-8") as f:
    js_code = f.read()
ctx = execjs.compile(js_code)

def get_data(i):
    result = ctx.call("get_data", i)
    headers = {
    "^accept": "application/json, text/plain, */*^",
    "^accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6^",
    "^cache-control": "no-cache^",
    "^pragma": "no-cache^",
    "^priority": "u=1, i^",
    "^referer": "https://www.spiderdemo.cn/authentication/hash_challenge/?challenge_type=hash_challenge^",
    "^sec-ch-ua": "^\\^Microsoft",
    "^sec-ch-ua-mobile": "?0^",
    "^sec-ch-ua-platform": "^\\^Windows^^^",
    "^sec-fetch-dest": "empty^",
    "^sec-fetch-mode": "cors^",
    "sec-fetch-site": "same-origin^",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0^",
    "x-request-token": result["xToken"] ,
    "x-verify-code": result["xCode"]
    }
    cookies = {
        "sessionid": "58wwb0b5e5079dpmlh3vuavfk4pz6794"
    }
    url = f"https://www.spiderdemo.cn/authentication/api/hash_challenge/page/{i}/"
    params = {
        "challenge_type": "hash_challenge",
        "sign": result["sign"],
        "code": result["code"],
        "t": result["t"]
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    data_li=response.json()
    data=data_li["page_data"]
    # print(f"第{i}页数据: {data}")
    return data


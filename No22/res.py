import httpx
import execjs
with open(r"C:\Users\chujiaxiang\Desktop\ccc\spiderDemo\No22\ha.js", "r", encoding="utf-8") as f:
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
    "^referer": "https://www.spiderdemo.cn/authentication/symmetry_challenge/?challenge_type=symmetry_challenge^",
    "^sec-ch-ua": "^\\^Microsoft",
    "^sec-ch-ua-mobile": "?0^",
    "^sec-ch-ua-platform": "^\\^Windows^^^",
    "^sec-fetch-dest": "empty^",
    "^sec-fetch-mode": "cors^",
    "^sec-fetch-site": "same-origin^",
    "^user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0^",
    "x-aes-token": result["aestoken"],
    "x-des-token": result["destoken"]
    }
    cookies = {
        "sessionid": "58wwb0b5e5079dpmlh3vuavfk4pz6794"
    }
    url = f"https://www.spiderdemo.cn/authentication/api/symmetry_challenge/page/{i}/"
    params = {
        "challenge_type": "symmetry_challenge",
        "aes_sign": result["aes_sign"],
        "des_sign": result["des_sign"],
        "t": result["t"]
    }
    response = httpx.get(url, headers=headers, cookies=cookies, params=params, verify=False)
    data_li=response.json()
    # print(response.text)
    data=data_li["page_data"]
    return data

if __name__ == "__main__":
    data = get_data(1)
    print(data)

import base64

import httpx


def getimg():
    headers = {
    "^accept": "*/*^",
    "^accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6^",
    "^cache-control": "no-cache^",
    "^pragma": "no-cache^",
    "^priority": "u=1, i^",
    "^referer": "https://www.spiderdemo.cn/captcha/cap5_challenge/?challenge_type=cap5_challenge^",
    "^sec-ch-ua": "^\\^Microsoft",
    "^sec-ch-ua-mobile": "?0^",
    "^sec-ch-ua-platform": "^\\^Windows^^^",
    "^sec-fetch-dest": "empty^",
    "^sec-fetch-mode": "cors^",
    "^sec-fetch-site": "same-origin^",
    "^user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0^"
    }
    cookies = {
        "sessionid": "wcdvmc0rp5jgspiqwoa8hkpocqb4wnbk^"
    }
    url = "https://www.spiderdemo.cn/captcha/api/cap5_challenge/captcha_image/"
    params = {
        "t": "1781277895765^"
    }
    response = httpx.get(url, headers=headers, cookies=cookies, params=params)
    with open("masked.jpg", "wb") as f:
        str=response.json()["masked"]
        image_data = base64.b64decode(str)
        f.write(image_data)
    with open("overlay.jpg", "wb") as f:
        str=response.json()["overlay"]
        image_data = base64.b64decode(str)
        f.write(image_data)
if __name__ == '__main__':
    getimg()
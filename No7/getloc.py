import httpx
import re

headers = {
    "^accept": "application/json, text/javascript, */*; q=0.01^",
    "^accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6^",
    "^cache-control": "no-cache^",
    "^pragma": "no-cache^",
    "^priority": "u=1, i^",
    "^referer": "https://www.spiderdemo.cn/css_anti/CSS1_challenge/?challenge_type=CSS1_challenge^",
    "^sec-ch-ua": "^\\^Microsoft",
    "^sec-ch-ua-mobile": "?0^",
    "^sec-ch-ua-platform": "^\\^Windows^^^",
    "^sec-fetch-dest": "empty^",
    "^sec-fetch-mode": "cors^",
    "^sec-fetch-site": "same-origin^",
    "^user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0^",
    "^x-requested-with": "XMLHttpRequest^"
}
cookies = {
    "sessionid": "58wwb0b5e5079dpmlh3vuavfk4pz6794"
}
url = "https://www.spiderdemo.cn/css_anti/api/CSS1_challenge/page/2/"
params = {
    "challenge_type": "CSS1_challenge"
}
response = httpx.get(url, headers=headers, cookies=cookies, params=params)

res=response.json()
data=res["page_data"]
pri

{
            "display_html": "<style>:root { --offset-0-8616: calc(((3 * 5px) * 2 / 2)); --offset-1-8039: calc(min((3 * 5px), (3 * 5px))); --neg-2-9129: calc(-1 * var(--offset-1-8039)); }</style><span data-index=\"4\">5</span><span data-type=\"char\" data-calc=\"0x3 * 0x5\" style=\"position:relative;left:var(--offset-0-8616)\">9</span><span title=\"position data\" data-calc=\"c * e\" style=\"position:relative;left:var(--neg-2-9129)\">5</span><span title=\"position data\">9</span>",
            "has_offset": true
        }

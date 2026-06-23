import base64
from fontTools.ttLib import TTFont
import httpx

def get_font(i):
    headers = {
        "^accept": "application/json, text/javascript, */*; q=0.01^",
        "^accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6^",
        "^cache-control": "no-cache^",
        "^pragma": "no-cache^",
        "^priority": "u=1, i^",
        "^referer": "https://www.spiderdemo.cn/font_anti/font_anti_challenge/?challenge_type=font_anti_challenge^",
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
        "sessionid": "kuitiaz64mby5c2c53as2dhfrf7jkfpx"
    }
    url = f"https://www.spiderdemo.cn/font_anti/api/font_anti_challenge/page/{i}/"
    params = {
        "challenge_type": "font_anti_challenge"
    }
    response = httpx.get(url, headers=headers, cookies=cookies, params=params)
    res=response.json()
    data=res["b64Font"]
    font_bytes = base64.b64decode(data)
    with open("font.ttf", "wb") as f:
        f.write(font_bytes)
    return res["page_data"]
def get_num(numstr,dic):
    num=""
    for i in numstr:
        num+=str(dic[int(i)] )
    return int(num)
def get_dic():
    font = TTFont("font.ttf")
    Zcmap={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0}
    glyph_order = font.getGlyphOrder()
    li=list(glyph_order)
    li.remove(".notdef")
    print(li)
    dic={}
    for i in range(0, len(li)):
        for i in range(0, len(li)):
            k=Zcmap[li[i]]
            dic[k]=i
    return dic

def compute(page_data,dic):
    sum=0
    for item in page_data:
        sum+=get_num(item,dic)
    return sum
def main(i):
    page_data=get_font(i)
    dic=get_dic()
    print(compute(page_data,dic))
if __name__ == "__main__":
    # page_data=get_font()
    # dic=get_dic()
    # print(compute(page_data,dic))
    he=0
    for i in range(1,101):
        page_data=get_font(i)
        dic=get_dic()
        he+=compute(page_data,dic)  
    print(he)
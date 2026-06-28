import httpx
import ddddocr
import io
import time
import cv2
def get_captcha(i):
    with httpx.Client(verify=False) as client:
        headers = {
        "accept": "application/json, text/javascript, */*; q=0.01^",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6^",
        "cache-control": "no-cache^",
        "content-type": "application/json^",
        "origin": "https://spiderdemo.cn^",
        "pragma": "no-cache^",
        "priority": "u=1, i^",
        "referer": "https://spiderdemo.cn/captcha/cap1_challenge/?challenge_type=cap1_challenge^",
        "sec-ch-ua": "^\\^Microsoft",
        "sec-ch-ua-mobile": "?0^",
        "sec-ch-ua-platform": "^\\^Windows^^^",
        "sec-fetch-dest": "empty^",
        "sec-fetch-mode": "cors^",
        "sec-fetch-site": "same-origin^",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0^",
        "x-requested-with": "XMLHttpRequest^"
    }
        cookies = {
            "cs_canvas_gate": "cc22e16a81f68a3da728b6ee3706b18668246432^%^7Cedca7b67-fe16-4590-9fc8-6108df47f993^%^7Cf9c1326f45b0465cc4d94687a14a163d36fdbedea3b692cb443fb679025ed5aa^%^7Cclient-signals-v2^%^7Ccc22e16a81f68a3da728b6ee3706b18668246432^%^7CMicrosoft^%^20Edge^%^7C149.0.4022.80^%^7CMicrosoft^%^20Edge^%^7C149.0.4022.80",
            "sessionid": "65d25gwzvv9wghngz6ksm7bv0vrtt5g0",
            "cs_stable_gate": "cc22e16a81f68a3da728b6ee3706b18668246432^%^7Ccee13414-1743-4f18-8583-72218148f2b1^%^7C7a4291b037ba1326878565296fa2c6695a450a1772fb9435c5b48536e62ad164^%^7Cclient-signals-v2^%^7Cstable-v2^%^3AeyJ2IjoyLCJjYW52YXNGaW5hbEhhc2giOiJjYzIyZTE2YTgxZjY4YTNkYTcyOGI2ZWUzNzA2YjE4NjY4MjQ2NDMyIiwid2ViZ2xJbWFnZUhhc2giOiIxQzA5MzAwMSIsIndlYmdsUmVwb3J0SGFzaCI6IkVGODE4OEI4Iiwid2ViZ2xVbm1hc2tlZFZlbmRvciI6Ikdvb2dsZSBJbmMuIChJbnRlbCkiLCJ3ZWJnbFVubWFza2VkUmVuZGVyZXIiOiJBTkdMRSAoSW50ZWwsIEludGVsKFIpIFVIRCBHcmFwaGljcyAoMHgwMDAwOUJDNCkgRGlyZWN0M0QxMSB2c181XzAgcHNfNV8wLCBEM0QxMSkiLCJ3ZWJncHVGdWxsSGFzaCI6IiIsImF1ZGlvRmluYWxIYXNoIjoiNjAzNzc1YWQ1MGQwNGIzMyIsImF1ZGlvQ3JlZXBIYXNoIjoiMzdkNDQzMTQiLCJjbGllbnRyZWN0RnVsbFNoYTEiOiJkNzI0NzYwNDlmOTE1ZGQwZDI4YmVlNzdiNDZiNTc3YTY3ZThmMTJiIiwiZm9udHNGb250SGFzaCI6ImFhNDVmNzQiLCJuYXZpZ2F0b3JQbGF0Zm9ybSI6IldpbjMyIiwiaGFyZHdhcmVDb25jdXJyZW5jeSI6IjEyIiwiZGV2aWNlTWVtb3J5IjoiOCIsImJyb3dzZXJOYW1lIjoiTWljcm9zb2Z0IEVkZ2UifQ^%^3D^%^3D^%^7CMicrosoft^%^20Edge^%^7C149.0.4022.80^"
        }
        url = "https://www.spiderdemo.cn/captcha/api/cap1_challenge/captcha_image/"
        t=int(time.time()*1000)
        params = {
            "t":t
        }
        resp = client.get(url, headers=headers, cookies=cookies, params=params)
        with open("captcha.png", "wb") as f:
                f.write(resp.content)
        img= cv2.imread("captcha.png")
        new_img=img[20:35,55:95]
        cv2.imwrite("new_captcha.png", new_img)

        ocr = ddddocr.DdddOcr(show_ad=False)
        result = ocr.classification(new_img, png_fix=True)
        url = "https://spiderdemo.cn/captcha/api/cap1_challenge/page/"
        client.headers.update({"Content-Type": "application/json"})
        data = {"captcha_input": result, "page_num":i, "challenge_type": "cap1_challenge"}
        response = client.post(url, headers=headers, cookies=cookies, json=data)
        ha=response.json()
        data=ha["page_data"]
        return data
if __name__ == "__main__":
    sum=0
    corr_li=[]
    for i in range(2, 101):
        try:
            data=get_captcha(i)
            he=0
            for item in data:
                    he+=item
            print("page", i, "sum", he)
            sum+=he
        except Exception as e:
            corr_li.append(i)
        
    print("sum", sum)
    print("corr_li", corr_li)
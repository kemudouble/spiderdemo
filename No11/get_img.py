import httpx
import ddddocr
from PIL import Image, ImageFilter, ImageOps
import io
import time
headers = {
    "^accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8^",
    "^accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6^",
    "^cache-control": "no-cache^",
    "^pragma": "no-cache^",
    "^priority": "u=1, i^",
    "^referer": "https://www.spiderdemo.cn/captcha/cap1_challenge/?challenge_type=cap1_challenge^",
    "^sec-ch-ua": "^\\^Microsoft",
    "^sec-ch-ua-mobile": "?0^",
    "^sec-ch-ua-platform": "^\\^Windows^^^",
    "^sec-fetch-dest": "image^",
    "^sec-fetch-mode": "no-cors^",
    "^sec-fetch-site": "same-origin^",
    "^user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0^"
}
cookies = {
    "sessionid": "wcdvmc0rp5jgspiqwoa8hkpocqb4wnbk"
}
url = "https://www.spiderdemo.cn/captcha/api/cap1_challenge/captcha_image/"
t=int(time.time()*1000)
params = {
    "t":t
}
resp = httpx.get(url, headers=headers, cookies=cookies, params=params)
with open("captcha.png", "wb") as f:
        f.write(resp.content)

ocr = ddddocr.DdddOcr(show_ad=False)
ocr.set_ranges(6)
# img = Image.open(io.BytesIO(resp.content)).convert("RGB")

# # ✅ 放大（ddddocr 对小人脸极度敏感）
# img = img.resize((img.width * 2, img.height * 2), Image.LANCZOS)

result = ocr.classification(resp.content, png_fix=True)
print("w", result)
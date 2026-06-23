import httpx
import base64
import time
import cv2
import numpy as np
from PIL import Image, ImageSequence
import ddddocr

def getgif():
    headers = {
        "^accept": "*/*^",
        "^accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6^",
        "^cache-control": "no-cache^",
        "^pragma": "no-cache^",
        "^priority": "u=1, i^",
        "^referer": "https://www.spiderdemo.cn/captcha/cap2_challenge/?challenge_type=cap2_challenge^",
        "^sec-ch-ua": "^\\^Microsoft",
        "^sec-ch-ua-mobile": "?0^",
        "^sec-ch-ua-platform": "^\\^Windows^^^",
        "^sec-fetch-dest": "empty^",
        "^sec-fetch-mode": "cors^",
        "^sec-fetch-site": "same-origin^",
        "^user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0^"
    }
    cookies = {
        "sessionid": "wcdvmc0rp5jgspiqwoa8hkpocqb4wnbk"
    }
    url = "https://www.spiderdemo.cn/captcha/api/cap2_challenge/captcha_image/"
    t=int(time.time()*1000)
    params = {
        "t": t
    }
    response = httpx.get(url, headers=headers, cookies=cookies, params=params)

    res=response.json()
    # print(res["T"])

    im=base64.b64decode(res["T"])
    with open("T.gif", "wb") as f:
        f.write(im)

def get_image_laplacian_var(img):
    """计算拉普拉斯方差，值越大图像越清晰"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    lap_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return lap_var

def extract_best_gif_frame(gif_path, save_path="best_frame.png"):
    # 1. 读取GIF所有帧
    gif = Image.open(gif_path)
    frames = []
    cv_frames = []

    for frame in ImageSequence.Iterator(gif):
        # 转RGB（去除GIF透明/索引色干扰）
        frame_rgb = frame.convert("RGB")
        # PIL 转 OpenCV 格式
        cv_img = cv2.cvtColor(np.array(frame_rgb), cv2.COLOR_RGB2BGR)
        frames.append(frame_rgb)
        cv_frames.append(cv_img)

    if not frames:
        print("未读取到GIF帧")
        return

    # 2. 给每一帧打分（清晰度）
    score_list = [get_image_laplacian_var(f) for f in cv_frames]
    # 找到分数最高的帧索引（最清晰）
    best_idx = np.argmax(score_list)
    best_frame = frames[best_idx]

    # 3. 保存最优帧
    best_frame.save(save_path)
    # print(f"已提取最优帧，帧序号：{best_idx}，清晰度分数：{score_list[best_idx]:.2f}")
    return best_frame


def getText(image):
    # ocr.set_ranges(8)
    result=ocr.classification(image,png_fix=True)
    print(result)
    return result

def getText2():
    
    getgif()
    img=extract_best_gif_frame("T.gif")
    result=getText(img)
    return result
def getdata(i,result):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0^",
    }
    cookies = {
        "sessionid": "wcdvmc0rp5jgspiqwoa8hkpocqb4wnbk"
    }
    url = "https://www.spiderdemo.cn/captcha/api/cap2_challenge/page/"
    data = {"captcha_input": result, "page_num": i, "challenge_type": "cap2_challenge"}
    response = httpx.post(url, headers=headers, cookies=cookies, json=data)

    res=response.json()
    data=res["page_data"]
    # print(response.text)
    return data
if __name__ == '__main__':
    ocr = ddddocr.DdddOcr(show_ad=False)
    # sum=5403307
    # list1=[]
    # for i in [1]:
    #     try:
    #         result = getText2()
    #         data=getdata(i, result)
    #         print("第",i,"页数据：",data)
    #         for item in data:
    #             sum+=item
    #     except Exception as e:
    #         list1.append(i)

    # print("sum",sum)
    # print("fail list",list1)
    result = getText2()
    data=getdata(1, result)
    print("第",1,"页数据：",data)
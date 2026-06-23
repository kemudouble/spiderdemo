import httpx
import base64
import re
from PIL import Image
import os
import ddddocr
def get_img(i):
    headers = {
        "^accept": "application/json, text/javascript, */*; q=0.01^",
        "^accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6^",
        "^cache-control": "no-cache^",
        "^pragma": "no-cache^",
        "^priority": "u=1, i^",
        "^referer": "https://www.spiderdemo.cn/font_anti/font_sprites_challenge/?challenge_type=font_sprites_challenge^",
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
    url = f"https://www.spiderdemo.cn/font_anti/api/font_sprites_challenge/page/{i}/"
    params = {
        "challenge_type": "font_sprites_challenge"
    }
    response = httpx.get(url, headers=headers, cookies=cookies, params=params)
    # print(response.status_code)
    # print(response.text)
    # print(response)
    imgbase64=response.json()["sprite"]
    css_code=response.json()["css_code"]
    page_data=response.json()["page_data"]
    return imgbase64, css_code, page_data

def base64_to_image(b64_str, save_path="sprite.png"):
    """Base64 转图片并保存"""
    img_data = base64.b64decode(b64_str)
    with open(save_path, "wb") as f:
        f.write(img_data)
    return Image.open(save_path)
def parse_css_positions(css_text):

    """解析CSS，得到 {class名: x偏移量}"""
    pat = re.compile(r"class(\d+)\{background-position:\s*(-?\d+)px\s+0;")
    res = pat.findall(css_text)
    class_pos = {}
    for cls_name, x_str in res:
        cls_full = f"class{cls_name}"
        offset_x = int(x_str)
        class_pos[cls_full] = abs(offset_x)  # 转为正数：裁剪起始x坐标
    # 去重
    return dict(set(class_pos.items()))
def extract_class_from_html(html_str):
    """从单条html里提取所有class列表"""
    pat = re.compile(r"class='sprite\s+([\w\d]+)'")
    return pat.findall(html_str)
def getClassDict(page_data):
    """构建 {class名: 字符} 的字典"""
    class_dict = {}
    i=1
    for item in page_data:
        v=extract_class_from_html(item)
        class_dict[i]=v
        i+=1
    return class_dict
def cut_sprite(img, start_x, char_w=50, char_h=None,name="q",cla={}):
    """
    裁剪单个字符
    :param img: 原图对象
    :param start_x: 起始X坐标
    :param char_w: 单字符宽度（根据前面规律：50px）
    :param char_h: 高度，默认整张图高度
    :param save_name: 保存文件名
    :return: 裁剪后的图
    """
    w, h = img.size
    if char_h is None:
        char_h = h
    # 裁剪区域：(left, upper, right, lower)
    box = (start_x, 0, start_x + char_w, char_h)
    ocr=ddddocr.DdddOcr(show_ad=False)
    crop_img = img.crop(box)
    ocr_result = ocr.classification(crop_img,png_fix=True)
    # print(f" {ocr_result} for {name}")
    if ocr_result=='o':
        cla[name] = '0'
    else:   
        cla[name] = ocr_result
    # return crop_img
def get_pageSum(i):
    sum=0
    imgb64, css_code, page_data = get_img(i)
    class_dict = getClassDict(page_data)
    ha=parse_css_positions(css_code)
    try:
        cla={}
        for k in ha:
            cut_sprite(base64_to_image(imgb64), ha[k],name=k,cla=cla)
        for k in class_dict:
            str=""
            for v in class_dict[k]:
                str+=cla[v]
            sum+=int(str)
        print(f"{i}_success,value={sum}")
        return sum,0
    except Exception as e:
        # print(f"Error occurred: {e}")
        return 0,i
if __name__ == "__main__":
    # sum=0
    # list=[]
    # for i in range(1,101):
    #     s,f = get_pageSum(i)
    #     sum += s
    #     if f != 0:
    #         list.append(f)
    # print(f"总和：{sum}")
    # print(f"失败的页码：{list}")
    sum=4990381
    list=[]
    for i in [13, 30, 37, 38, 39, 42, 65, 93]:
        s,f = get_pageSum(i)
        sum += s
        if f != 0:
            list.append(f)
    print(f"总和：{sum}")
    print(f"失败的页码：{list}")
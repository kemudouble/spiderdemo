import httpx
import execjs
with open(r"C:\Users\chujiaxiang\Desktop\ccc\spiderDemo\No23\ah.js", "r", encoding="utf-8") as f:
    js_code = f.read()
ctx = execjs.compile(js_code)

def get_data(i):
    result = ctx.call("cumpt", i)
    headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0^",
    "x-auth-key": result["XAuthKey"],
    "x-signature": result["XSignature"]
}
    cookies = {
    "sessionid": "oxgjah5t9jtpwn8zro4n4463wpbmq62p",
    "cs_canvas_gate": "cc22e16a81f68a3da728b6ee3706b18668246432^%^7Cedca7b67-fe16-4590-9fc8-6108df47f993^%^7Cf9c1326f45b0465cc4d94687a14a163d36fdbedea3b692cb443fb679025ed5aa^%^7Cclient-signals-v2^%^7Ccc22e16a81f68a3da728b6ee3706b18668246432^%^7CMicrosoft^%^20Edge^%^7C149.0.4022.80^%^7CMicrosoft^%^20Edge^%^7C149.0.4022.80^"
}
    url = f"https://spiderdemo.cn/authentication/api/fsymmetry_challenge/page/{i}/"
    params = {
    "challenge_type": "fsymmetry_challenge",
    "data": result["data"],
    "verify": result["verify"],
    "t": result["t"]}
    response = httpx.get(url, headers=headers, cookies=cookies, params=params)
    data_li=response.json()
    # print(response.text)
    data=data_li["page_data"]
    print(f"第{i}页数据：{data}")
    return data
def cumpt(li):
    he=0
    for i in li:
        he+=int(i)
    return he
if __name__ == "__main__":
    # data = get_data(1)
    # print(data)
    # print(cumpt(data))
    corr_li=[]
    sum=0
    for i in range(1, 101):
        try:    
            data = get_data(i)
            sum+=cumpt(data)
        except Exception as e:
           corr_li.append(i)

    print(sum)
    print(corr_li)

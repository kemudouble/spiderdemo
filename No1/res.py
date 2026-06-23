import httpx


he=0
with httpx.Client(
    base_url="https://www.spiderdemo.cn/sec1/api/challenge/init/",
    cookies={"sessionid": "58wwb0b5e5079dpmlh3vuavfk4pz6794"},
    # headers={"User-Agent": "MyApp/1.0"},
    params = {"challenge_type": "header_check" },
    follow_redirects=True , # httpx 默认不自动重定向
    verify=False  # 禁用 SSL 验证
) as client:
     for i in range(1, 101):
        r = client.get(f"https://www.spiderdemo.cn/sec1/api/challenge/page/{i}/?challenge_type=header_check")
        data_li=r.json()
        data=data_li["page_data"]
        print(f"第{i}页数据: {data}")
        for item in data:
            he+=item

print(he)
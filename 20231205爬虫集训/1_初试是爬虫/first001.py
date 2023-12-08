# BS架构
# 浏览器/服务器架构
# 爬虫  实际上就是为了替代浏览器，去请求服务器，获取数据


# XMLRequestHttp
import requests
# pycharm 2023如何修改镜像源

# 先按照相应组件 pip install urllib requests beautifulsoup4

# Request URL
# url = "https://www.baidu.com/"

# Request Headers   字典,键值通常为字符串类型
# header = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "zh-CN,zh;q=0.9",
#         "Cache-Control": "no-cache",
#         "Connection": "keep-alive",
#         "Cookie": "BIDUPSID=16C6F107236FD5E9D1A8F0A9B0EADC97; PSTM=1701406097; BAIDUID=16C6F107236FD5E9D1A8F0A9B0EADC97:FG=1; BD_UPN=123253; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=802k8gah8h000h858la0ah2k1imrmqk1r; BAIDUID_BFESS=16C6F107236FD5E9D1A8F0A9B0EADC97:FG=1; ZFY=HLhMoz1155:B4B:B:AOXMiYvpAmmF3XJgf:AM:AEVCklItjo:C; COOKIE_SESSION=6837_0_3_3_4_5_0_0_3_2_0_0_6840_0_4_0_1701767547_0_1701767543%7C5%230_0_1701767543%7C1",
#         "Host": "www.baidu.com",
#         "Pragma": "no-cache",
#         "Sec-Fetch-Dest": "document",
#         "Sec-Fetch-Mode": "navigate",
#         "Sec-Fetch-Site": "none",
#         "Sec-Fetch-User": "?1",
#         "Upgrade-Insecure-Requests": "1",
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
#         "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
#         "sec-ch-ua-mobile": "?0",
#         "sec-ch-ua-platform": "macOS"
# }
# 查找Request Method    除了url 其他都是kw = val 这种类型进行传参
# response = requests.get(url,headers=header)
# print(response)  # <Response [200]>  响应对象
# if response.status_code == 200:
#     print(response.text)   # 以文本/字符串数据形式拿到响应的值
#     print("请求成功")
# print(response.status_code)  # 响应状态码
# response.content   # 以字节数据形式拿到响应的值
# response.json()    # 将json格式的响应数据转换为字典/列表类型
# demo = '{"name":"yzz","age":18}'  # json就是长得像Python中字典/列表的字符串
# print(type(demo))
# print([demo])
# print(repr(demo))
import json
# demo1 = json.loads(demo)
# print(type(demo1))
# print([demo1])
# A.dict  B.str
# \n\r\t

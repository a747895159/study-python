# 模拟登录....


# cookie   <---  携带用户身份信息,大部分情况下是服务器给我们的



import requests

loginUrl = "https://passport.17k.com/ck/user/login"
loginHeaders ={
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "passport.17k.com",
    "Origin": "https://passport.17k.com",
    "Pragma": "no-cache",
    "Referer": "https://passport.17k.com/login/",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
data = {
'loginName': '13636001441',
'password': 'yzz19940831'
}
response = requests.post(url=loginUrl,headers=loginHeaders,data=data)
print(response.text)
# print(response.cookies.get_dict()) # 查看响应中的cookie,以字典形式返回...

# haeders中的cookie 通常是 "key=value; key=value; key=value"
cookies = '; '.join([key+'='+value for key,value in response.cookies.get_dict().items()])
print(cookies)
mainpageUrl = "https://user.17k.com/www/"
headers ={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "user.17k.com",
    "Pragma": "no-cache",
    "Referer": "https://passport.17k.com/",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
headers['Cookie'] = cookies
mainpageResponse = requests.get(url=mainpageUrl,headers=headers)
mainpageResponse.encoding = mainpageResponse.apparent_encoding
print(mainpageResponse.text)

cookies = '; '.join([key+'='+value for key,value in mainpageResponse.cookies.get_dict()])
headers['Cookie'] = cookies
# 填cookie
# 发请求
# 拿cookie
# 填cookie
# 发请求
# 拿cookie

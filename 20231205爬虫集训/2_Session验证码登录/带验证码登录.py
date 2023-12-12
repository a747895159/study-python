import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 不提示 HTTPS的证书警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from chaojiying import Chaojiying_Client

sess = requests.Session()

# 获取验证码
imgurl = "https://www.xqb5200.com/checkcode.php"
imgheaders = {
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Referer": "https://www.xqb5200.com/login.php",
    "Sec-Ch-Ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "image",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}
imgresponse = sess.get(imgurl, headers=imgheaders, verify=False)
with open('code.png', 'wb') as f:
    f.write(imgresponse.content)
chaojiying = Chaojiying_Client('MiddleYang', 'RFYang_31', '950691')  # 用户中心>>软件ID 生成一个替换 96001
with open('code.png', 'rb') as f:
    im = f.read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
checkcode = chaojiying.PostPic(im, 1004)['pic_str']
print(checkcode)
# 账号 密码  软件ID(用户中心里设置)      codetype

loginurl = "https://www.xqb5200.com/login.php?do=submit"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "no-cache",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://www.xqb5200.com",
    "Pragma": "no-cache",
    "Referer": "https://www.xqb5200.com/login.php",
    "Sec-Ch-Ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}
data = {
    "username": "18772517221",
    "password": "yzz123456",
    "checkcode": checkcode,
    "usecookie": "0",
    "action": "login",
    "submit": "%26%23160%3B%B5%C7%26%23160%3B%26%23160%3B%C2%BC%26%23160%3B"
}
response = sess.post(loginurl, headers=headers, data=data, verify=False)
print(response.text)

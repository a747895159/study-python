import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# 准备url
url = "https://www.shicimingju.com/shicimark"
# 准备请求头   尽量带全 是好习惯  只带UA 是陋习
headers ={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Cookie": "Hm_lvt_649f268280b553df1f778477ee743752=1701761335,1701780556; Hm_lpvt_649f268280b553df1f778477ee743752=1701780556",
    "Pragma": "no-cache",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "macOS",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
# 发送请求  检查请求方法
response = requests.get(url,headers=headers)
# 打印响应数据
# 1.显式指定编码
response.encoding = "utf-8"
# 2.显式指定
# print(response.content.decode('utf-8'))
# 3.隐式指定
response.encoding = response.apparent_encoding

# print(response.text)
# 文字描述解析过程
# 我们要找到class属性为card hc_other_zuozhe的div(一个)
# 通过这个div找到下面所有的a标签
# 提取a标签里所有的href和文本
soup = BeautifulSoup(response.text,"html.parser")
div = soup.find('div',class_='card hc_other_zuozhe')
alist = div.find_all('a')  # .find 约等于 .find_all()[0]
# find_all返回来的是一个列表
print(len(alist))
for a in alist:
    text = a.text  # 提取标签中的文本
    # href = a['href']  # 提取标签中的href属性
    # href = a.get('href', "没有href属性的时候返回这个字符串,默认是None")
    href = urljoin(url,a.get('href'))
    print(text,href)

import requests
from bs4 import BeautifulSoup
import os
# 所有的静态资源  word csv xlsx/xls pdf md txt zip/rar  mp3/mp4  png/jpg/gif  exe/msi  apk/ipa  js/css/html
# 都是一套下载逻辑
# content = b"这个是二进制数据"
# with open('file','wb') as f:  # w 覆写 a 追加
#     f.write(content)
# 经常有同学问  老师 为什么我下载数据文件数目少了

if not os.path.exists('D:/data/img'):
    os.mkdir('D:/data/img')  # 如果文件夹已存在 还去创建 就会报错


# 1.查看响应找到我们需要的数据在哪里
url = 'https://sc.chinaz.com/tupian/chouxiangtupian.html'
headers ={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "cz_statistics_visitor=3055b24d-d2ed-de80-1e42-36e631484a6e; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1701776125,1701782324; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1701782328",
    "Host": "sc.chinaz.com",
    "Pragma": "no-cache",
    "Referer": "https://sc.chinaz.com/tupian/renwutupian.html",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
response = requests.get(url=url,headers=headers)
response.encoding =  response.apparent_encoding
soup = BeautifulSoup(response.text,'html.parser')
divs = soup.find_all('div',class_='item')
for div in divs:
    img = div.find('img')
    href = "https:"+img.get('data-original')
    # title = img.get('alt')
    # print(title,href)
    filename = href.split('/')[-1]
    with open('D:/data/img/'+filename,'wb') as f:
        imgheaders = {
          "Accept" : "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
          "Accept-Encoding" : "gzip, deflate, br",
          "Accept-Language" : "zh-CN,zh;q=0.9",
          "Cache-Control" : "no-cache",
          "Pragma" : "no-cache",
          "Referer" : "https://pos.baidu.com/",
          "Sec-Ch-Ua" : "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
          "Sec-Ch-Ua-Mobile" : "?0",
          "Sec-Ch-Ua-Platform" : "\"macOS\"",
          "Sec-Fetch-Dest" : "image",
          "Sec-Fetch-Mode" : "no-cors",
          "Sec-Fetch-Site" : "cross-site",
          "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }
        imgresponse = requests.get(url=href,headers=imgheaders)
        f.write(imgresponse.content)
        print(filename,'下载成功')
# 老师 pdf怎么下载
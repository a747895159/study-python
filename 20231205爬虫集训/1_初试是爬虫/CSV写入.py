import pandas as pd
import requests

url = 'http://www.xinfadi.com.cn/getCat.html'
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "www.xinfadi.com.cn",
    "Origin": "http://www.xinfadi.com.cn",
    "Pragma": "no-cache",
    "Referer": "http://www.xinfadi.com.cn/index.html",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "x-yh-requestfeature": "zhoubin"
}
data = {
    "prodCatid": 1186
}
response = requests.put(url, headers=headers, data=data)
print(type(response.text))
obj = response.json()
print(obj['list'])
f = open('D:/data/data.csv','w',encoding='utf-8-sig')
f.write('名称,均价\n')
for item in obj['list']:
    f.write(f"{item['prodName']},{item['avgPrice']}\n")
f.close()
print('写入成功')
pd.DataFrame(obj['list']).to_csv('D:/data/pdd001.csv', encoding='utf-8-sig', index=False)


import subprocess
from functools import partial

import execjs
import requests
import json

subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

url = 'https://mgw.yiche.com/site_api/quote/api/car/get_car_list'

cityId = "2401"

param = {
    "cid": "508",
    "param": {
        "serialSpell": "siyucivic",
        "cityId": "2401"
    }
}

header = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Cid": "508",
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": "CIGUID=dcb90cecba7cc71d726327861b0161fa; auto_id=ca805d8fdff3339b9062ee993e97489e; selectcity=310100; selectcityid=2401; selectcityName=%E4%B8%8A%E6%B5%B7; isWebP=true; locatecity=310100; bitauto_ipregion=116.234.204.97%3A%E4%B8%8A%E6%B5%B7%E5%B8%82%3B2401%2C%E4%B8%8A%E6%B5%B7%2Cshanghai; CIGDCID=E74yfC4F8h8CAFeGJaQjAkSG5mYQGS4t; Hm_lvt_610fee5a506c80c9e1a46aa9a2de2e44=1702348776; csids=6580; UserGuid=dcb90cecba7cc71d726327861b0161fa; Hm_lpvt_610fee5a506c80c9e1a46aa9a2de2e44=1702349391",
    "Origin": "https://car.yiche.com",
    "Pragma": "no-cache",
    "Referer": "https://car.yiche.com/siyucivic/peizhi/",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

f = open('yiche02.js', mode="r", encoding="utf-8")
js_code = f.read()
js = execjs.compile(js_code)

edata = {
    "serialSpell": "siyucivic",
    "cityId": cityId
}

print("--"*20)

# 动态传参，调用JS
js_headers = js.call("fn", url, edata, "POST", "v10.71.0", cityId)

header.update(js_headers)
resp = requests.post(url, json=param, headers=header)
print(resp.text)


# 请求第二个Url
url2 = 'https://mapi.yiche.com/web_api/car_model_api/api/v1/car/config_new_param'

param2 = {
    'cid': '508',
    'param': '{"cityId":"2401","serialId":"1661"}'
}
edata2 = {
    "cityId": cityId,
    "serialId": "1661"
}

# print(js.call("add", 3, 5))
print("--"*20)
# 动态传参，调用JS
js_headers = js.call("fn", url2, edata2, "GET", "v10.80.0", cityId)
header.update(js_headers)
resp = requests.get(url2, params=param2, headers=header)

item = resp.json()['data'][0]['items'][0]
# 格式化打印JSON数据，缩进4格
formatted_data = json.dumps(item, ensure_ascii=False, indent=4)
print(formatted_data)

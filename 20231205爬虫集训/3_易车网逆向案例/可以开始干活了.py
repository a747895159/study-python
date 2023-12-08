# 你需要执行写好的js代码. 需要用到execjs模块
# pip install pyexecjs
# 大坑:  如果不做任何处理. 直接使用, 会出现中文乱码问题. 或者干脆就报错.
# 以下三句话写在程序的开头
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

import execjs
import requests

url = "https://mapi.yiche.com/web_api/car_model_api/api/v1/car/config_new_param"  # 干掉?后面的东西

# 为了减少出错的概率. 才这样拆的.
param = {
    "cid": "508",
    # 浏览器自动的处理了这里的特殊符号
    "param": '{"cityId":"201","serialId":"1661"}'
}

headers = {
    # 请求的内容是什么格式的.
    "content-type": "application/json;charset=UTF-8",
    # 用来记录服务器和浏览器之间的会话.
    "cookie": "auto_id=6ae32b66b9af3d48b7c670281066438a; selectcity=110100; selectcityid=201; selectcityName=%E5%8C%97%E4%BA%AC; UserGuid=3b0fec58-e8fc-4a83-b1b6-672adbe11c76; CIGUID=3b0fec58-e8fc-4a83-b1b6-672adbe11c76; CIGDCID=wFsTnfJDfExHEfSXsJP6EcQX68ad7TCE; csids=2406; isWebP=true; locatecity=110100; bitauto_ipregion=120.244.62.183%3A%E5%8C%97%E4%BA%AC%E5%B8%82%3B201%2C%E5%8C%97%E4%BA%AC%2Cbeijing; Hm_lvt_610fee5a506c80c9e1a46aa9a2de2e44=1701937780; Hm_lpvt_610fee5a506c80c9e1a46aa9a2de2e44=1701949621",
    # 防盗链 -> 记录本次请求是在哪一个请求里面携带的.
    "referer": "https://car.yiche.com/siyucivic/peizhi/",
    # 用户的浏览器设备的版本. 如果你不改它. 会惹大麻烦.
    # 这是对服务器最基本的尊重.
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# 加载js代码
f = open('my_js.js', mode="r", encoding="utf-8")
js_code = f.read()
js = execjs.compile(js_code)
js_headers = js.call("fn")
# print(js_headers)
# 更新进我们的请求头
headers.update(js_headers)

resp = requests.get(url, params=param, headers=headers)
print(resp.text)

# 如果服务器返回的是一个json. 你也得到的这个json
# 只能证明, 你和服务器之间的网络是通的
# {"message":"公共参数缺失","status":"11036"} 没有人能告诉你. 你缺了什么.
# 你要和浏览器对比.
# 浏览器返回的可不是这样.

# 通过对比. 发现. 请求头里. 貌似多了一大堆恶心人的东西.

# 通过分析. 得知. x-sign和x-timestamp是动态变化的.
# 我们得在我们的程序中. 复刻出来. 浏览器的对这两个参数的计算过程.

# 我们需要去浏览器中找到这两个参数的生成过程. 在我们的程序中, 复刻出来. 计算的逻辑. 得到的结果得是一致的.
# 这个过程叫逆向.

# 骨架 + 化妆 + 聪明的大脑
# html + css + js

# 需要有一些js的语法的基础...
# 听我的...

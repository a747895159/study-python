# 需要调用js代码
# pip install pyexecjs
# 该模块有坑. 对中文不友好. 有乱码的问题.
# 这三句话是固定的. 这三句话放在所有代码的第一行.
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

import execjs
import requests

# 加载js代码
f = open("caifu.js", mode="r", encoding="utf-8")
js_content = f.read()
f.close()

js = execjs.compile(js_content)

# 发请求需要的东西.
url = "https://www.zhitongcaijing.com/immediately/content-list.html"

param = {
    "type": "all",
    # "token": "c25c9276113de8e3b4bd35110d869e53d5d811da",
    # 这个值. 是上一次请求. 返回来的最后一条数据的时间.
    "last_update_time": "1702554924",  # 这个是观察来的.
    "platform": "web",
}

# 计算token
token = js.call("fn", param)
print(token)

param["token"] = token

# 发请求, 发请求的时候请注意, 一定要带着请求头.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

resp = requests.get(url, params=param, headers=headers)
print(resp.text)
# 如果想要下一页数据. 需要从这次结果中. 解析出最后一条数据的create_time
# 作为下一次请求的last_update_time值带过去.

# param["last_update_time"] = 新值.

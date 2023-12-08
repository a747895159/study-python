import concurrent.futures
import os

import requests

filepath = 'D:/data/day02/'
videoname = 'D:/data/video/video_day01.mp4'
url = "https://btt-vod.xiaoeknow.com/522ff1e0vodcq1252524126/e31b9b193270835013148846131/playlist_eof.m3u8?sign=6e2aedac7afc598667cb87a9a1c638d1&t=6573821c&us=WIqlgNIVjk"
header = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Origin": "https://appl2m4pcpu3553.pc.xiaoe-tech.com",
    "Pragma": "no-cache",
    "Referer": "https://appl2m4pcpu3553.pc.xiaoe-tech.com/",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

imgheaders = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Origin": "https://appl2m4pcpu3553.pc.xiaoe-tech.com",
    "Pragma": "no-cache",
    "Referer": "https://appl2m4pcpu3553.pc.xiaoe-tech.com/",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

baseVideoUrl = "https://btt-vod.xiaoeknow.com/522ff1e0vodcq1252524126/e31b9b193270835013148846131/"

# 如果文件夹已存在 还去创建 就会报错
if not os.path.exists(filepath):
    os.mkdir(filepath)

videoResp = requests.get(url, headers=header)
videoText = videoResp.text
videoText.split("\n")
tsArr = []
fileName = []


def str_filter(s):
    return not s.startswith('#') and s.strip() != ''


for a in videoText.split("\n"):
    a1 = a.strip()
    if str_filter(a1):
        tsArr.append(baseVideoUrl + a1.strip())
        fileName.append(a1.split("?")[0])

print('该视频文件个数:', len(tsArr))


def worker(tsurl, tsfilename):
    with open(filepath + tsfilename, 'wb') as f:
        tsresponse = requests.get(url=tsurl, headers=imgheaders)
        if tsresponse.status_code == 200:
            f.write(tsresponse.content)
        else:
            print('下载文件失败:', url)


with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    for i in range(len(tsArr)):
        executor.submit(worker, tsArr[i], fileName[i])

executor.shutdown(wait=True)

print('所有文件下载成功总共: ', len(tsArr))


def merge(filenames, dirname, video=videoname):
    # 先用一个文件保存所有的文件路径(格式：file '***.ts')
    path = os.path.join(dirname, 'path.txt')
    with open(path, 'w+') as f:
        for filename in filenames:
            f.write("file '%s'\n" % os.path.join(filename))

    os.chdir(dirname)
    os.system('ffmpeg -f concat -safe 0 -y -i %s -c copy -strict -2 %s' % (path, video))


merge(fileName, filepath)

os.rmdir(filepath)

print('视频合成成功')




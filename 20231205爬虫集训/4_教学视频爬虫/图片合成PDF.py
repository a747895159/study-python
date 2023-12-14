import requests
from PIL import Image
import os

folder = 'D:/data/day02/'

def download_pic():

    url = "https://openapi.bestsign.cn/openapi/v2/contract/preview?signType=token&developerId=1548134996017589119&sign=eyJkZXZlbG9wZXJJZCI6IjE1NDgxMzQ5OTYwMTc1ODkxMTkiLCJjYXRhbG9nSWQiOiI0NTgwODU0NTM5MDg5MTExMzE5IiwiY29udHJhY3RJZCI6IiIsImV4cGlyZUF0IjoiMTcwMzAzOTY1OSIsImFjY291bnQiOiIxNzYyMTc2MDk5NCJ9LjE3MDI0MzQ4NTkyODM4OTM2.8fd1d4b1ea99cf2dccfcf98a43044aa6&rtick=1702519623009&quality=100&contractId=170243485801000044&pageNum="

    url2 ="https://openapi.bestsign.cn/openapi/v2/contract/preview?signType=token&developerId=1548134996017589119&sign=eyJkZXZlbG9wZXJJZCI6IjE1NDgxMzQ5OTYwMTc1ODkxMTkiLCJjYXRhbG9nSWQiOiI0NTgwODU0NTM5MDg5MTExMzE5IiwiY29udHJhY3RJZCI6IiIsImV4cGlyZUF0IjoiMTcwMzAzOTY1OSIsImFjY291bnQiOiIxNzYyMTc2MDk5NCJ9LjE3MDI0MzQ4NTkyODM4OTM2.8fd1d4b1ea99cf2dccfcf98a43044aa6&rtick=1702519623009&quality=100&contractId=170243485701000085&pageNum="

    header = {
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Host": "openapi.bestsign.cn",
        "Pragma": "no-cache",
        "Referer": "https://openapi.bestsign.cn/fe/intf/v2/",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "image",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    for i in range(1, 6):
        resp = requests.get(url + str(i), headers=header)
        with open(folder + "pic" + str(i) + ".png", 'wb') as f:
            f.write(resp.content)

    print("下载完成")

def combine_imgs_pdf(folder_path, pdf_file_path):
    """
    Args:
    folder_path (str): 源文件夹
    pdf_file_path (str): 输出路径
    """
    files = os.listdir(folder_path)
    png_files = []
    sources = []
    for file in files:
        if 'png' in file or 'jpg' in file:
            png_files.append(folder_path + file)
    png_files.sort()
    output = Image.open(png_files[0])
    png_files.pop(0)
    for file in png_files:
        png_file = Image.open(file)
        if png_file.mode == "RGB":
            png_file = png_file.convert("RGB")
        sources.append(png_file)
    output.save(pdf_file_path, "pdf", save_all=True, append_images=sources)

if __name__ == "__main__":
    download_pic()
    pdfFile = r'D:/data/竞业协议.pdf'
    combine_imgs_pdf(folder, pdfFile)
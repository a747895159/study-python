# 招聘  有很多大的网站  非常非常难搞定
# 可以另辟蹊径 很多地方人才市场网站  有很多招聘信息
# 沈阳人才网
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

# f = open('沈阳人才网.csv','w',encoding='utf-8-sig')
# f.write('title,salary,company\n')
mainpageurl = "https://www.syrc.com.cn/job/"
mainpageheader ={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Referer": "https://www.syrc.com.cn/job/",
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
mainpageresponse = requests.get(url=mainpageurl,headers=mainpageheader)
time.sleep(1)
mainpageresponse.encoding = mainpageresponse.apparent_encoding
mainpagesoup = BeautifulSoup(mainpageresponse.text,"html.parser")
alist = mainpagesoup.find('div',class_="Search_jobs_sub_Box").find_all('a')[1:]
for a in alist:
    lavel1 = a.text
    lavel1url = a['href']
    response2 = requests.get(url=lavel1url,headers=mainpageheader)
    response2.encoding = response2.apparent_encoding
    time.sleep(1)
    soup2 = BeautifulSoup(response2.text,"html.parser")
    alist2 = soup2.find('div',class_="Search_jobs_sub").find_all('a')[1:]
    for a2 in alist2:
        level2 = a2.text
        level2url = a2['href']
        response3 = requests.get(url=level2url,headers=mainpageheader)
        response3.encoding = response3.apparent_encoding
        time.sleep(1)
        soup3 = BeautifulSoup(response3.text,"html.parser")
        alist3 = soup3.find('div',class_="Search_jobs_sub").find_all('a')[1:]
        for a3 in alist3:
            level3 = a3.text
            level3url = a3['href']
            dataresponse = requests.get(url=level3url,headers=mainpageheader)
            time.sleep(1)
            datasoup = BeautifulSoup(dataresponse.text,"html.parser")
            divs = datasoup.find_all('div',class_='search_job_list')
            titlelist = []
            salarylist = []
            companylist = []
            for div in divs:
                title = div.find('a',class_='yunjoblist_newname_a').text
                salary = div.find('span',class_='search_job_l_xz').text
                company = div.find('a',class_='search_job_com_name').text
                print(title,salary,company)
                titlelist.append(title)
                salarylist.append(salary)
                companylist.append(company)
                # f.write(title + ',' + salary + ',' + company + '\n')
            pd.DataFrame({'title':titlelist,'salary':salarylist,'company':companylist}).to_csv('沈阳人才网.csv',mode='a',encoding='utf-8-sig',index=False,header=False)
            print('爬取该页完成')
#
# f.close()

# 做一件事情   不要死脑筋
# 我们爬虫 是结果导向的


# 下沉市场    数分的单子  100一单  几十单
#                      500-1000  10
# 反复出现的概率极高  多点 美菜

# xlrd xlwt  xlsxwriter--->excel
# csv  ---> csv
# matplotlib ---> 画图

# flask/Django 大屏图    pyecharts

# GUI  Tkinter pyqt5

# 机器学习   很简单  但是  隔行如隔山
# 学的越多  能接的越多

# 数据处理




# 1.爬虫
# 2.数分(数据处理,办公自动化脚本,机器学习)
# 3.Python基础辅导
# 4.Python毕业设计   一般一年就   接个几单  就行了


# AI全能副业班 全套课程  (JS逆向     APP逆向  数据分析人工智能)送Django课程
#                       直播      直播       直播(周末班)     录播
#                    lucky/我/樵夫  沛齐      我             樵夫
#            简化版    (JS逆向 数据分析人工智能)送Django课程(樵夫 录播)


# APP Java(安卓开发) C(so加密)     核心技能  hook
# 脱壳   <------   要懂AOSP底层源码

# 1.确定自己的决心
# 2.要有学习的时间  以及兼职的时间
# 答疑 行业遥遥领先   +    课程质量
# 答疑老师越强  学生学习能力越弱...
# 有问题  我告诉你在哪里加打印  告诉你检查哪一块儿变量值 告诉你去看哪一课

# 明天是樵夫老师   带他家去跑一个js逆向案例...
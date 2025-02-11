import re

import pandas as pd

# 解析YAPI的接口文档

# 读取Markdown文件
with open('D:\\下载\\easy-api.md', 'r', encoding='utf-8') as file:
    content = file.read()

# 定义正则表达式模式
title_pattern = re.compile(r'^##\s+(.*)', re.MULTILINE)
path_pattern = re.compile(r'^\s\*\*Path:\*\*\s(.*)', re.MULTILINE)

# 查找所有标题和路径
titles = title_pattern.findall(content)
paths = path_pattern.findall(content)

# 调试信息
print("Titles found:", titles)
print("Paths found:", paths)

# 确保标题和路径的数量一致
if len(titles) != len(paths):
    print("标题和路径的数量不一致，请检查文件内容。")
else:
    # 将数据转换为DataFrame
    data_list = [{'Title': title, 'Path': path} for title, path in zip(titles, paths)]
    df = pd.DataFrame(data_list)

    # 保存到Excel文件
    df.to_excel('D:\\下载\\output-md.xlsx', index=False)

    print("Excel文件已生成: output.xlsx")

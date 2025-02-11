import json
import pandas as pd
import re

# http://localhost:8080/actuator/mappings SpringBoot项目所有接口解析

input_file = 'FeHelper-filemanager.json'
output_file = 'output-filemanager.xlsx'
app_name = 'filemanager-service'
package_name = 'com.buffaloex.filemanager.adapter'

file_path = 'C:\\Users\\zhoubin\\Desktop\\temp\\清关所有接口\\'

# 读取JSON文件
with open(file_path + input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)
# 使用正则表达式分割每个条目

# 初始化一个字典来存储类名和URL
class_url_map = {}
data = data.get('contexts').get(app_name).get('mappings').get('dispatcherServlets').get('dispatcherServlet')
# 遍历JSON数据
for entry in data:
    handler = entry.get('handler')
    if handler:
        class_name = handler.split('#')[0]
        if class_name.startswith(package_name):
            method_name = handler.split('#')[1].split('(')[0]
            patterns = entry.get('details', {}).get('requestMappingConditions', {}).get('patterns', [])

            # 简短类名
            short_class_name = class_name.split('.')[-1]

            if short_class_name not in class_url_map:
                class_url_map[short_class_name] = []

            class_url_map[short_class_name].extend(patterns)

# 将数据转换为DataFrame
data_list = []
for class_name, urls in class_url_map.items():
    for url in urls:
        data_list.append({'className': class_name, 'url': url})

df = pd.DataFrame(data_list)

# 保存到Excel文件
df.to_excel(file_path+output_file, index=False)

print("Excel文件已生成")

import pandas as pd


# 接口初始化sql 父页面Id、接口名称、接口key、接口Url、排序

# 根据导入的excel数据和sql模版(INSERT INTO `p_permission` (`parent_id`, `permission_type`, `permission_name`, `permission_code`, `permission_path`,`sort_flag`, `system_id`) VALUES (%s, 50, '%s', '%s', '%s', %s, 46);)生成python代码。其中%s为sql变量，excel有3列，页面id，页面名，url。
# 要求：
# 1.每行数据生成一条sql语句。
# 2.sql中第一个变量取页面Id;
# 3.sql中第二个变量取值逻辑为: 截取url后三位路径,将其中"/"换成".",去掉首位"/"字符;
# 4.sql中第五个变量取值逻辑为: 按照当前页面名分组，从1开始递增取值；
# 5.sql中第三个变量取值逻辑为: 取页面名按空格分组后三位+第五个变量。按照"_"拼接，全部小写。
# 6.sql中第四个变量取url。
# 7.所有的字符串都去除前后空格。


input_excel = "D:\\datum\\temp002\\清关菜单url.xlsx"
filename = "D:\\datum\\temp002\\sql.txt"

# 读取Excel数据
df = pd.read_excel(input_excel, sheet_name="Sheet1")


# 处理URL路径函数获取接口名称
def process_url(url):
    url = url.strip().lstrip("/")
    parts = url.split("/")
    if len(parts) >= 3:
        return ".".join(parts[-3:])
    return ".".join(parts)


# 生成权限码函数
def generate_permission_code(page_name, sorted_index):
    name_parts = page_name.replace('-', '_').strip().replace('-', '_').split()
    if len(name_parts) >= 3:
        return f"{'_'.join(name_parts[-3:])}_{sorted_index}"
    return f"{'_'.join(name_parts)}_{sorted_index}"


# 计算排序序号
df["sort_flag"] = df.groupby("页面名").cumcount() + 1

# 创建一个空集合来存储唯一的 url+页面名 组合
unique_set = set()

# 创建一个空列表来存储去重后的对象
unique_list = []

print('----'*30)
# 遍历数据列表
for _, item in df.iterrows():
    # 将 url 和 页面名 组合成一个唯一的字符串（这里使用简单的字符串拼接，但你也可以使用其他方法，如哈希）
    unique_key = item["url"] + " " + item["页面名"]

    if unique_key in unique_set:
        print(f"{unique_key} 已经存在，跳过")
    # 检查这个组合是否已经在集合中
    if unique_key not in unique_set:
        # 如果不在，则添加到集合和去重后的列表中
        unique_set.add(unique_key)
        unique_list.append(item)

# 生成SQL语句
sql_statements = []
for row in unique_list:
    parent_id = str(row["页面id"]).strip()
    page_name = row["页面名"].strip()
    url = row["url"].strip()

    # 接口名称
    interface_name = process_url(url)

    # 生成权限码
    permission_code = generate_permission_code(page_name, row['sort_flag']).lower()

    # 组装SQL
    sql = (
        f"INSERT INTO `p_permission` (`parent_id`, `permission_type`, `permission_name`, "
        f"`permission_code`, `permission_path`,`sort_flag`, `system_id`) VALUES "
        f"({parent_id}, 50, '{interface_name}', '{permission_code}', "
        f"'{url}', {row['sort_flag']}, 46);"
    )
    sql_statements.append(sql)

# 输出结果
# for sql in sql_statements:
#     print(sql)

print('----'*30)
# 打开文件以写入模式（'w' 表示写入，会覆盖文件；如果希望追加则使用 'a'）
with open(filename, "w") as file:
    for item in sql_statements:
        # 将每个元素写入文件并换行（'\n' 表示新行）
        file.write(item + "\n")

print(f"数据已成功写入到文件 {filename} 中。")
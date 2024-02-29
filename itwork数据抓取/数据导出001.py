import copy
import math
import time

import pandas as pd
import requests

from datetime import datetime
from excel_util import write_excel

# 1.authorization 鉴权
authorization = "47bddbf9-ccad-4731-a13c-9facb439e0c2"
# 2.请求Sql 语句中的 from 一定要小写; 最大仅支持1000条
# 循环查询数据，id 与 created_at 对应的sql字段中必有
query_sql = ""


# 3.应用编码
instance_id = 4198
# 4.数据库名称
db_name = "wms_inv_center"
# 5.环境变量 福州仓科
env = 1435
# 6.导出的文件路径
file_path = 'D:/data/数据导出001.xlsx'
# 7.每页条数
page_size = 1000

# 请求参数SQL,目前最大数据仅支持1000, 条件中from要小写
param = {
    "env": env,
    "limitNum": page_size,
    "sqlContent": query_sql,
    "instanceId": instance_id,
    "dbName": db_name,
    "explain": "false"
}


def exec_import():
    data_1 = send_data(param)
    write_data(data_1['rows'], data_1['column_list'])


def write_data(data, columns):
    curr_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'{curr_time},开始写入数据条数:{str(len(data))} ')
    df = pd.DataFrame(data, columns=columns)
    file_suffix = file_path.split(".")[1]
    # 写成csv格式数据
    if file_suffix == "csv":
        df.to_csv(file_path.split(".")[0] + ".csv", encoding='utf-8-sig', index=False)
    if file_suffix == "xlsx":
        # 将所有列转换为字符串类型
        write_excel(df, file_path)
    print('写入成功')


# 循环查询数据，id 与 created_at 对应的sql字段中必有
def exec_import_loop():
    # 校验数据量
    count = sql_count()
    curr_page = 1
    total_page = math.ceil(count / page_size)
    print(f"count 总数据条数:{count},总页数：{total_page}")
    # 首次查询
    query_param = copy.deepcopy(param)
    query_param['sqlContent'] = copy.deepcopy(query_sql) + " order by id desc,created_at asc"
    data_1 = send_data(query_param)
    data_list = data_1['rows']
    column_list = data_1['column_list']
    total = page_size
    last_id = int(data_list[-1][0])
    # 按照降序,循环查询数据,
    while count > total:
        query_param = copy.deepcopy(param)
        sql1 = copy.deepcopy(query_sql)
        # 按照Id降序 方式循环查询数据
        query_param['sqlContent'] = sql1 + " and id <" + str(last_id) + " order by id desc,created_at asc "
        location = str(curr_page) + '/' + str(total_page)
        try:
            data_2 = retry_send(query_param, location, 5)
        except Exception as e:
            curr_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{curr_time},当前位置: {location} ,last_id: {last_id},请求SQL: {query_param['sqlContent']}")
            print()
            raise e
        last_id = int(data_2['rows'][-1][0])
        data_list.extend(data_2['rows'])
        total = total + page_size
        time.sleep(1)
        curr_page += 1

    write_data(data_list, column_list)


# 追加数据
def append_data():
    data_1 = send_data(param)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time},追加数据条数：{str(len(data_1['rows']))}")
    file_suffix = file_path.split(".")[1]
    df_new = pd.DataFrame(data_1['rows'], columns=data_1['column_list'])
    # 写成csv格式数据
    if file_suffix == "csv":
        df = pd.read_csv(file_path, dtype=str)
        df = pd.concat([df, df_new], axis=0)
        df.to_csv(file_path, encoding='utf-8-sig', index=False)
    if file_suffix == "xlsx":
        df = pd.read_excel(file_path, dtype=str)
        df = pd.concat([df, df_new], axis=0)
        write_excel(df, file_path)
    print('追加结束')


def sql_count():
    count_param = copy.deepcopy(param)
    sql_0 = param['sqlContent']
    count_param['sqlContent'] = "SELECT count(*) " + sql_0[sql_0.find("from"):]
    data = send_data(count_param)
    c0 = data['rows'][0][0]
    int_c = int(c0)
    return int_c


def retry_send(sendparam, location,max_retries=5):
    retries = 0
    while retries < max_retries:
        try:
            data = send_data(sendparam)
            return data
        except Exception as e:
            # 发生异常时，打印错误信息，并重试
            retries += 1
            # 如果达到最大重试次数后仍然失败，抛出异常
            if retries == max_retries:
                raise e
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{current_time},当前位置: {location},异常重试：{retries},异常: {e}")
            time.sleep(2)


def send_data(sendparam):
    url = "http://public-service.sqldbms-front.gw.yonghui.cn/api/sql-workflow-dbms/v1/projects/211/sql/query"
    header = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Authorization": authorization,
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    # 设置链接超时 3秒，读取超时30秒
    resp = requests.post(url, json=sendparam, headers=header, timeout=(3.0, 30.0))
    resp.encoding = resp.apparent_encoding
    obj = resp.json()
    data = obj['data']
    if obj['code'] != 200000:
        raise Exception("异常1 " + resp.text)
    if data is None:
        raise Exception("异常2 " + resp.text)
    if isinstance(data, str):
        raise Exception("异常3 " + data)
    if data['rows'] is None:
        raise Exception("异常4 " + resp.text)
    return data


if __name__ == '__main__':
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'{current_time},开始执行')
    print('----'*30)
    # exec_import()
    exec_import_loop()
    # append_data()
    age = 21
    name = 'jiali'
    print('name:%s,age:%d' % (name, age))
    print()
    print('----'*30)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'{current_time},执行成功')

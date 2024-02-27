import copy
import time
import pandas as pd
import requests

from excel_util import write_excel

# 1.authorization 鉴权
authorization = "c27311a9-28e5-41cb-80c4-0481e1faf6c8"
# 2.请求Sql 语句中的 from 一定要小写; 最大仅支持1000条
# 循环查询数据，id 与 created_at 对应的sql字段中必有
query_sql = "SELECT id,receipt_no as '单号',receipt_status '状态',from_warehouse_id,created_at from  ibd_receipt where  created_at>'2023-12-11 00:00:00' and  created_at < '2024-01-01 03:00:00' and warehouse_id = 648270039501710466"
# 3.应用编码
instance_id = 4199
# 4.数据库名称
db_name = "wms_ibd_center"
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
    print('开始写入数据条数: ' + str(len(data)))
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
        data_2 = send_data(query_param)
        last_id = int(data_2['rows'][-1][0])
        data_list.extend(data_2['rows'])
        total = total + page_size
        time.sleep(1)

    write_data(data_list, column_list)


# 追加数据
def append_data():
    data_1 = send_data(param)
    print("追加数据条数：" + str(len(data_1['rows'])))
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
    print("count 总数据条数： " + c0)
    int_c = int(c0)
    return int_c


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
        print(resp.text)
        raise Exception("响应报文格式异常")
    if data is None:
        print(resp.text)
        raise Exception("响应报文数据异常")
    if isinstance(data, str):
        print(resp.text)
        raise Exception(data)
    if data['rows'] is None:
        print(resp.text)
        raise Exception("响应报文数据异常")
    return data


if __name__ == '__main__':
    # exec_import()
    exec_import_loop()
    # append_data()
    age = 21
    name = 'jiali'
    print('name:%s,age:%d' % (name, age))
    print(f'name:{name},age:{age}')

import copy

import pandas as pd
import requests

# 1.authorization 鉴权
authorization = "c27311a9-28e5-41cb-80c4-0481e1faf6c8"
# 2.请求Sql 语句中的 from 一定要小写; 最大仅支持1000条
query_sql = "SELECT id,receipt_no as '单号',receipt_status '状态',from_warehouse_id,created_at from  ibd_receipt where  created_at>'2024-01-01 00:00:00' and  created_at < '2024-01-01 03:00:00' and warehouse_id = 648270039501710466"
# 3.应用编码
instance_id = 4199
# 4.数据库名称
db_name = "wms_ibd_center"
# 5.导出格式 CSV 或者 EXCEL
export_format = "EXCEL"
# 6.环境变量 福州仓科
env = 1435

# 请求参数SQL,目前最大数据仅支持1000, 条件中from要小写
param = {
    "env": env,
    "limitNum": 5,
    "sqlContent": query_sql,
    "instanceId": instance_id,
    "dbName": db_name,
    "explain": "false"
}


def exec_csv(format, validate_count):
    # 校验数据量
    if validate_count == 1:
        sql_count()
    # exec_sql = copy.deepcopy(param)
    data_1 = send_data(param)
    print('开始写入')
    # print(data_1['rows'])
    # print(data_1['column_list'])

    df = pd.DataFrame(data_1['rows'], columns=data_1['column_list'])
    # 写成csv格式数据
    if format == "CSV":
        df.to_csv('D:/data/数据导出001.csv', encoding='utf-8-sig', index=False)
    if format == "EXCEL":
        # 将所有列转换为字符串类型
        with pd.ExcelWriter('D:/data/数据导出001.xlsx') as writer:
            df.to_excel(writer, sheet_name='Sheet1', na_rep='', index=False)

    print('写入成功')


def append_excel():
    data_1 = send_data(param)
    print("追加数据条数：" + str(len(data_1['rows'])))
    file_path = 'D:/data/数据导出001 - 副本.xlsx'
    sheet_name = 'Sheet1'
    df_new = pd.DataFrame(data_1['rows'])
    df_existing = pd.read_excel(file_path)
    df_existing = pd.concat([df_existing, df_new], axis=0)
    df_existing.to_excel(file_path, index=False, na_rep='')
    # 将新数据追加到原始 Excel 文件的尾部  if_sheet_exists='replace'  pd
    # with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
    #     df_existing.to_excel(writer, sheet_name=sheet_name, index=False, na_rep='', header=True)

    # df_new = pd.DataFrame(data_1['rows'])
    # df_existing = pd.read_excel(file_path)
    # df_existing = pd.concat([df_existing, df_new])
    # df_existing.to_excel(file_path, index=False, na_rep='', header=False)

    print('追加结束')


def sql_count():
    count_param = copy.deepcopy(param)
    sql_0 = param['sqlContent']
    count_param['sqlContent'] = "SELECT count(*) " + sql_0[sql_0.find("from"):]
    data = send_data(count_param)
    c0 = data['rows'][0][0]
    print("总数据条数： " + c0)
    int_c = int(c0)
    if int_c > 1000:
        raise Exception("仅支持1000以内的数据导出")
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
    exec_csv(export_format, 1)
    # append_excel()

import csv

import pandas as pd

data = [
    ['926263723671810048', 'SH24010100277A80A01', '3', '', '2024-01-02 00:01:20.852000'],
    ['926263724758327297', 'SH24010100279AA1C00', '3', '', '2024-01-02 00:01:21.109000'],
    ['926263725928345600', 'SH2401010027BD60600', '3', '', '2024-01-02 00:01:21.387000'],
    ['926287044316622848', 'SH2401010AC25B40A00', '3', '', '2024-01-02 01:34:00.922000'],
    ['926287044475654144', 'SH2401010AC26080600', '3', '', '2024-01-02 01:34:00.964000']
]

header = ['id', '单号', '状态', 'from_warehouse_id', 'created_at']

file_path = 'D:/data/数据导出001 - 副本.csv'

df_new = pd.DataFrame(data, columns=header)
df = pd.read_csv(file_path, dtype=str)
df = pd.concat([df, df_new], axis=0)
df.to_csv(file_path, encoding='utf-8-sig', index=False)

print('追加结束')

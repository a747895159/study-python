import numpy as np
import pandas as pd
from openpyxl.utils import get_column_letter
from pandas import ExcelWriter

data = [
    ['926263723671810048', 'SH24010100277A80A01', '3', '', '2024-01-02 00:01:20.852000'],
    ['926263724758327297', 'SH24010100279AA1C00', '3', '', '2024-01-02 00:01:21.109000'],
    ['926263725928345600', 'SH2401010027BD60600', '3', '', '2024-01-02 00:01:21.387000'],
    ['926287044316622848', 'SH2401010AC25B40A00', '3', '', '2024-01-02 01:34:00.922000'],
    ['926287044475654144', 'SH2401010AC26080600', '3', '', '2024-01-02 01:34:00.964000']
]

header = ['id', '单号', '状态', 'from_warehouse_id', 'created_at']

file_path = 'D:/data/数据导出001 - 副本.xlsx'

df_new = pd.DataFrame(data, columns=header)

df_existing = pd.read_excel(file_path, dtype=str)

df_existing = pd.concat([df_existing, df_new], axis=0)


# 写入excel时,自适应列的宽度
def to_excel_auto_width(df: pd.DataFrame, writer: ExcelWriter, sheet_name):
    """DataFrame保存为excel并自动设置列宽"""
    df.to_excel(writer, sheet_name=sheet_name, na_rep='', index=False)
    #  计算表头的字符宽度
    column_widths = (
        df.columns.to_series().apply(lambda x: len(x.encode('gbk'))).values
    )
    #  计算每列的最大字符宽度
    max_widths = (
        df.astype(str).map(lambda x: len(x.encode('gbk'))).agg("max").values
    )
    # 计算整体最大宽度
    widths = np.max([column_widths, max_widths], axis=0)
    # 设置列宽
    worksheet = writer.sheets[sheet_name]
    for i, width in enumerate(widths, 1):
        # openpyxl引擎设置字符宽度时会缩水0.5左右个字符，所以干脆+2使左右都空出一个字宽。大于50时取50
        w = (50 if width + 2 > 50 else width + 2)
        worksheet.column_dimensions[get_column_letter(i)].width = w


with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
    to_excel_auto_width(df_existing, writer, 'Sheet1')
    # df_existing.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='')
    # writer.sheets['Sheet1'].set_column('A:E', 30)

print('追加结束')

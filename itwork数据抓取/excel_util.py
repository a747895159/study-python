import numpy as np
import pandas as pd
from openpyxl.utils import get_column_letter
from pandas import ExcelWriter


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


def write_excel(df: pd.DataFrame, file_path):
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        to_excel_auto_width(df, writer, 'Sheet1')

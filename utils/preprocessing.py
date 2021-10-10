# encoding = utf-8
import re

def to_number(value):
    if type(value) in (int,float):
        return value
    else:
        values = re.findall(r'\d+\.?\d*',value.strip())
        if values:
            values = float(''.join(values))
            if '-' in value:
                values *= -1
            if '%' in value:
                 values /= 100
            return values

def scalar_data(data, column=[]):
    """数值化数据，将包含部分字符的列数据转换为float类型"""
    if type(column) != list:
        column = [column]
    for col in data.columns:
        is_number = False
        for key in ['数','额','率','比','变化','值','新访客']+column:
            if key in col:
                is_number = True
                break
        if is_number:
            data[col] = data[col].apply(to_number)
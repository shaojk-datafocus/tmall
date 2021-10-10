# encoding = utf-8
import re
import pandas as pd
from utils.preprocessing import scalar_data

data = pd.read_excel("【生意参谋平台】无线店铺流量来源-2021-10-03_2021-10-09.xls",header=5)
# print(data['访客数'].tolist())
# print(type(data['访客数'].str.extract(r'(\d*)',expand=True)))
scalar_data(data)
print(data['访客数'])
# data.sort_values('访客数',ascending=False,inplace=True) # 排序
# data.to_csv('result.csv', index=False, encoding='gbk')
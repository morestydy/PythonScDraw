# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 17:49:59 2020

@author: admin
"""


# =============================================================================
# 1. 缺失值的查找与处理
# =============================================================================
import numpy as np
import pandas as pd
from pathlib import Path

# Python原生None
a = None
# Numpy 的NaN
b = np.nan
# Pandas的NaT
c = pd.NaT

df = pd.read_csv(r'python_res\sample_data\datapreprocess.csv')
# 如何在程序中判断某个值否值为空值
# if pd.isna(a):
#     print('It is a None')

# if pd.isna(b):
#     print('It is a nan')
    
# if pd.isna(c):
#     print('It is a NaT')
# na_values参数使用，将需要视作空值的数值列入na_values中
df1 = pd.read_csv(r'python_res\sample_data\datapreprocess.csv',na_values=[' ','E'])
print(df1)
# 判断是否存缺失数据，对每一个值都进行判断，True为空值，最终生成布尔值矩阵
print(df1.isna())
# 判断每列是否存在缺失数据，True为某列存在有空值
print(df1.isna().any())
# 判断每行是否存在缺失数据，True为对应行存在有空值
print(df1.isna().any(axis=1)) #axis=1表示横向
# 判断dataframe是否存在缺失数据，True为该dataframe中存在有缺失值
print(df1.isna().any().any())

# 判断每列缺失数据的个数
print('判断每列缺失数据的个数:',df1.isna().sum())
# 判断每行缺失数据的个数
print('判断每行缺失数据的个数:',df1.isna().sum(axis=1))
# 全部dataframe缺失的数据个数
print('全部dataframe缺失的数据个数:',df1.isna().sum().sum())
# 删除缺失数据
df2 = df1.copy()
df3 = df1.copy()
df4 = df1.copy()
df6 = df1.copy()
df7 = df1.copy()
# 删除存在缺失值的列，此时如果需要将删除后的结果更新至df中，需要在括号中加入 inplace = True
df1.dropna(inplace=True)
print(df)
print(df1)
# 删除满足条件的缺失行
df2.dropna(axis=1,inplace=True)
print(df2)
# 填充缺失数据
values = {'temp':'37.0','height':'0'}
df3.fillna(value=values,inplace=True)
print(df3)
# =============================================================================
# 2. 重复数据的查找与处理
# =============================================================================
# 读入数据

# 查找重复的数据
print(df4.duplicated(keep=False))

# 删除重复的数据
df4.drop_duplicates(inplace=True)
print('删除重复的数据',df4)


# =============================================================================
# 3. 异常数据的查找与处理
# =============================================================================
# 读入数据
df5 = df4.copy()
# 异常数据的查找
print(df5[(df5.temp>40)|(df5.temp<30)])
# 异常数据的替换
# df5['temp'][df5[(df5.temp>42)|(df5.temp<36)]] = -1
df5.loc[((df5.temp>42)|(df5.temp<35)),'temp']=-1
print(df5)

print(df5.describe())
# =============================================================================
# 4. 离散化与面元划分
# =============================================================================
# 读入数据

# pd.cut()
bins = [0, 10, 18, 30, 50, 100]
label_list = ['儿童', '少年', '青年', '中年', '老年']
cats = pd.cut(df5.Age, bins, labels = label_list)

#在df中添加一列名为group的列，并填充每行数据对应的组别信息
df5['group'] = cats
print('pd.cut():\n',df5)
# 输出cut方法得到的每组样本数量
cats = pd.cut(df6.Age,4)
df6['group'] = cats
print(df6)
# pd.qcut()
# 输出qcut方法得到的每组样本数量
cats = pd.qcut(df7.Age,4)
df7['Group'] = cats
print(df7)
print(pd.value_counts(cats))
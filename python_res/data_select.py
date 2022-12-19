# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 01:11:09 2020

@author: admin
"""

# =============================================================================
# 1.按位置提取数据
# =============================================================================
import pandas as pd
from pathlib import Path

filepath = r'python_res\sample_data\data_selection.csv'
df = pd.read_csv(filepath,na_values=[' ','e'],encoding='gbk')
# 提取单行数据，注意索引是从0开始计数的，所以此处提取的是文件中第五行的数据
# print(df.iloc[4])

# 提取连续多行数据，注意提取时是左闭右开区间，即从索引为4的行，提取到索引为7的行
# print(df.iloc[4:8])
# 提取行数据时，也可以直接在df后面的中括号填写需要提取的行索引,效果等同于df.iloc[4:8]
# print(df[4:8])

# 注意在df后不能跟单一数值表示提取某一行，如果想提取索引为N的行数据，可以使用df.loc[N]或df[N:N+1]
# 注意使用df直接提取行数据时，不能使用逗号的隔开行索引的方式提取不连续行数据


# 提取前N行数据
# print(df.head(2))

#提取最后N行数据
# print(df.tail(2))

# 采用行索引提取不连续行数据
# print(df.iloc[[0,1,3,5,9]])

# 采用布尔值提取行数据，一定要确认布尔值元素个数的数量应该与数据行数是一致的
# print(df.iloc[[True,True,False,False]])

# 使用列索引，提取单列数据，注意逗号前要写上冒号才能提取该列的所有数据
# print(df.iloc[:,3])

# 提取连续多列数据，注意此时提取是左闭右开区间，即从列索引为1的列，提取到列索引为4的列
# print(df.iloc[:,3:8])

# 采用列索引提取不连续列数据，注意此时需要将需要提取的列索引序号写入在中括号中
# print(df.iloc[:,[0,3,5]])

# 采用布尔值提取列数据，注意不要将布尔值序列放入中括号，并且确认布尔值的个数是与列的数量是一致的
# print(df.iloc[:,[True,False,False,True,False,False,True]])
# print(df.iloc[lambda a:a.index%2==0])

# =============================================================================
# 2. 按标签提取数据
# =============================================================================

# 当行索引为默认的数字时，使用loc提取单行数据
# print(df.loc[1])
# 当行索引为默认的数字时，使用loc提取连续多行数据,注意此时是左闭右闭的区间，提取从行索引名称为4到行索引名称为8的所有行数据
# print(df.loc[1:3])

# 自定义数据的行索引
df.index = ['a', 'b' , 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# 当行索引为自定义的字符时，使用loc提取单行数据
print(df.loc['e'])
# 当行索引为自定义的字符时，使用loc提取连续多行数据,注意此时是左闭右闭的区间，提取从行索引名称为e到行索引名称为i的所有行数据
# print(df.loc['e':'h'])

# 采用行标签提取不连续行数据
# print(df.loc[['a','c','f']])
# 采用布尔值提取行数据,注意记得将布尔值放入中括号中，另外需要确认布尔值的个数与数据行的数据应该一致


# 提取单列数据
# 使用loc方法时，注意不要忘记冒号与逗号
# 另一种提取某单列数据的方法
# 提取列数据时，也可以直接在df后面的中括号填写需要提取的列名
# print(df.Gender)
# print(df['Gender'])
# print(df.loc[:,'Gender'])


# 也可以直接在中括号写入需要提取的多行的行标签，注意需要将他们放入中括号中
# 注意使用df直接提取列数据时，不能直接使用冒号做连续列的提取


# 提取连续多列数据
# print(df.loc[:,'ID':'Age'])
# 采用列标签提取不连续列数据，注意前面的冒号与逗号，还有需要提取的列名需要使用逗号隔开放入中括号中
# print(df.loc[:,['ID','Age']])
# 采用布尔值提取列数据，注意中括号与布尔值个数的确认




# =============================================================================
# 3. 按条件筛选数据
# =============================================================================
# 单个条件筛选
# 筛选年龄大于30的数据的所有行的全部数据，以下三种方式效果一样
# print(df[df.Age>30])
# print(df[df['Age']>=30])
# print(df[df.loc[:,'Age']>=30])

# 筛选年龄大于30的数据的所有行数据的Name列名字，以下两种方式效果一样
# print(df[['Name']][df.Age>30])
# print(df.Name[df.Age>30])

# 通过条件筛选多个列的信息
# print(df.Name[(df.Age>30)&(df.Name=='June')])


# 多个与条件筛选,注意每个条件放入括号内，并且用&符合连接多个条件
# print(df[['Name','Age']][(df.Age>30)&(df.Name=='June')])

# 多个或条件筛选，当条件涉及的是同一列数据，也可以采用第二种方式
# print(df[['Name','Age']][(df.Age>30)|(df.Name=='June')])
# 字符串模糊筛选，返回包含指定内容的数据，注意做模糊筛选的时候关键词之间使用|连接
# print(df[df['Diagnose'].str.contains('白血病|高血压')])
# 当需要返回同时包含多个关键词的数据时，可以将这些数据视作多个筛选条件，使用&进行连接即可
# print(df[df['Diagnose'].str.contains('白血病')&df.Diagnose.str.contains('高血压')])

# =============================================================================
# 5. 数据修改
# =============================================================================

# 修改列标签
# df.columns=['ID', '姓名', '体温', '年龄', '性别', '身高', '诊断']
# print(df)
# 同时修改部分列标签与行名称，在括号了换行是为了使我们对于参数的设置更加一目了然
# df.rename(columns={'ID':'序号'},index = {'a':'a1','b':'b2'},inplace = True)
# print(df)
# 修改某个元素
# df.loc['a','Age'] = 20
# print(df)
# 修改行索引为9所在行的所有数据
# df.loc[9] = [10, 'Mia', 37.2, 59, 2, 168.0, '糖尿病伴有高血压' ]
# print(df)
# 修改整个体温列的所有数据
# df.loc[:,'temp']=[36.5, 37.1, 37.0, 37.1, 36.9, 36.8, 37.1, 19.5, 36.7, 35.9]
# print(df)
# 修改部分数据
# df.loc[['d', 'f'], ['年龄','身高']] = [[20, 158], [25, 181]]
# print(df)
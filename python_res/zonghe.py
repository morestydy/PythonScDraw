import enum
from pickle import TRUE
import pandas as pd
from pathlib import Path

filepath = Path('python_res\\zonghe')
df = pd.DataFrame()
for index, file in enumerate(filepath.rglob("*.csv")):
    # print(index,file.name)
    data = pd.read_csv(file,na_values=' ')
    if df.empty:
        df = data
    else:
        df = pd.merge(df,data,how='outer')
    newer = 'dataset_'+str(index+1)+'.csv'
    file.rename(file.parent / newer)

# 数据的排序
df.sort_values(by='id',inplace=True)
# 缺失值值删除
df.dropna(how='all',inplace=True)
# 重复值处理
df.drop_duplicates(inplace=True)
# 年龄进行面源切分
ages = df.Age
age_bins = [0,18,30,50,100]
age_group = [1,2,3,4]
df['Group'] = pd.cut(ages,age_bins, labels=age_group)
# 分组变换
df_div = pd.get_dummies(df,columns=['Group'],prefix='G')

# 写入文件
df_div.to_csv('./zonghe.csv',index=False)
# print(df.tail())
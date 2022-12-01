import pandas as pd

# txt文件读取csv文件读取
# data = pd.read_csv(r'python_res\sample_data\sample.txt',sep=' ')
# csv
# data = pd.read_csv(r"python_res\sample_data\sample.csv",usecols=['ID','temp']) #前几列 ==>usecols=[1;3]
# data1 = pd.read_csv(r'python_res\sample_data\sample.csv',nrows=2)# 读前几行

# print(data1)

### 写入txt
# 覆写
# data.to_csv('./sam.csv',index=False,encoding='utf_8_sig')
# # 追加
# data.to_csv('./sam.csv',mode='a',header=False)# header=false不重复写入列名

### Excel文件的读写

# 单一sheet
# data = pd.read_excel('sample.xlsx')
# 多个sheet读取
# usecols:读取指定列名 sheet_name读取指定sheet
# data = pd.read_excel('python_res\sample_data\sample.xlsx',sheet_name='Sheet2',usecols=['ID','Name'])
# data1 = pd.read_excel('python_res\sample_data\sample.xlsx',sheet_name='Sheet2',usecols=['ID','Name'])
#Excel文件的写入
# 写入单一sheet
# data.to_excel('filepath',sheet_name='sheet1',index=False)
# 同时写入多个sheet
# filepath = './sam.xlsx'
# with pd.ExcelWriter(filepath) as f:#index=false写入时不写入行索引
#     data.to_excel(f,sheet_name='sheet1',index=False)
#     data1.to_excel(f,sheet_name='sheet2',index=False)

# print(data)

# sas文件读取
# data = pd.read_sas('file')
# data = pd.read_spss('file')
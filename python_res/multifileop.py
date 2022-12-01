from imp import find_module
import pandas as pd
from pathlib import Path
import shutil

# =============================================================================
# 1. 获取目录下文件列表
# =============================================================================

#import chardet

#获取当前工作目录
# print(Path.cwd())
#创建Path实例
# file = Path('python_res\multi_samplt\sample.txt')
# 文件的绝对路径
# print(file.absolute())
# print(file.parent)
# print(file.name)
# print(file.suffix)
#文件的上一级文件名

#文件全名（包含文件后缀）

#文件名（不包含文件后缀）

# 文件后缀名


#获取目录的子目录或文件
# folder = Path(r'python_res\multi_samplt')
# for i in folder.iterdir():
#     print(i.name)
#获取目录下所有文件列表
# folder = Path(r'python_res\multi_samplt')
# for i in folder.rglob('*.*'):
#     print(i.name)

# =============================================================================
# 2. 文件批量移动
# =============================================================================
# 将所需文件拷贝到下列目标目录下
# filepath = Path(r'python_res\multi_samplt')
# dstpath = Path(r"python_res\dstfile")
# for i in filepath.rglob('*.csv*'):
#     shutil.copy(i,dstpath)

# 如果目标目录不存在，则创建这个目录

# filepath = Path(r'python_res\multi_samplt')
# dstpath = Path(r"python_res\dstfile")
# # shutil.rmtree(dstpath)# 删除非空目录
# if not dstpath.exists():
#     dstpath.mkdir()
# for i in filepath.rglob('*.csv*'):
#     shutil.copy(i,dstpath)
# 将需要的文件拷贝到目标目录下

# =============================================================================
# 3. 文件重命名
# =============================================================================
dstpath = Path(r"python_res\dstfile")
filelist = dstpath.rglob('*.csv')

for index,f in enumerate(filelist):
    name = 'testdata'+str(index+1)+'.csv'
    f.rename(f.parent/name)
# =============================================================================
# 4. 文件批量合并
# =============================================================================
# 如果文件中不存在中文，则直接合并即可

#如果文件中存在中文，出现乱码时，可以先获取文件编码格式，然后再读取相关内容
#注意自动获取编码时，需要先导入import chardet
# 获取文件编码类型的函数
# def get_encoding(file):
#     # 二进制方式读取，获取字节数据，检测类型
#     with open(file, 'rb') as f:
#         data = f.read()
#         return chardet.detect(data)['encoding']
    
# scrfolder = Path('./sample_data')
# mergeData = pd.DataFrame()
# for file in scrfolder.rglob('*.csv'):
#     #先获取文件的编码
#     file_encoding = get_encoding(file)
#     #读取文件的时候采用相对应的编码去去读
#     df = pd.read_csv(file, encoding = file_encoding)
#     mergeData = mergeData.append(df)
# mergeData.to_csv('./alldata.csv', index = False, encoding = 'utf_8_sig')



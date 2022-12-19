from msilib.schema import tables
from tableone import TableOne
import pandas as pd

df = pd.read_csv(r'table\sample_data.csv')
columns_label = ['Age','SysABP','Height','Weight','LOS','ICU','death']
cate = ['ICU']

table1 = TableOne(df,
                    # columns=columns_label,
                    # categorical=cate,
                    missing=False,
                    overall=False,
                    groupby = 'death',
                    nonnormal=['Age222222222222222222','Height'],
                    pval=True,
                    htest_name=True,
                    smd=True,
                    min_max=['Age','Height'],
                    order={'ICU':['SICU','CSRU','MICU','CCU']})
print(table1.tabulate(tablefmt='latex'))
# table1.to_csv('./table1.csv')


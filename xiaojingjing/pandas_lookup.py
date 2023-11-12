"""pandas 查询数据几种方法
1、df.loc  根据行列的标签查询，**非常常用，且既能查询又能覆盖写入！！！！ df.loc[行标签，列标签]
2 df.iloc   根据行列的数字位置查询
3 df.where
4 df.query
"""
# df.loc 查询数据的five种方法
    #首先数据预处理：设定行列标签，数据格式和数字化
"""
#fpath2 = "D:/python\MyPython-学习过程与code/origin_data/deal_with_data.xlsx"
fpath2= "./deal_with_data.xlsx"
import pandas as pd
df = pd.read_excel(fpath2)
print(df.head(2))
#设定索引为第一列的id ，方便按照id查询
df.set_index('id',inplace=True)
#print('id1:',df.columns[-1])
#df['id'] = df.columns[0].astype('str')
#print('id:',df.columns[0])
#对某列字符串做 部分字符的替换str.replace /  分裂 str.split
df.loc[:,'temper']=df['temper'].str.replace('℃',"").astype('int32')
print(df.head(3))
#1 单个label值：精确查询某个单元格 或者series
#df.loc['23',['temper','loan_amount']]

#2 使用值列表，返回dataframe
#df.loc[['23','35'],['temper','loan_amount']]

#3 使用数值区间进行范围查询,注意区间既包含开始，也包含结束
#print(df.loc['35':'23','gender':'education'])

#4 使用条件表达式查询
#5 调用函数查询
"""
import pandas as pd
from openpyxl import load_workbook

# 读取 Excel 文件
excel_file = './晨会_副本.xlsx'

# 从 Sheet1 读取数据到 Pandas DataFrame
df = pd.read_excel(excel_file, sheet_name='原始数据-不要动 -数字化')

# 提取商品名、等级和年份作为透视表的索引和列
pivot_table = pd.pivot_table(df, index=['商品名', '等级'], columns='年份', values=['列名1', '列名2', ...], aggfunc='mean')

# 打开 Excel 文件并将透视表写入到 Sheet2
with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a') as writer:
    writer.book = load_workbook(excel_file)
    pivot_table.to_excel(writer, sheet_name='Sheet2')
    writer.save()



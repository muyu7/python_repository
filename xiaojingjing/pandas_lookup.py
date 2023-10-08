"""pandas 查询数据几种方法
1、df.loc  根据行列的标签查询，**非常常用，且既能查询又能覆盖写入！！！！ df.loc[行标签，列标签]
2 df.iloc   根据行列的数字位置查询
3 df.where
4 df.query
"""
# df.loc 查询数据的five种方法
    #首先数据预处理：设定行列标签，数据格式和数字化
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
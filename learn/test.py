"""
a = round(5.12245,2)
b='wang'
c=b+'%'
#print(c)
d=5
e=d+'%'
print(e)"""
import pandas as pd
d = {'a': 10, 'b': 2, 'c': 3}
# 遍历并拼接 
for i in range(len(ser)):
    ser[i]=str(ser[i])+'%'

print(ser)
# 截取部分serie
ser1=ser['b':]

closes=[1,2,3,4,5,6,7,8,9,0]
means=[]
for i in range(len(closes)-4):
    close=closes[i:i+5]
    print('i:',i,"+close:",close,"+close_len:",len(close))
    mean=sum(close)/len(close)
    means.append(mean)
print(means)
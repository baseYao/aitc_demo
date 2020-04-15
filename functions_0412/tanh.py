import numpy as np
import matplotlib.pyplot as plt

def tanh(x):
    return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
def softsign(x):
    return x/(1+np.abs(x))
#定义一个sign函数作为对比，这个函数x<0时为-1，x>0时为1
def sign(x):
    y = []
    for i in x:
        if i >0:
            y.append(1)
        elif i == 0:
            y.append(0)
        else:
            y.append(-1)
    return np.array(y)

x = np.arange(-5,5,0.01)
y2 = tanh(x)
y3 = softsign(x)
y4 = sign(x)
#为了更加直观，这里引入pandas进行封装
import pandas as pd
data = np.vstack((y2,y3,y4)) #将函数进行行拼接
put = pd.DataFrame(data.T,index=x,columns=['tanh','softsign','sign'])  #这里的data.T是将矩阵进行转置操作
put.plot()
plt.show()

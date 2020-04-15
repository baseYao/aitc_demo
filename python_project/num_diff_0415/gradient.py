import numpy as np
import matplotlib.pyplot as plt

def gradient(f,x,h=1e-4):
    #梯度计算
    grad = np.zeros_like(x)
    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x)
        x[idx] = tmp_val - h
        fxh2 = f(x)
        grad[idx] = (fxh1-fxh2)/(2*h)
        x[idx] = tmp_val
    return grad

def grad_desc(f,init_x,lr=0.01,step=100):
    x = init_x
    x_history = []  #记录历史坐标值
    for i in range(step):
        x_history.append( x.copy() ) #使用numpy的copy函数，而不是直接等于
        grad = gradient(f,x)
        x -= lr*grad
    return x,np.array(x_history)
#定义一个函数
def fun1(x):
    return x[0]**2+x[1]**2

#初始化的坐标
init_x = np.array([-3.0,4.0])
lr = 0.1  #上面默认是0.01，这里可以重新赋值
step = 20  #默认是100，这里重新赋值
x,x_history = grad_desc(fun1,init_x,lr=lr,step=step)

plt.plot( [-5, 5], [0,0], '--b')
plt.plot( [0,0], [-5, 5], '--b')
plt.plot(x_history[:,0], x_history[:,1], 'o')

plt.xlim(-3.5, 3.5)
plt.ylim(-4.5, 4.5)
plt.xlabel("X1")
plt.ylabel("X2")
plt.show()

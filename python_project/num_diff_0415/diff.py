import numpy as np
import matplotlib.pyplot as plt

#求导函数
#向前差分
def forward_diff(f,x,h=1e-4):
    return (f(x+h)-f(x))/h
#中心差分
def diff(f,x,h=1e-4):
    return (f(x+h)-f(x-h))/(2*h)

def fun(x):
    return x**2
x = np.arange(0,4,0.01)
f = fun(x)
#tanh函数在(2,4)处的倒数
dy = diff(fun,2)
plt.plot(x,f)
plt.plot(x,dy*(x-2)+4)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

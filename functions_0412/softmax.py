import numpy as np

def softmax(x):
    exp_x = np.exp(x)
    exp_x_sum = np.sum(exp_x)  #求和
    return exp_x/exp_x_sum
a = np.array([0.3,2.9,4.0])
out = softmax(a)
print("输出值：",out,"\n值的和：",np.sum(out))

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,5,0.01)
#ReLU函数
def relu(x):
    return np.maximum(0, x)
y5 = relu(x)
plt.plot(x,y5)
plt.show()

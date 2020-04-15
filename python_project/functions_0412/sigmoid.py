import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sgn(x):
    y = []
    for i in x:
        if i >=0:
            y.append(1)
        else:
            y.append(0)
    return np.array(y)

x = np.arange(-5,5,0.01)
y = sigmoid(x)
y1 = sgn(x)
plt.plot(x,y)
plt.plot(x,y1,'r--')
plt.show()

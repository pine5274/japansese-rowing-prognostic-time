import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(60, 110, 1000)
plt.figure(0)
plt.plot(x, 633.07*((x+22)/123)**(-2/9), label='2d')
plt.plot(x, 633.07 + (101-x) * 0.91, label='1d')
plt.title("men")
plt.xlabel('weight[kg]', fontsize=12) 
plt.ylabel('2000mTime', fontsize=12) 
plt.savefig('./../dst/weight/men.jpg')
plt.figure()

x = np.linspace(50, 100, 1000)
plt.figure(0)
plt.plot(x, 633.07*((x+22)/123)**(-2/9), label='2d')
plt.plot(x, 633.07 + (100-x) * 1.4, label='1d')
plt.title("women")
plt.xlabel('weight[kg]', fontsize=12) 
plt.ylabel('2000mTime', fontsize=12) 
plt.savefig('./../dst/weight/women.jpg')
plt.figure()
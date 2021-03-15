'''
Author: Ful Chou
Date: 2021-01-25 16:38:04
LastEditors: Ful Chou
LastEditTime: 2021-01-25 16:42:45
FilePath: /leetcode/sigmoid.py
Description: What this document does
'''

import matplotlib.pyplot as plt
import numpy as np
 
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS'] # 修改字体，让plt 可以显示中文
 
def sigmoid(x):
    # 直接返回sigmoid函数
    return 1. / (1. + np.exp(-x))
 
 
def plot_sigmoid():
    # param:起点，终点，间距
    x = np.arange(-8, 8, 0.2)
    y = sigmoid(x)
    plt.plot(x, y)
    plt.title('sigmoid 函数图像')
    plt.xlabel('x')
    plt.show()
    
 
 
if __name__ == '__main__':
    plot_sigmoid()
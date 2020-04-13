# -*- encoding: utf-8 -*-
'''
@file:2.2PerceptronDual.py
@description:感知机学习算法的对偶形式，输入：训练数据集，标签y,输出：参数w,b
@time:2020/04/13
@author:Wei
'''

import numpy as np
class Perceptron:
    def __init__(self, dataset, labels, eta): #初始化数据集，标签，学习率
        self.dataset = dataset
        self.labels = labels
        self.eta = eta

    def train(self):
        n, m = np.shape(self.dataset) #数据集有n个样本,每个样本有n维
        w = np.zeros(m)
        a = np.zeros(n) 
        gram = np.dot(dataset, dataset.T)   #与他的转置相乘，计算Gram矩阵
        # print(gram)
        b = 0 #bias
        t = 0 #计数，运行了几次
        print("%s : alpha,%s bias,%s" % (t,a,b))
        flag = True  #标志位来表示是否还存在误分类点
        while(flag):
            flag = False
            for i in range(n):
                temp = b
                for j in range(n):
                    temp += a[j] * self.labels[j] * gram[j][i]
                if((self.labels[i] * temp) <= 0): #判断是否误分类点,切记不要忘了标志位labels，即y
                    a[i] += self.eta #更新权重
                    b += self.eta * self.labels[i]  #更新偏置
                    t += 1  #计数加1
                    print("%s : alpha,%s bias,%s" % (t,a,b))
                    flag = True
        for i in range(n):
            w += a[i] * self.labels[i] * self.dataset[i]
        return w, b

if __name__ == "__main__":
    dataset = np.array([[3, 3], [4, 3], [1, 1]])
    labels = np.array([1, 1, -1])
    eta = 1  #设置学习率

    per = Perceptron(dataset, labels, eta)
    w, b = per.train()
    print("result: weights,%s bias,%s" % (w,b))

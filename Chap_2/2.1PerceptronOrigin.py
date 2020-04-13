# -*- encoding: utf-8 -*-
'''
@file:2.1PerceptronOrigin.py
@description:感知机学习算法的原始形式，输入：训练数据集，标签y,输出：参数w,b.
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
        n, m = np.shape(self.dataset) #数据集有n个样本，单个样本维度m
        w = np.zeros([1,m]) 
        b = 0 #bias
        t = 0 #计数，运行了几次
        print("%s : weights,%s bias,%s" % (t,w,b))
        flag = True  #标志位来表示是否还存在误分类点
        while(flag):
            flag = False
            for i in range(n):
                if(self.labels[i] * (w.dot(self.dataset[i])+b) <= 0): #误分类点
                    w += self.eta * self.labels[i] * self.dataset[i]  #更新权重
                    b += self.eta * self.labels[i]  #更新偏置
                    t += 1  #计数加1
                    print("%s : weights,%s bias,%s" % (t,w,b))
                    flag = True
        return w, b

if __name__ == "__main__":
    dataset = np.array([[3, 3], [4, 3], [1, 1]])
    labels = np.array([1, 1, -1])
    eta = 1  #设置学习率

    per = Perceptron(dataset, labels, eta)
    w, b = per.train()
    print("result: weights,%s bias,%s" % (w,b))



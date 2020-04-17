# -*- encoding: utf-8 -*-
'''
@file:kNN.py
@description:k近邻算法，输入：训练数据集，所属类别，实例特征向量x。输出：实例x所属的类别y
使用kd树实现kNN步骤：1.建立kd树 2.搜索kd树，寻找最近邻 3.多数表决，输出类别
@time:2020/04/16
@author:Wei
'''

import numpy as np 
import sys

class Node:
    def __init__(self, data, lchild = None, rchild = None):
        # 初始化节点
        self.data = data
        self.lchild = lchild   
        self.rchild = rchild

class KdTree:
    def __init__(self):
        self.KdTree = None
        self.m = 0 # 保存数据特征向量维度
    
    def create(self, dataset, depth = 0):  #建树
        if(len(dataset) > 0):   # 数据集长度要大于0
            n, self.m = np.shape(dataset) # 样本数n，单个样本维度m
            axis = depth % self.m # 选择切分坐标轴
            sortdataset = sorted(dataset, key=lambda x: x[axis]) #调用sort函数排序
            mid = int(n/2)  # 中位数位置
            node = Node(sortdataset[mid])
            # print(sortdataset[mid])
            node.lchild = self.create(sortdataset[:mid], depth+1)
            node.rchild = self.create(sortdataset[mid+1:], depth+1)
            return node 
        return None #返回None

    def preOrder(self,node):    #前序遍历，查看建树结果是否正确
        if(node != None):
            print(node.data)
            self.preOrder(node.lchild)
            self.preOrder(node.rchild)
    
    # def search(self, node, x, k=1):  # 最近邻算法
    #     self.nearestNode = None
    #     self.nearestDis = None

    #     def traverse(node, depth=0):
    #         if(node != None):
    #             axis = depth % self.m # 选择切分坐标轴,与第几个坐标进行比较
    #             # 找叶节点
    #             if(x[axis] < node.data[axis]):
    #                 traverse(node.lchild,depth+1)
    #             else: 
    #                 traverse(node.rchild,depth+1)

    #             # 判断当前点
    #             thisDist = self.dist(node.data, x)
    #             if np.all(self.nearestNode == None):    # 需要加np.all
    #                 self.nearestNode = node.data
    #                 self.nearestDis = thisDist
    #             elif(thisDist < self.nearestDis):
    #                 self.nearestNode = node.data
    #                 self.nearestDis = thisDist

    #             # 判断当前最邻近距离与父节点的子节点区域是否相交
    #             if(abs(x[axis]-node.data[axis]) < self.nearestDis):
    #                 if(x[axis] < node.data[axis]):
    #                     traverse(node.rchild, depth+1)
    #                 else:
    #                     traverse(node.lchild, depth+1)
        
    #     traverse(node)
    #     return self.nearestNode

    def search(self, node, x, k=1):  # 搜索，默认是最近邻算法
        self.nearest = []
        for i in range(k):  # 初始化nearest为None 距离为最大整数值
            self.nearest.append([None,sys.maxsize]) 
        # print(self.nearest)

        def traverse(node, depth=0):
            if(node != None):
                axis = depth % self.m # 选择切分坐标轴,与第几个坐标进行比较
                # 找叶节点
                if(x[axis] < node.data[axis]):
                    traverse(node.lchild,depth+1)
                else: 
                    traverse(node.rchild,depth+1)

                # 判断当前点
                thisDist = self.dist(node.data, x)
                for i in range(k):  
                    j = k-1-i   #确保出现小于nearest中dist时，不会直接替换掉原有记录。从后向前，先替换大的值。
                    if np.all(self.nearest[j][0]) == None:
                        self.nearest[j][0] = node.data  # 结点
                        self.nearest[j][1] = thisDist   # 距离
                        break   #防止重复赋值
                    elif(thisDist < self.nearest[j][1]):
                        self.nearest[j][0] = node.data
                        self.nearest[j][1] = thisDist
                        break
                
                self.nearest = sorted(self.nearest,key=lambda x: x[1])  # 升序排序


                # 判断当前最大的邻近距离 与父节点的子节点区域是否相交
                if(abs(x[axis]-node.data[axis]) < self.nearest[k-1][1]):
                    if(x[axis] < node.data[axis]):
                        traverse(node.rchild, depth+1)
                    else:
                        traverse(node.lchild, depth+1)
        
        traverse(node)
        return self.nearest


    def dist(self, x1, x2, p=2):    # 计算两个实例点之间距离，默认计算欧氏距离
        if(p == 0):  # 切比雪夫距离
            return np.abs(x1-x2).max()
        if(p == 1):  # 曼哈顿距离
            return np.sum(np.abs(x1-x2))  
        return np.sqrt(np.sum(np.square(x1-x2)))

def maxcount(dataset, y, result):   # 多数表决 确定x实例类别
    type = []   
    for i in range(len(result)):
        for j in range(dataset.shape[0]):
            if(np.all(result[i][0] == dataset[j])): # 找结果对应训练数据集下标
                type.append(y[j])
    print("该实例点的类别为：")
    return max(type, key=type.count) # max()的使用

if __name__ =="__main__":
    dataset = np.array([[2, 3], [5, 4], [9, 6], [4,7], [8,1], [7,2]])   #书P54 例3.2
    y = np.array([1, 1, 1, -1, -1, -1]) #随意取得
    x = [3, 4.5]    #测试实例

    kdt = KdTree()  #需要首先创建对象
    node = kdt.create(dataset)
    print("数据集建树结果：")
    kdt.preOrder(node)

    print("最近邻（k=1)结果:")
    result = kdt.search(node,x)
    print(result)
    print(maxcount(dataset, y, result))

    n = np.shape(dataset)[0]   # 训练数据集样本数
    k = input("输入k：")
    if int(k)>n:
        print("错误")
    else:
        print("k近邻结果:")
        result = kdt.search(node,x,int(k))
        print(result)
        print(maxcount(dataset, y, result))

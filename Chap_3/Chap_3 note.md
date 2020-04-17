# 第3章 k近邻法
k近邻法（k-nearest neighbor,k-NN）是一种基本分类与回归的方法。k近邻法的输入为实例的特征向量，对应于特征空间的点；输出为实例的类别，可以取多类。
k近邻法不具有显示的学习过程。
k值的选择、距离度量及分类决策规则是k近邻法的三个基本要素。
## 3.1 k近邻算法
给定一个训练数据集，对新的输入实例，在训练数据集中找到与该实例最邻近的k个实例，这k个实例的多数属于某个类，就把该输入实例分为这个类。
## 3.2 k近邻模型
### 3.2.1 模型
### 3.2.2 距离度量
特征空间中两个实例点的距离是两个实例点相似程度的反映。
![](https://github.com/RubbshiWei/StatisticalLearning-lihang/blob/master/image/3_1.png)
![](https://github.com/RubbshiWei/StatisticalLearning-lihang/blob/master/image/3_1.png)
p=无穷时，距离公式推导：
![](https://github.com/RubbshiWei/StatisticalLearning-lihang/blob/master/image/3_1.png)

参考：https://blog.csdn.net/W_peijian/article/details/79113020?utm_source=blogxgwz7
### 3.2.3 k值的选择
较小k值，意味着整体模型变得复杂，容易发生过拟合。选择较大k值，可以减少学习的估计误差，缺点是增大学习的近似误差，整体模型变得简单。如果k=N（样本数），这时模型过于简单，完全忽略训练实例中的大量有用信息，不可取。
实际应用中，选择较小的k值，并通过交叉验证法选择最优k值。
### 3.2.4 分类决策规则
k近邻法中的分类决策规选择多数表决，即由输入实例的k个邻近的训练实例中的多数类决定输入实例的类。
## 3.3 k近邻算法的实现：kd树
主要考虑如何对训练数据进行快速k近邻搜索
### 3.3.1 构造kd树
kd树是一种对k维空间中的实例点进行存储以便对其进行快速检索的树形数据结构。
![](https://github.com/RubbshiWei/StatisticalLearning-lihang/blob/master/image/3_1.png)
### 3.3.2 搜索kd树
![](https://github.com/RubbshiWei/StatisticalLearning-lihang/blob/master/image/3_1.png)
注意：  (a)与当前点（父节点）   (b)另一侧子节点

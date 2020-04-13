# 第2章 感知机
感知机是二类分类的线性分类模型，其输入为示例的特征向量，输出为实例的类别，取+1和-1二值。感知机学习旨在求出将训练数据进行线性划分的分离超平面，为此，导入基于互分类的损失函数，利用梯度下降法对损失函数进行极小化，求得感知机模型。
## 2.1 感知机模型
感知机是一种线性分类模型，属于判别模型。感知机模型的假设空间是定义在特征空间中的所有线性分类模型或线性分类器，即函数集合{f|f(x)=w·x+b}
## 2.2 感知器学习策略
### 2.2.1 数据集的线性可分性
给定一个数据集T，存在某个超平面S，w·x+b=0,能够将数据集的正示例点和负实例点完全正确地划分到超平面的两侧，则称该数据集为线性可分数据集。
### 2.2.2 感知机学习策略
目标：求得一个能够将训练集正实例点和负实例点完全正确分开的分离超平面。
策略：为确定感知机参数，w,b. 定义损失函数并将损失函数极小化。
![](https://github.com/RubbshiWei/StatisticalLearning-lihang/blob/master/image/2_1.png)     

任意一点x0到超平面S的距离推导：
参考：https://blog.csdn.net/yutao03081/article/details/76652943?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158676873719725211947849%2522%252C%2522scm%2522%253A%252220140713.130056874..%2522%257D&request_id=158676873719725211947849&biz_id=0&utm_source=distribute.pc_search_result.none-task-blog-blog_SOOPENSEARCH-2
![](https://github.com/RubbshiWei/StatisticalLearning-lihang/blob/master/image/2_2.png)

## 2.3 感知机学习算法
感知机学习问题转化为求解损失函数的最优化问题，最优化的方法是随机梯度下降法。
### 2.3.1 感知机学习算法的原始形式
当一个实例点被误分类，即位于分离超平面的错误一侧时，则调整w,b的值，使分离超平面向该误分类点的一侧移动，以减少该误分类点与超平面间的距离，直至超平面越过该误分类点使其被正确分类。
![](https://github.com/RubbshiWei/StatisticalLearning-lihang/blob/master/image/2_3.png)

### 2.3.2 算法的收敛性
根据定理证明，误分类的次数k是由上界的，经过有限次搜索可以找到将训练数据完全正确分开的分离超平面，即当训练数据集线性可分时，感知机学习算法原始形式迭代是收敛的。
感知机学习算法的解不是唯一的。当训练集线性不可分时，感知机学习算法不收敛，迭代结果会发生震荡。
### 2.3.3 感知机学习算法的对偶形式
![](https://github.com/RubbshiWei/StatisticalLearning-lihang/blob/master/image/2_4.png)

**Gram矩阵：**
提出：对偶形式中训练实例仅以內积的形式存在，方便计算（省的在训练过程中在进行单独计算），所以预先将训练实例间的內积计算出来并以矩阵的形式存储这个矩阵就是Gram矩阵。
![](https://github.com/RubbshiWei/StatisticalLearning-lihang/blob/master/image/2_5.png)

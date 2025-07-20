# Nonlinear Systems

## Ⅰ : Fixed Points for Functions of Several Variables

### Theorem
![1-1](1-1.png)
![1-2](1-2.png)
*将非线性系统的多个方程依次构造成每个变量的不动点问题，迭代即可。*  
*更快速的办法是已有的 $x_i^{(k)}$也直接代入当前第 k 次迭代要用的函数中。*

## Ⅱ : Newton's Method for Nonlinear Systems

### Theorem
![alt text](2-1.png)
![alt text](2-2.png)
![alt text](2-3.png)
![alt text](2-4.png)

**简单求矩阵的逆的方法：**
![简单求逆的方法](2-5.png)


### Gradient Descent Techniques
#### Background:
牛顿迭代法需要一个零点附近的p，如何寻找合适的p？
![Background](3-1.png)

#### Solution:
最陡下降法指的是为 g 寻找一个局部最小值。
首先代入初始值 x(0)，根据 x(0)得到 g 下降的方向，沿着这个方向移动合适的距离得到 x(1)。重复步骤即可。
1. 构造 g(x)
![3-2](3-2.png)
2. 递降 逼近
![3-3](3-3.png)
![示意图3-4](3-4.png)
3. 公式
![alt text](3-5.png)

#### Gradient Descent vs. Newton's Method:
![3-1](3-1.png)
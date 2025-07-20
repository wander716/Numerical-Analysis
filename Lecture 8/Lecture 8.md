# Solution of Differential Equations 微分方程的数值解法

## Ⅰ：Initial-Value Problems for ODEs 常微分方程中的初值问题
对一个常微分方程（或方程组）在给定初始条件下求解的问题。
#### 一、Introduction:
![Introduction](ODE-Introduction.png)
不同于数学上的常微分方程的解法。  
此处的常微分方程是用有限个点，去近似得到一个函数。或者只需要求 n 个点的函数近似值即可。
#### 二、 Lipschitz连续
**Definition：**
![def](<ODE-Lipschitz 连续.png>)
反例：
![反例](<ODE-Lipschitz 连续-反例.png>)
**凸集：**
![凸集](ODE-凸集.png)
**Lipschitz 连续的充分条件：**
![充分条件](<ODE-Lipschitz 连续-充分条件.png>)
#### 三、良态问题
**Definition：**
![def](ODE-良态问题定义.png)
**Theorem：**
![Theorem](ODE-良态问题定理.png)
*良态问题的意义：δ(t)是函数z(t)的误差项。根据定理显示，带有误差的 z(t) 与常微分方程 y(t) 的差值不超过 ke ，即误差是有界的。*
**Example：**
Q:
![1](ODE-良态问题-E1.png)
A:
![2](ODE-良态问题-E2.png)
验证：y(t)是可解的。
![3](ODE-良态问题-E3.png)
![4](ODE-良态问题-E4.png)

## Ⅱ：Euler's Method 欧拉方法
#### 一、Object：
![目标方程](欧拉方法-目标方程.png)
求 N+1 个点处的函数近似值
#### 二、Solution：泰勒多项式
![1](欧拉方法-1.png)

w是取了y的近似值。
![2](欧拉方法-2.png)

**示意图：**
![1](欧拉方法-示意图-1.png)
![2](欧拉方法-示意图-2.png)

#### 三、误差上界：
![误差上界](欧拉方法-误差上界.png)
（证明略）

#### 四、舍入误差：
![舍入误差-1](欧拉方法-舍入误差-1.png)
δ 是每次迭代产生的舍入误差  
L：Lipschitz常量  
M：y''(t) 的上界  
a：t 的下界  
$t_i$：由 i 、a、b 确定  
只有 h 是变量
![舍入误差-2](欧拉方法-舍入误差-2.png)

#### 五、Comments：关于 y''(t)  
劣：误差较大。  
优：*在未知 y(t) 的情况下，欧拉方程中 y''(t) 实际上是可求的。*
![comments](欧拉方法-分析.png)

## Ⅲ：Higher-Order Taylor Methods 高阶泰勒方法
#### 一、Object:
提高欧拉方法的精度。

#### 二、局部截断误差：
![局部截断误差-1](高阶泰勒-局部截断误差定义-1.png)
*假设 $y_i$ 是精确的，即 $ω_i$ = $y_i$，在此基础上分析 $y_{i+1}$ 的误差。*  
**欧拉方法的局部截断误差 如下：**
![局部截断误差-2](高阶泰勒-局部截断误差定义-2.png)


#### 三、分析欧拉方法的局部截断误差：
![局部截断误差-欧拉方法](高阶泰勒-局部截断误差-欧拉方法.png)

#### 四、Motivation:
*提高精度，即由 $0(h)$ -> $0(h^p)$*
![Motivation](高阶泰勒-Motivation.png)


#### 五、Solution:
**泰勒展开至更高阶。**
1. 泰勒展开至 n 阶
![1](高阶泰勒-Solution-1.png)
2. 利用迭代
![2](高阶泰勒-Solution-2.png)
3. 化简
![化简](高阶泰勒-化简.png)
4. 公式
![公式](高阶泰勒-公式.png)
最终误差项满足 $0(h^n)$
#### 六、Theorem:
*泰勒展开至 n 阶，即 n+1 阶是 $y^{(n+1)}(ξ_i)$，满足精度为 $0(h^n)$ 。*
![Theorem](高阶泰勒-Theorem.png)
**Proof:**
![Proof-1](高阶泰勒-Theorem-Proof-1.png)
![Proof-2](高阶泰勒-Theorem-Proof-2.png)


## Ⅳ：Runger-Kutta Methods 龙格库塔方法
#### 一、引入：
高阶泰勒方法需要多次求高阶导数，计算太复杂！
![引入](龙格库塔方法-引入.png)

#### 二、Solution
![1](龙格库塔方法-1.png)
![2](龙格库塔方法-2.png)
构造：
![3](龙格库塔方法-3.png)
![4](龙格库塔方法-4.png)
![5](龙格库塔方法-5.png)
![6](龙格库塔方法-6.png)
解得：
![7](龙格库塔方法-7.png)
验证：
![8](龙格库塔方法-8.png)

#### 三、Midpoint Method $0(h^2)$
![Midpoint Method](<龙格库塔方法-Midpoint Method.png>)

#### 四、3 阶 $0(h^3)$
![3阶](龙格库塔方法-3阶.png)

#### 五、4 阶 $0(h^4)$
![4阶](龙格库塔方法-4阶.png)

## Ⅴ：Systems of Differential Equations 求解微分方程组

#### 一、Systems of Differential Equations 微分方程组
![1](微分方程组-1.png)
代入龙格库塔方法
![2](微分方程组-2.png)
![3](微分方程组-3.png)

#### 二、Higher-Order Differential Equations 高阶微分方程
![1](高阶微分方程-1.png)
![2](高阶微分方程-2.png)

## Ⅵ：Boundary-Value Problems for ODEs 常微分方程的边值问题

#### 一、Introduction：
![Introduction-1](边值问题-Introduction-1.png)
**Theorem：存在性 & 唯一性**
![存在唯一性](边值问题-Introduction-存在唯一性.png)
（证明略）

#### 二、The Linear Shooting Method 线性打靶方法
**线性边值问题：**
![线性边值问题](线性打靶方法-线性边值问题-1.png)

**Solution：**
1. 构造2个初值问题。对于每一个初值问题，可以用龙格库塔方法求解。
![Solution-1](线性打靶方法-1.png)
2. 线性叠加
![Solution-2](线性打靶方法-2.png)

**验证合法性：**
即带入检验
![Proof-1](线性打靶方法-Proof-1.png)
![Proof-2](线性打靶方法-Proof-2.png)

**示意图：**
![示意图](线性打靶方法-示意图.png)

**Example：**
![E1](线性打靶方法-E1.png)
![E2](线性打靶方法-E2.png)

#### 三、Finite-Difference Methods 有限差分方法
**Solution：**
1. 差分为 N+1 个区间（ N+2 个点，其中首位两个是边值条件）
![1](有限分差方法-1.png)
有点类似欧拉方法的思路。
2. y''，y' 近似至 $0(h^2)$  ，考虑**数值微分中的三点公式和高阶微分公式**（见Lecture 6）
![2](有限分差方法-2.png)
3. 得到 N 个线性方程，构造 N $\times$ N 矩阵
![3](有限分差方法-3.png)
![4](有限分差方法-4.png)
注意到：该矩阵为对角严格主导矩阵，故 Aw = b 一定有解。

**提高精度：**
![提高精度](有限分差方法-提高精度.png)
*理查森外推法具有通用性！*

**有限差分方法用于解决非线性问题：**
![1](有限分差方法-非线性问题-1.png)
左边是y''，右边是f，x，y，y'
![2](有限分差方法-非线性问题-2.png)
![3](有限分差方法-非线性问题-3.png)
不一定有解。  
但是当 h < 2/L 时，一定有解。
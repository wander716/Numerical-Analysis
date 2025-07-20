# Numerical Analysis

## Ⅰ：Introduction to Numerical Differetiation 数值微分的介绍
#### 微积分引入：
![微积分引入](Introduction-微积分引入.png)
但是误差会很大
#### 引入拉格朗日插值多项式：
![拉格朗日插值多项式](Introduction-拉格朗日插值多项式引入-1.png)
![alt text](Introduction-拉格朗日插值多项式引入-2.png)
将 x = $x_0$ 代入 f'(x)  =>  
**结论：**
![Theorem](Introduction-Theorem.png)
![Throrem-1](Introduction-Theorem-1.png)
**示意图：**
![示意图](Introduction-Theorem-示意图.png)

## Ⅱ：General Derivative ApproximationFormulas 通用公式

#### 构造：利用拉格朗日插值多项式（L）
![构造-1](通用公式-构造-1.png)
![构造-2](通用公式-构造-2.png)
结果：
![构造结果](通用公式-构造结果.png)

#### 三点公式：即 n = 2
**推导：**
![1](三点公式-1.png)
![2](三点公式-2.png)
![3](三点公式-3.png)
![4](三点公式-4.png)
**结论：**
（2）优于（1）：  
误差是（1）的1/2；运算用到的点少
![结论](三点公式-结论.png)
**示意图：**
![示意图](三点公式-示意图.png)

#### 五点公式：
![五点公式](五点公式-1.png)
下面的公式优于上面的。

#### 高阶微分公式：（以二阶为例）
![1](高阶-1.png)
![2](高阶-2.png)
**结论：**
![3](高阶-3.png)

## Ⅲ：Round-Off Error Instability 数值微分对于舍入误差的不稳定性
#### 引入舍入误差：
![引入-1](舍入误差-引入-1.png)
![引入-2](舍入误差-引入-2.png)

#### 分析：
![分析-1](舍入误差-分析-1.png)
![分析-2](舍入误差-分析-2.png)

## Ⅳ：Richardson's Extrapolation 理查森外推方法
*通过迭代产生更高精度。*
#### 以二阶为例：
![1](理查森外推法-1.png)
![2](理查森外推法-2.png)
![3](理查森外推法-3.png)
$N_2$(h) 比 $N_1$(h) 更精确。
#### 外推至更高阶：
![1](理查森外推法-更高阶-1.png)
![2](理查森外推法-更高阶-2.png)
#### Attention！
阶数越高 -> n 越大 -> h/$2^n$ 越大 -> 舍入误差越大 ！
![Attention](理查森外推法-注意事项.png)
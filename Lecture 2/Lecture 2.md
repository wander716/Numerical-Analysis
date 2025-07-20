# Solutions of Equations in One Variable 单变量方程的求解问题
## Ⅰ: The Root-Finding Problem 寻根问题
![Def of Root-Finding Problem](<Def of Root-Finding Problem.png>)
### The Bisection Method 对分搜索法
![The Bisection Method](<The Bisection Method.png>)  

## Ⅱ: Fixed-Point Iteration 不动点迭代方法
![Proof of Fixed-Point Problem](<Proof of Fixed-Point Problem.png>)
### Fixed-Point Theorem
![Fixed-Point Problem](<Fixed-Point Theorem.png>)
**Corollary:**
![Corollary](<Fixed-Point Problem's Corollary.png>)
*收敛速度完全取决于k，k越小，$k^n$ 越小，$p_n$ 越接近于p，且收敛速度越大。*  

### Example
![Example 1](<Fixed-Point Problem Ex1.png>)


![Example 2](<Fixed-Point Problem Ex2.png>)

## Ⅲ: Newton's Method 牛顿迭代方法
### VS Fixed-Point Problem:
#### Similarity:
是一种特殊的不动点迭代
![Newton's Method & Fixed-Point Problem](<Newton's Method & Fixed-Point Problem.png>)
#### Difference:
收敛速度快得多

<br>

### 牛顿定理的收敛性证明:
![Convergence Theorem for Newton's Method](<Convergence Theorem for Newton's Method.png>)
**Proof:**
*即证：满足Fixed-Point Problem Theorem的两个条件。*
![1](<Newton's Method Proof1.png>)
![2](<Newton's Method Proof2.png>)
![3](<Newton's Method Proof3.png>)
![4](<Newton's Method Proof4.png>)

<br>

## Ⅳ: Error Analisis for Iterative Method 误差与性能分析
![Def of 误差分析](误差分析定义.png)
### 一般的不动点迭代
![4-1](<Proof1 of 一般的不动点迭代收敛速度.png>)

<br>

**特殊情况 之 g'(p) = 0:**
![4-2](<Proof2 of 一般的不动点迭代收敛速度.png>)

### Newton's Method
![4-3](<Proof of Newton's Method 的收敛速度.png>)

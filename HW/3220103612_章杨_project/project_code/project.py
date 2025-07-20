import random
import numpy as np
import scipy
import scipy.sparse as sp
#----------------------------初始化两个矩阵-----------------------------------#
print("problem1:")
print("1:the matrix is ")
A = np.random.rand(10,10) # 生成一个10*10的矩阵，每个元素在-10到10之间
A = (A+A.T)/2#对这个矩阵进行实对称化
print(A)
print("---------------------------------------------------------------------")
print("2:the matrix is(coo格式）")
B = scipy.sparse.random(10000, 10000, density=0.001)#生成一个10000*# 10000的矩阵，密度为0.001
print(B)
print("(2):矩阵中的非0元素共有:",B.nnz)##输出非零个数
print("为方便计算，把B转化为对称阵")
B=(B.todense()+B.todense().T)/2.0#转化为对称阵
B=sp.csc_matrix(B)##转为csc格式
print(B)
#-------------------------------Function-------------------------------------#
def getmaxn(a,n):#获取a序列中绝对值最大的n个值
    abs_a=abs(a)
    sorted_sequence = sorted(abs_a, reverse=True)  # 按降序对序列进行排序
    max_n_values = sorted_sequence[:n]  # 获取排序后的前n个值
    return max_n_values  # 输出最大的n个值
def powermethod(A,eps):#幂法
    m,n=A.shape
    uk=np.ones((n,1))#初始向量
    flag=1#判断条件
    val=0#特征值
    pre_val=0#上一次的特征值
    n=0
    while flag:
        n=n+1
        vk =np.dot(A,uk)#乘上A矩阵
        val = max(abs(x) for x in vk)#最终收敛的时候，最大特征值将会是vk中的最大元素
        uk = vk / val#除掉最大值用于下一次计算
        if (np.abs(val - pre_val) < eps):#判断是否符合条件
            flag = 0
        pre_val = val#把当前计算的特征值赋值给pre_val用于下一次计算
    return val
def Householder(A):
    (m, n) = A.shape
    R = np.copy(A)#R为和A同样的矩阵
    for line in range(n - 1):#line表示现在处理第i列
        l = n - line#(n-1)-line+1,表示要构造的规模是l*l的
        a = np.array(R[line:, line]).reshape(l, 1)#取R矩阵的第line列，其中的数据从第line行开始
        a_norm = np.linalg.norm(a)#计算范数
        e = np.zeros((l, 1))#构造一个l维的向量
        e[0] = 1#把它的第一个元素赋值为1
        w = a - np.dot(a_norm, e)#进行householder变换的工作
        if(np.linalg.norm(w)==0):#检查范数是否为0（为了应对稀疏矩阵的全0列）
            continue
        w = w / np.linalg.norm(w)#正交化
        H_sizeofl = np.identity(l) - 2.0 * np.dot(w, w.T)#计算l*l的矩阵H
        if (line == 0):#如果是第一次
            H = H_sizeofl#直接赋值给H
        else:#如果不是
            H = np.block([#进行一个分块矩阵的操作，左上角为单位阵，其他为0
                [np.identity(line), np.zeros((line, l))],
                [np.zeros((l, line)), H_sizeofl]
            ])#分块矩阵
        # 最后计算Q和R
        if (line == 0):
            Q = H
        else:
            Q = np.dot(Q, H)
        R = np.dot(H, R)
    return Q,R
def QRmethod(A,eps):#QR方法的思路
    n=0
    flag=1
    A_pre=A
    while flag:
        Q,R=Householder(A_pre)#对A_pre进行QR分解
        A_next=np.dot(R,Q)#得到的A矩阵为R*Q
        # print(max(x for x in np.diag(np.abs(A_next - A_pre))))
        if (max(x for x in np.diag(np.abs(A_next-A_pre)))<eps):#判断误差
            flag=0
        A_pre=A_next#用于迭代
        n+=1
    return np.diag(A_next)
def QRmethod_sparse(A,eps):#这里是因为最后写的householder不能很好处理稀疏矩阵，就用库函数的QR分解根据上述流程来了一遍
    n=0
    flag=1
    A_pre=A
    while flag:
        Q,R=np.linalg.qr(A_pre)#对A_pre进行QR分解
        A_next=np.dot(R,Q)#得到的A矩阵为R*Q
        # print(max(x for x in np.diag(np.abs(A_next - A_pre))))
        if (max(x for x in np.diag(np.abs(A_next-A_pre)))<eps):
            flag=0
        A_pre=A_next
        n+=1
    return np.diag(A_next)
def arnoldi(A, k):
    m, n = A.shape#获取规模
    Q = np.zeros((m, k+1))#构造一个m行，k+1列的矩阵，用于存放krylov空间的向量
    H = np.zeros((k+1, k))#构造一个k+1行，k列的矩阵，因为我们只关注前k行k列
    q = np.random.rand(m)#随机初始化一个向量
    q = q / np.linalg.norm(q)#正交化
    Q[:, 0] = q#Q的第一列放置初始向量

    for j in range(k):#进行k次，填充完整个krylov空间
        v = A @ Q[:, j]#v=Aq_m ,得到v为一个m*1的列向量
        #计算q_{m+1}
        for i in range(j+1):
            H[i, j] = np.dot(Q[:, i], v)
            v = v - H[i, j] * Q[:, i]#根据公式
        H[j+1, j] = np.linalg.norm(v)
        if H[j+1, j] == 0:
            break
        Q[:, j+1] = v / H[j+1, j]

    return Q[:, :k], H[:k, :k]#最后取前k行k列
def ERAM_sparse(A,k):#ERAM算法，因为这里只处理稀疏矩阵
    m, n = A.shape#获取规模
    flag=1
    Q,H=arnoldi(A,k)#进行一次aroldi迭代后得到H
    evals_pre,_=scipy.linalg.eig(H)#得到一个差不多的特征值
    while(flag==1):
        # print(evals_pre)
        # print(evals)
        q = np.ones(m)
        for i in range(m):
            t=random.randint(0,k-1)#随机化两个坐标
            s=random.randint(0,k-1)
            q[i] =evals_pre[t]+evals_pre[s]#然后让这个q向量等于随机两个特征值的和
        #接下来的操作同arnoldi算法
        Q = np.zeros((m, k + 1))
        H = np.zeros((k + 1, k))
        q = q / np.linalg.norm(q)
        Q[:, 0] = q
        for j in range(k):
            v = A @ Q[:, j]
            for i in range(j + 1):
                H[i, j] = np.dot(Q[:, i], v)
                v = v - H[i, j] * Q[:, i]
            H[j + 1, j] = np.linalg.norm(v)
            if H[j + 1, j] == 0:
                break
            Q[:, j + 1] = v / H[j + 1, j]
        H=H[:k, :k]#更新H

        evals, evecs = scipy.linalg.eig(H)#更新新的特征值
        maxd = max(x for x in abs(evals - evals_pre))#计算向量差的无穷范数
        # print(maxd)
        if (maxd < 1):#误差给定1
            flag = 0
    return evals

#------------------------------Problem Action--------------------------------#
def problem1():
    print("(3):1矩阵的特征值为")
    evals1, evecs1 = scipy.linalg.eig(A)#用库函数解特征值
    print(evals1)
    print("---------------------------------------------------------------------")
    print("    2矩阵的特征值为")
    evals2, evecs2 = scipy.sparse.linalg.eigs(B)#用库函数解特征值
    print(evals2)
def problem2():
    print("problem2:")
    print("(1):1矩阵中绝对值最大的特征值的绝对值：")
    eps = 1e-5
    val1= powermethod(A, eps)
    print(val1)

    print("---------------------------------------------------------------------")
    print("(2):2矩阵中绝对值最大的特征值的绝对值：")
    val2 = powermethod(B.todense(), eps)
    print(val2)

    print("---------------------------------------------------------------------")
    print("使用problem1中得到的特征值序列得到的最大值(作为检验):")
    evals1, evecs1 = scipy.linalg.eig(A)
    evals2, evecs2 = scipy.sparse.linalg.eigs(B)
    max_abs_value1 = max(abs(x) for x in evals1)
    max_abs_value2 = max(abs(x) for x in evals2)
    print("检验1:",max_abs_value1)
    print("检验2:",max_abs_value2)
def problem3():
    print("Problem3")
    print("(1)第一个矩阵的前4个绝对值最大的特征值为：")
    evals1=QRmethod(A,1e-10)
    print(getmaxn(evals1,4))
    print("---------------------------------------------------------------------")
    m,n=B.todense().shape
    if(n>100):
        print("规模过大，使用QR分解将持续很长时间，故不进行")
    else:
        print("(2)第二个矩阵的前5个绝对值最大的特征值为：")
        C=B.todense()
        evals2 = QRmethod_sparse(C, 1e-3)
        print(getmaxn(evals2,5))
def problem4():
    print("Problem4")

    k=6
    Q,H=arnoldi(A,10)
    evals1, evecs1 = scipy.linalg.eig(H)
    print("(1)第一个矩阵的前6个绝对值最大的特征值为")
    print(getmaxn(evals1,k))
    print("用库函数得到的前6个绝对值最大的特征值为")
    real,realv=np.linalg.eig(A)
    print(getmaxn(real,k))

    print("---------------------------------------------------------------------")
    k =7
    Q, H = arnoldi(B, k)
    evals2, evecs2 = scipy.linalg.eig(H)
    print("(2)第二个矩阵的前7个绝对值最大的特征值为")
    print(getmaxn(evals2, k))
    print("用库函数得到的前7个绝对值最大的特征值为")
    real, realv = scipy.sparse.linalg.eigs(B)
    print(getmaxn(real,k))
def problem5():
    print("Problem5")
    k=8
    print("(1)第二个矩阵的前8个绝对值最大的特征值为")
    evals=ERAM_sparse(B,k)
    print(getmaxn(evals,k))
    print("---------------------------------------------------------------------")
    print("(2)第二个矩阵的前20个绝对值最大的特征值为")
    k=20
    evals = ERAM_sparse(B, k)
    print(getmaxn(evals, k))

def main():
    while(1):
        user_input = input("Which problem do you want to check :")
        if user_input == '1':
            problem1()
        elif user_input == '2':
            problem2()
        elif user_input == '3':
            problem3()
        elif user_input == '4':
            problem4()
        elif user_input == '5':
            problem5()
        elif user_input == 'q':
            print("Thanks.")
            break
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()
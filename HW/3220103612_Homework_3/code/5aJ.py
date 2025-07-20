import numpy as np
import numpy.linalg
import math

x0 = np.array([[0],[0],[0]])
print('x0 = ',x0)
b=np.array([[1],[0],[4]])
D= np.mat([[3,0,0], [0, 6, 0],[0,0,7]])
R= np.mat([[0,1,-1], [-3, 0, -2],[-3,-3,0 ]])
T=np.dot(np.linalg.inv(D),R)
c=np.dot(np.linalg.inv(D),b)


i=1
while(1):
    x =np.dot(T,x0)+c
    print('x%d = \n'%i)
    i=i+1
    print(x)
    if((np.linalg.norm(x-x0,ord=np.Inf)/np.linalg.norm(x,ord=np.Inf))<0.001):
        print("find the solution")
        break
    x0=x

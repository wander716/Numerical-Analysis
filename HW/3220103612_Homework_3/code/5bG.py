import numpy as np
import numpy.linalg
import math

x0 = np.array([[0],[0],[0]])
print('x0 = ',x0)
b=np.array([[9],[7],[6]])
D= np.mat([[10,0,0], [-1, 10, 0],[0,-2,10]])
R= np.mat([[0,1,0], [0, 0, 2],[0,0,0 ]])
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

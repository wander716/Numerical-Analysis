import numpy as np
import numpy.linalg
import math

x = np.array([[0],[0],[0]])
print('x0 = ',x)
b=np.array([[5],[-4],[1]])
D= np.mat([[4,0,0], [0, 3, 0],[0,0,5]])
R= np.mat([[0,-1,1], [1, 0, -1],[-2,-2,0]])
T=np.dot(np.linalg.inv(D),R)
c=np.dot(np.linalg.inv(D),b)
for i in range(1,4):
    x =np.dot(T,x)+c
    print('x%d = \n'%i)
    print(x)
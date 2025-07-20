import numpy as np
import numpy.linalg
import math

x = np.array([[0],[0],[0]])
print('x0 = ',x)
b=np.array([[4],[-4],[0]])
D= np.mat([[-2,0,0], [0, -2, 0],[0,0,2]])
R= np.mat([[0,-1,-0.5], [-1, 0, 0.5],[0,-1,0 ]])
T=np.dot(np.linalg.inv(D),R)
c=np.dot(np.linalg.inv(D),b)

for i in range(1,4):
    x =np.dot(T,x)+c
    print('x%d = \n'%i)
    print(x)
import numpy as np
#print(np.array([0,1,2,3,4,5,6,7,8,9]))
#print(np.arange(3,9,0.5))
#print(np.linspace(0,10,9))
#x, y = np.mgrid[0:4, 0:4]
#print(np.mgrid[1:5, 1:5])
#r = np.random.rand(3,3)
#print(r)
#np.diag([2,3,4], k = -1)
#print(np.zeros((4, 6), dtype = float))
#print(np.ones(7, dtype = int))

m = np.random.rand(3,3)
print(m)
np.savetxt('random-matrix.csv', m)

a = np.arange(0,15,3)
print(a)
a[3:8]

b = np.array([n for n in range(5)])
print(b)
row_mask = np.array([True, False, True, False, False])
b[row_mask]

x = np.arange(0,10,0.5)
print(x)

mask = (5<x)*(x<7.5)
x[mask]

indices =np.where(mask)
print(indices)
x[indices]

v = np.arange(-3,3)
print(v)
row_indices = [1,3,5]
print(v[row_indices])
v.take(row_indices)

a = np.array([[1,2,3],[4,5,6]])
b = a.copy()[:,::-1]
print(a)
b[0,0] = 0
print(b)


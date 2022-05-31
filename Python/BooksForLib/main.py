import numpy as np
fileName = 'books_for_lib.txt'
A = np.genfromtxt(fileName, dtype = None, delimiter = '\', \'', encoding= 'utf-8')
n = A.size
for i in range(int(n/2), int(3/4 * n)):
  if i % 3 == 0:
    print(A[i])
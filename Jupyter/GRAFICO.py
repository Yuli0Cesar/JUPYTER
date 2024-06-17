import numpy as np
import matplotlib.pyplot as plt
import random

def matriz(m):

    for i in range(m):
        vec1 = []
        for j in range(m):
            r = random.randint(0, 999)
            vec1.append(r)
        mat.append(vec1)

m = random.randint(2, 5)
mat = []
matriz(m)

def vector(x,m):
    for i in range(m):
        a = random.randint(0, 999)
        x = np.append(x, a)
    return x

def gauss_seidel(A, B, tol=1e-10, max_iter=100):

    n = len(A)
    X = np.zeros(n)
    for _ in range(max_iter):
        X_new = np.copy(X)
        for i in range(n):
            s1 = sum(A[i][j] * X_new[j] for j in range(i))
            s2 = sum(A[i][j] * X[j] for j in range(i+1, n))
            X_new[i] = (B[i] - s1 - s2) / A[i][i]
        if np.linalg.norm(X_new - X) < tol:
            break
        X = X_new
    return X

x0 = vector(np.array([]), m)

X = gauss_seidel(mat, x0)

fig, ax = plt.subplots()
ax.plot(X)

ax.set_title('Gráfica 2D')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')

print(mat)
print(x0)
print(X)
plt.show()
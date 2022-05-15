import numpy as np
import matplotlib.pyplot as plt

n, m = map(int, input("n, m: ").split())    # input in rows and columns
iterations = int(input("Number of iterations: "))
print("Rows of Coefficient Matrix:")
array = np.array([input().strip().split() for _ in range(n)], int)
print("Answers to equations: ")
b = np.array([input().strip().split() for _ in range(n)], int)
print("Initial Guess: ")
x = np.array([input().strip().split() for _ in range(n)], int)
D = np.diag(np.diag(array))
L = np.tril(array)-D
U = np.triu(array)-D
invDL = np.linalg.inv(D+L)
G = -(invDL @ U)
H = invDL @ b
residue =[]
iter = []
for i in range(iterations):
    x = G @ x + H
    r = array@x -b
    residue.append(np.linalg.norm(r, ord="fro"))
    iter.append(i+1)
plt.style.use('fivethirtyeight')
plt.plot(iter, residue)
plt.show()
print(x)
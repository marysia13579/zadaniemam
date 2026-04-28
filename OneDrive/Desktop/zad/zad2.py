import numpy as np

def relax(A, b, omega=1.25, dokl=1e-6, max_iter=1000):
    n = len(b) 
    x = np.zeros(n) 

    for k in range(max_iter):
        x_old = x.copy() 

        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i]) 
            sum2 = np.dot(A[i, i+1:], x_old[i+1:]) 
            x[i] = (1 - omega) * x_old[i] + (omega / A[i, i]) * (b[i] - sum1 - sum2)
        if np.linalg.norm(x - x_old, ord=np.inf) < dokl:
            print(f"Zbieżność po {k} iteracjach")
            return x

    print("Nie osiągnięto zbieżności")
    return x

A = np.array([
    [12, 3, 22, 10, 2, 0],
    [6, 11, -1, 3, 0, 0],
    [2, -1, 10, -1, 0, 0],
    [0, 3, -1, 2, -1, 0],
    [4, 0, 0, -1, 5, 2],
    [0, 3, 0, 0, 2, 4]
], dtype=float)

b = np.array([6, 25, -11, 15, 10, 10], dtype=float) 
x = relax(A, b, omega=1.25)

print("Rozwiązanie:", x)
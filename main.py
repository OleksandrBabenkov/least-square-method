import math
import matplotlib.pyplot as plt

# P(x) = a0 + a1*x + a2*x^2 + ... + ak*x^k

def solve_system(L, y):
    
    n = len(y)

    x = [[0] for _ in range(n)]

    for i in range(n):

        suma = 0

        for j in range(i):

            suma += L[i][j] * x[j]

        x[i] = (y[i] - suma) / L[i][i]

    return x

#L = [[2, 0, 0], [-3, 1, 0], [4, 2, 3]]
#y = [2, -4, 11]

#print(solve_system(L, y))


def solve_transpondent_system(L_T, x):

    n = len(x)

    a = [[0] * n for _ in range(n)]

    for i in range(n-1, -1, -1):

        suma = 0

        for j in range(i + 1, n):

            suma += L_T[i][j] * a[j]

        a[i] = (x[i] - suma) / L_T[i][i]

    return a

#L_T = [[2, -3, 4], [0, 1, 2], [0, 0, 3]]
#x = [1, -1, 3]

#print(solve_transpondent_system(L_T, x))

def Cholesky_decomposition(A):

    n = len(A)

    L = [[0] * n for _ in range(n)]
    L_T = [[0] * n for _ in range(n)]
   
    for i in range(n):

        for j in range(i+1):
        
            suma = 0
            
            if j == i:
                
                for k in range(j):

                    suma += math.pow(L[j][k], 2)

                L[j][j] = math.sqrt(A[j][j] - suma)
    
            else:

                for k in range(j):
                    
                    suma += L[j][k] * L[i][k]

                L[i][j] = ( A[i][j] - suma ) / L[j][j]

   
    for i in range(n):
        for j in range(n):

            L_T[i][j] = L[j][i]
  
    return L,L_T

def get_coefficients(X, Y, n):
    #pass

    A = []
    y = []

    m = len(X)

    if (len(Y) != m):
        print("Rozmiary danych wejsciowych sie nie zgdzaja")
        return

    for k in range(n):

        temp = []
        suma_y = 0

        for i in range(n):
            
            suma = 0
           
            for j in range(m):
                
                suma += math.pow(X[j], i) * math.pow(X[j], k)
            
            temp.append(suma)
         
        for i in range(m):
            suma_y += Y[i] * math.pow(X[i], k)

        A.append(temp)
        y.append(suma_y)

    #return A, y
    
    L, L_T = Cholesky_decomposition(A)

    a_temp = solve_system(L, y)

    a = solve_transpondent_system(L_T, a_temp)

    return a

'''
X_2 = [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]
Y_2 = [-9, -4.5, -2.2, -0.8, 0.1, 0.6, 1.2, 4.3, 8.5]

X_t = [-1, 0, 1, 2]
Y_t = [4, -1, 0, 7]
n = 5

'''
def polynomial(a_local, x):
    ans = 0
    for i in range(len(a_local)):
        ans += a_local[i] * math.pow(x, i)
    return ans    

def MNK(X, Y, n):

    a = get_coefficients(X, Y, n)
    print(f"wspojczynniki wielomianu: {a}")
    X_curve = [i / 100 for i in range(min(X) * 100, max(X) * 100)]
    
    Y_fit = [polynomial(a, x) for x in X_curve]

    plt.figure()
    plt.scatter(X, Y, color='blue', label='data points')

    plt.plot(X_curve, Y_fit, color='red', label=f'polynomial degree {n}')

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Least Squares Method")
    plt.legend()



# dane przykladowe

X = [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]
Y = [-9, -4.5, -2.2, -0.8, 0.1, 0.6, 1.2, 4.3, 8.5]

n = 4
MNK(X, Y, n)

plt.show()

# -*- coding: utf-8 -*-
"""Felipe_Avila_Silva_Relatorio2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aHqDrD40-Z6KkRYNxLmnmassY2WAnaVl

DEF
"""

import numpy as np
import math

def printf(X):
  for i in range(len(X)):
    print(X[i])



def sempivo(A, b):
  for k in range (n-1):
    for i in range (k+1, n):
      if A[i, k] == 0:continue
      factor = A[k,k]/A[i,k]
      for j in range (k,n):
        A[i,j] = A[k,j] - A[i,j]*factor
      b[i] = b[k] - b[i]*factor
  print(A)
  print(b)

  x[n-1] = b [n-1] / A[n-1,n-1]
  for i in range (n-2,-1,-1):
    sum_ax=0
    for j in range (i+1, n):
      sum_ax += A[i,j]*x[j]
    x[i] = (b[i] - sum_ax)/ A[i,i]

  return x



def gaussPivo(A, b):
  for i in range(len(A)):
    pivo = math.fabs(A[i][i])
    linhaPivo = i
    for j in range(i+1, len(A)):
      if math.fabs(A[j][i]) > pivo:
        pivo = math.fabs(A[j][i])
        linhaPivo = j
    if linhaPivo != i:
      linhaAux = A[i]
      A[i] = A[linhaPivo]
      A[linhaPivo] = linhaAux

      bAux = b[i]
      b[i] = b[linhaPivo]
      b[linhaPivo] = bAux
    for m in range(i+1, len(A)):
      multi = A[m][i]/A[i][i]
      for n in range(i,len(A)):
        A[m][n] = A[m][n] - multi * A[i][n]
      b[m] = b[m] - multi * b[i]
  print("matriz triangular superior")    
  for k in range(len(A)):
    print(A[k])
  print()
  print("novo vet b")
  print(b)
  print()



def retroativa(A, b):
  vet = []
  for i in range(len(A)):
    vet.append(0)
  linha = len(A) - 1
  while linha >= 0:
    x = b[linha]
    coluna = len(A) - 1
    while coluna > linha:
      x = x - A[linha][coluna]* vet[coluna]
      coluna = coluna - 1
    x = x / A[linha][linha]
    linha = linha - 1
    vet[coluna] = x
  print("valores de X's") 
  for j in range(len(vet)):
    print("x"+str(j+1)+"="+str(format(vet[j], '.4f')))
  



def LU(A, L, b):

  for i in range(len(A)):
    pivo = A[i][i]
    linhaPivo = i

    for m in range(i+1, len(A)):
      multi = A[m][i]/A[i][i]
      L[m][i] = multi

      for n in range(i,len(A)):
        A[m][n] = A[m][n] - multi * A[i][n]

  return A, L



def cholesky(a):
  a = np. array(a, float)
  L = np.zeros_like(a)
  n,_ = np.shape(a)
  for j in range(n):
    for i in range(j, n):
      if i == j:
        sumk = 0
        for k in range(j):
          sumk += L[i][k] ** 2
        L[i][j] = np.sqrt(a[i][j]-sumk)
      else:
        sumk = 0
        for k in range(j):
          sumk += L[i][k]* L[j][k]
        L[i][j] = (a[i][j]-sumk) / L[j][j]
  return L



def gaussSeidel (A, b, vet, n):
  iteracao=0
  while iteracao<n:
    for i in range(len(A)):
      x=b[i]
      for j in range(len(A)):
        if i!=j:
          x-=A[i][j]*vet[j]
      x/=A[i][i]
      vet[i]=x
    iteracao += 1

  return vet



def gaussJacob (A, b, vet, n):
  iteracao = 0
  vetorAuxiliar=[]
  for k in range(len(vet)):
    vetorAuxiliar.append(0)

  while iteracao < n:
    for i in range(len(A)):
      x=b[i]
      for j in range(len(A)):
        if i != j:
          x-=A[i][j]*vet[j]
      x/=A[i][i]
      vetorAuxiliar[i]=x
    iteracao += 1
    
    for p in range(len(vetorAuxiliar)):
      vet[p]=vetorAuxiliar[p]
  
  return vet

"""1.A) Pivotamento Parcial"""

A = [[1, -3, 5, 6],
    [-9, 4, -1, 0],
    [3, 2, -2, 7],
    [1, 2, 5, -4]]

b = [17, 29, -11, 7]

gaussPivo(A, b) 
retroativa(A, b)

"""Sem Pivotamento"""

from numpy import array, zeros
A = array ([[1, -3, 5, 6],
    [-9, 4, -1, 0],
    [3, 2, -2, 7],
    [1, 2, 5, -4]], float)
b = array ([17, 29, -11, 7], float)
n = len(b)
x = zeros(n, float)

x = sempivo(A, b)

print("valores de X's")
printf(x)

"""B) Pivotamento Parcial"""

A = [[-2, 3, 1, 5],
    [5, 1, -1, 0],
    [1, 6, 3, -1],
    [4, 5, 2, 8]]

b = [2, -1, 0, 6]

gaussPivo(A, b)
retroativa(A, b)

"""Sem Pivotamento"""

from numpy import array, zeros
A = array ([[-2, 3, 1, 5],
    [5, 1, -1, 0],
    [1, 6, 3, -1],
    [4, 5, 2, 8]], float)
b = array ([2, -1, 0, 6], float)
n = len(b)
x = zeros(n, float)

x = sempivo(A, b)

print("valores de X's")
printf(x)

"""2. A)"""

import numpy as np

A = [[-1, 2, -2],
     [3, -4, 1],
     [1, -5, 3]]

b = [6, -11, -10]

L = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]


y = [0, 0, 0]
x = [0, 0, 0]

U, L = LU(A, L, b)

print("L:")
printf(L)
print("U:")
printf(U)

y[0] = b[0]
y[1] = (b[1] - L[1][0] * y[0]) / L[1][1]
y[2] = b[2] - L[2][0] * y[0] - L[2][1] * y[1]

print("y:", y)

x[2] = y[2] / U[2][2]
x[1] = (y[1] - U[1][2] * x[2]) / U[1][1]
x[0] = (y[0] - U[0][1] * x[1] - U[0][2] * x[2]) / U[0][0]

print("Valor de x's:")
for i in range(len(x)):
  print(str(format(x[i], '.4f')))

"""B)"""

import numpy as np

A = [[-1, 2, -2],
     [3, 4, 1],
     [-4, -5, 3]]

b = [-1, -4, 20]

L = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]
  

y = [0, 0, 0]
x = [0, 0, 0]

U, L = LU(A, L, b)

print("L:")
printf(L)
print("U:")
printf(U)

y[0] = b[0]
y[1] = (b[1] - L[1][0] * y[0]) / L[1][1]
y[2] = b[2] - L[2][0] * y[0] - L[2][1] * y[1]

print("y:", y)

x[2] = y[2] / U[2][2]
x[1] = (y[1] - U[1][2] * x[2]) / U[1][1]
x[0] = (y[0] - U[0][1] * x[1] - U[0][2] * x[2]) / U[0][0]

print("Valor de x's:")
for i in range(len(x)):
  print(str(format(x[i], '.4f')))

"""3. A)"""

G = [[20, 7, 9],
    [7, 30, 8],
    [9, 8, 30]]

GT = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

b = [16, 38, 38]

x = [0, 0 , 0]
y = [0, 0 , 0]

G = cholesky(G)
print("G:")
printf(G)
det = (G[0][0]*G[1][1]*G[2][2])**2
print("det:", det)

y[0] = b[0]/G[0][0]
y[1] = (b[1] - G[1][0] * y[0]) / G[1][1] 
y[2] = (b[2] - G[2][1] * y[1]) / G[2][2] 
print("y:", y)

GT = np.transpose(G)
print("GT:")
printf(GT)

x[2] = y[2] / GT[2][2]
x[1] = (y[1] - GT[1][2] * x[2]) / GT[1][1]
x[0] = (y[0] - GT[0][1] * x[1] - GT[0][2] * x[2]) / GT[0][0]

print("Valor de x's:")
for i in range(len(x)):
  print(str(format(x[i], '.4f')))

"""B)"""

G = [[8, 20, 16],
    [20, 80, 50],
    [16, 50, 60]]

GT = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

b = [100, 250, 100]

x = [0, 0 , 0]
y = [0, 0 , 0]

G = cholesky(G)
print("G:")
printf(G)
det = (G[0][0]*G[1][1]*G[2][2])**2
print("det:", det)

y[0] = b[0]/G[0][0]
y[1] = (b[1] - G[1][0] * y[0]) / G[1][1] 
y[2] = (b[2] - (G[2][1] * y[1])) / G[2][2] 
print("y:", y)

GT = np.transpose(G)

x[2] = y[2] / GT[2][2]
x[1] = (y[1] - GT[1][2] * x[2]) / GT[1][1]
x[0] = (y[0] - GT[0][1] * x[1] - GT[0][2] * x[2]) / GT[0][0]

print("Valor de x's:")
for i in range(len(x)):
  print(str(format(x[i], '.4f')))

"""4.A)

GAUSS-SEIDEL
"""

A = [[3, 0.1, -0.2],
     [0.1, 7, -0.3],
     [0.3, -0.2, 10]]

b = [7.85, -19.3, 71.4]

vet = [0, 0, 0]
n = 10

vet = gaussSeidel(A, b, vet, n)
print("Valor de x's")
printf(vet)

"""GAUSS-JACOBI"""

A = [[3, 0.1, -0.2],
     [0.1, 7, -0.3],
     [0.3, -0.2, 10]]

b = [7.85, -19.3, 71.4]

vet = [0, 0, 0]
n = 10

vet = gaussJacob(A, b, vet, n)
print("Valor de x's")
printf(vet)

"""B)

GAUSS-SEIDEL
"""

A = [[10, 2, 1],
     [1, 5, 1],
     [2, 3, 10]]

b = [7, -8, 6]

vet = [0.7, -1.6, 0.6]
n = 10

vet = gaussSeidel(A, b, vet, n)
print("Valor de x's")
printf(vet)

"""GAUSS-JACOBI"""

A = [[10, 2, 1],
     [1, 5, 1],
     [2, 3, 10]]

b = [7, -8, 6]

vet = [0.7, -1.6, 0.6]
n = 10

vet = gaussJacob(A, b, vet, n)
print("Valor de x's")
printf(vet)
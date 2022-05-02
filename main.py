import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


# x = [0, 1, 2, 3, 4, 5]
# y = [2.1, 7.7, 13.6, 27.2, 40.9, 61.1]
x = [1, 3, 5, 7, 13]
y = [800, 2310, 3090, 3940, 4755]
m = 1
n = len(x)
if n < m+1:
    print("Aproksymacja niemożliwa, za mało elementów")
    exit(1)
x = np.array(x)
y = np.array(y)
x_sum = []
for i in range(2*m+1):
    x_sum.append(np.sum(x**i))
y_sum = []
for i in range(m+1):
    y_sum.append(np.sum(y*(x**i)))
a_matrix = [[]]
for i in range(m+1):
    if len(a_matrix) != m+1:
        a_matrix.append([])
    for j in range(m+1):
        a_matrix[i].append(x_sum[j+i])
a_matrix = np.array(a_matrix)
b = np.array(y_sum)
a_param = np.linalg.solve(a_matrix, b)
eq = 'y='
for i in range(m+1):
    eq += str(a_param[i])
    if i != 0:
        if i == 1:
            eq += 'x'
        else:
            eq += 'x^' + str(i)
    if i != m:
        eq += ' + '
print(eq)
x_new = np.linspace(np.amin(x), np.amax(x), 300)  # Dla gładkiego wykresu
y_reg = []
y_elem = 0
for i in range(x_new.size):
    for j in range(m+1):
        y_elem += a_param[j] * x_new[i]**j
    y_reg.append(y_elem)
    y_elem = 0
# Obliczanie błędów i współczynników
y_mean = (y-y.mean())**2
print("(y_i - y_mean)^2 :", y_mean)
err_square_val = 0
err_square_val_sum = []
for i in range(x.size):
    for j in range(m+1):
        err_square_val += a_param[j] * x[i]**j
    err_square_val_sum.append((y[i] - err_square_val)**2)
    err_square_val = 0
print("Błąd standardowy: ", sqrt(np.sum(err_square_val_sum)/(n-(m+1))))
r2 = (np.sum(y_mean)-np.sum(err_square_val_sum))/np.sum(y_mean)
print("R^2: ", r2)
print("R: ", sqrt(r2))
fig = plt.figure(figsize=(6, 6))
plt.plot(x, y, 'y.')
plt.plot(x_new, y_reg, 'r-')
plt.legend(["Funkcja Aproksymowana", "Funkcja aproksymująca"])
plt.xlabel('t(s)')
plt.ylabel('v, cm/s')
# plt.title('Aproksymacja wielomianowa')
plt.show()

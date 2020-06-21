# -*- coding: utf-8 -*-
# Найти max и min и поменять их местами.

import numpy as np #импорт библиотеки numpy.

#y = np.random.randint(100,size = (5,5))

#.savetxt(fname = 'dataset.csv',X = y) 
#print(y)
x = np.loadtxt(fname = 'dataset.csv') # Загрузка данных из файла.
print(x) # Вывод исходной матрицы.

maxim = np.max(x) # Находим максимум.
print(maxim)
minim = np.min(x) # Находим минимум.
print(minim)

indmax = np.where(x == maxim) # Ищем индексы максимальных элементов.
print(indmax)

indmin = np.where(x == minim) # Ищем индексы минимальных элементов.
print(indmin)

# Заменяем все максимумы на минимумы.
for i in range(len(indmax[0])):
    x[indmax[0][i]][indmax[1][i]] = minim
    
# Заменяем все минимумы на максимумы.
for i in range(len(indmin[0])):
    x[indmin[0][i]][indmin[1][i]] = maxim    

# Выводим получившуюся матрицу.
print(x)
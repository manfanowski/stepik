#Вычесление площади треугольника
a = int(input())
b = int(input())
c = int(input())
p = (a+b+c) / 2
from math import sqrt
print (sqrt(p*(p-a)*(p-b)*(p-c)))
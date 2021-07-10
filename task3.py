# Заполните 2 списка а и b случайными целыми числами и верните 3 список общих для а и b элементов
import random

a = []
b = []
for i in range(20):
    a.append(random.randint(1,100))
    b.append(random.randint(1,100))
result = list(set(a) & set(b))
print(a, b, result)
# Задача 2. Требуется найти в массиве A[1..N] самый близкий по величине 
# элемент к заданному числу X. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai. Последняя строка содержит число X.

n = int(input('Введите количество элементов массива: '))
num_list = []

for i in range(n):
    num = int(input('Введите элементы массива: '))
    num_list.append(num)

x = int(input('Введите число X: '))
b=[abs(num_list[i]-x) for i in range(len(num_list))]
print(num_list[b.index(min(b))])

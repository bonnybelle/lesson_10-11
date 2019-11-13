from random import randint

lst = [randint(1, 200) for i in range(20)]
print(lst)
a = int(input('Введите a: '))
b = int(input('Введите b: '))
lst1 = lst[a-1:b][::-1]
lst = lst1 in range(a-1, b)
print(lst)

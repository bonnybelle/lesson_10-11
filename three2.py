from random import randint

lst = [randint(1, 200) for i in range(15)]
print(lst)
a = int(input('Введите a: '))
b = int(input('Введите b: '))-2
for i in range(a-1, int((a-1+b)+1/2)//2):
    lst[i], lst[b-(i-a+1)] = lst[b-(i-a+1)], lst[i]
print(lst)

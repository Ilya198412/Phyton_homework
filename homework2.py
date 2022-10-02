# 1. **Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.Пример:
# 6782 -> 23
# - 0,56 -> 11

num = float(input('Введите вещественное число :'))
num=abs(num) 
count=0
#if num <0:
    #num=-num
while int(num) !=num: 
    num*=10           
    print(num)

while num!=0:         # пока нум неравен 0 
    count+= num%10    # отсекаем последнюю цифру и прибавляем ее в переменную count
    num//=10          # делим убираем прибавленную цифру и по новой прогоняем цикл
    print(count)      # пока не отсечем все цифры
    
print ((f' Сумма цифр введенного числа : {count}'))




# 2. **Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N**.*Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input('Введите число N:'))
res=[]
count=1
for i in range(1, num+1):
    res.append(i*count)
    count*=i
print (f'Факториал чисел от 1 до {num}:\n  {res}')

# 3. **Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму**.

num = int(input('Введите число N:'))
def SumDigit (n):
    res=[]
    for i in range(1, num+1):
        res.append((1+1/i)**i)  
    return res
print (f'Сумма чисел последовательности числа {num} равна {sum(SumDigit(num))},\nчисла полученные по формуле  (1+1/n)^n N =  {SumDigit(num)}')

# 4. **Реализуйте алгоритм перемешивания списка**.

import random
# number = int (input ('Размер списка : '))
listA=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list_mix=[]
# def Shuffle:
for i in range(0, len(listA)):
    j= random.randrange(0,len(listA))
    list_mix.append(listA[j])
    # listA.remove(listA[j])

print(f'Изначальный список -  {listA} \nПеремешанный список - {list_mix}')

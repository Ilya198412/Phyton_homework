# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> [] 


from ast import Num
from random import randint as rL

num = "".join(list(map(str,[rL(0,9) for i in range(10)])))

count=1
num_list=[]

for i in range(len(num)):
    num_list.append(int(num[i:i+count]))  
 
new_list=[]
for i in num_list:
    if num_list.count(i)==1:
        new_list.append(i)
    
print(f'Список в котором ищем уникальные знаяения - {num_list}')
print(f'Уникальные значения находящиеся в списке {new_list}') 


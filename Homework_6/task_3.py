# # 3. **Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму**.

# num = int(input('Введите число N:'))
# def SumDigit (n):
#     res=[]
#     for i in range(1, num+1):
#         res.append((1+1/i)**i)  
#     return res
# print (f'Сумма чисел последовательности числа {num} равна {sum(SumDigit(num))},\nчисла полученные по формуле  (1+1/n)^n N =  {SumDigit(num)}')

num = int(input('Введите число N:'))
res = list(range (1, num +1))
print(list(map(lambda x: (1+1/x)**x,res)))
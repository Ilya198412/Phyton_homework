import random
# функция создания списка с рандомными значениями
# list= []
# def fillArray(list):
#     list.clear() # очищает список, если нужно вывести новый список, в противном случае он будет добавлять в уже созданный список еще элементы 
#     for i in range(10):
#         list.append(random.randint(-10,10))
#     return list 

# fillArray(list)
# print(list)

## функция по созданию перевернутого списка
# def fillArray():
#     list= []
#     list.clear() # очищает список, если нужно вывести новый список, в противном случае он будет добавлять в уже созданный список еще элементы 
#     for i in range(10):
#         list.append(random.randint(-10,10))
#     return list 

# novaya = fillArray()
# print(novaya)
# novaya.reverse() # для вывода перевернутого массива
# print(novaya)


# функция по созданию списка коэффициентов

from random import randint as rL


def createEquation():
    
    degree = int(input('Введите максимальную степень многочлена : '))

    equation= ''

    for d in range(degree,-1,-1):
        coef =rL(-20,20)
        if d==degree:
            if coef >0:
                equation+=' + ' + str(coef) +'x^' +str(d)
            if coef <0:
                equation+=' - ' + str(abs(coef)) +'x^' +str(d)

    else:
        if coef >0:
            equation+=' + ' + str(coef) +'x^' +str(d)
        if coef <0:
            equation+=' - ' + str(abs(coef)) +'x^' +str(d)

    return equation + '=0'

eq1= createEquation()
print((eq1.replace('x^1', 'x').replace('x^0','')).replace('1x^','x^'))
eq2= createEquation()
print((eq2.replace('x^1', 'x').replace('x^0','')).replace('1x^','x^'))
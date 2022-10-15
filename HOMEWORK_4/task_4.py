# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от-100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

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
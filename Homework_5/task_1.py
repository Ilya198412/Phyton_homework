# *1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".**


abvStr = 'абв арпв абв вавыро ыфвыфавабввыарыво ыфыцгс выа фбв абв'
print(f'Список для проверки: {abvStr}'  )
elem = input("Введите искомый элемент: ")
listAbv=[]
abvStr=abvStr.split()
for i in abvStr:
    if elem not in i:
        listAbv.append(i)
        
print(f'Список элементов после проверки и удаления - {elem} - = {listAbv}')


# txt = input("Введите текст через пробел:\n")
# print(f"Исходный текст: {txt}")
# find_txt = "абв"
# lst = [i for i in txt.split() if find_txt not in i]
# print(f'Результат: {" ".join(lst)}')
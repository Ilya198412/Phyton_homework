# **1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".**


# abvStr = 'абв арпв абв вавыро ыфвыфавабввыарыво ыфыцгс выа фбв абв'
# print(f'Список для проверки: {abvStr}'  )
# elem = input("Введите искомый элемент: ")
# listAbv=[]
# abvStr=abvStr.split()
# for i in abvStr:
#     if elem not in i:
#         listAbv.append(i)
        
# print(f'Список элементов после проверки и удаления - {elem} - = {listAbv}')


# функция  filter

abvStr = 'абв арпв абв вавыро ыфвыфавабввыарыво ыфыцгс выа фбв абв'
print(f'список для проверки [{abvStr}]')

abvStr=abvStr.split()
text=input(f'Введите данные для поиска - ')
filt_abvStr= list(filter(lambda x: text not in x, abvStr))

print(f'Список элементов после проверки и удаления "{text}" = {filt_abvStr}')
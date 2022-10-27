# **4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.**
# *Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc*

pathRead = r'E:\Илья\обучение\PYTHON\Python_homework\Homework_5\text3.txt'
pathWrite = r'text4.txt'

try:
    with open (pathRead) as data:
        file = data.read().split(' ')
except:
    print('ошибка файла')

print(file)
file=str(file)

zipDig = f'{file.count("a")}a{file.count("b")}b{file.count("c")}c'

print(zipDig)
unZip = ''
zip = ''
for i in zipDig:
    if i.isdigit():
        zip += i
    else:
        unZip += str(int(zip) * i)
        zip = ''
print(unZip)
try:
    with open (pathWrite, 'w') as data:
        data.write(str((unZip)))
        data.write('\n')
        data.write(str((zipDig)))
except:
    print("Ошибка работы с файлом")


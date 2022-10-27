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


# txt = input("Введите текст через пробел:\n")
# print(f"Исходный текст: {txt}")
# find_txt = "абв"
# lst = [i for i in txt.split() if find_txt not in i]
# print(f'Результат: {" ".join(lst)}')

# **2. Создайте программу для игры с конфетами человек против человека.**

# *Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?*a) Добавьте игру против ботаb) Подумайте как наделить бота 'интеллектом'


# print('Игра начинается, ознакомьтесь с правилами : На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.')
# print('Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.') 


# candy = 150



# def take_move(player_token):
#     valid = False
#     while not valid:
#         player_answer=(input('Ваш ход: ' + player_token + "?"))

#         try:
#             player_answer = int(player_answer)
#         except:
#             print('Некорректный ввод. Ввведите число от 1 до 28')
#             continue
#         if player_answer>=1 and player_answer<=28:
#             candy-=player_answer
#             if candy>player_answer:
#                 valid = True
#             else:
#                 print(f"на столе осталось {candy} конфет")
#         else:
#             print("Введите число от 1 до 28")

#         return candy
# #  def check_win(candy):
# #     lose_comb=1
# #     if candy == 1:
# #         print('{player_token} Ты проиграл')
    
# #     return False


# def main():
#     ''' основная функция'''
#     counter = 0
    

#     win = False
#     while not win:
        
#         if counter %2 ==0:
#             take_move('Ход Первого игрока')
#             counter +=1
#         else:
#             take_move('Ход Второго игрока')
#             counter +=1

#         if candy == 1:
#             print("Ты выиграл")
    
#         # break

        
    
# main()


# **3. Создайте программу для игры в 'Крестики-нолики'.**


from turtle import ontimer


x = 'X'
y = 'O'
board = list(range(1,10))
# for i in range(1,10):
#     position.append(i)

# winComb=



def draw_board(board):
    ''' функция по рисованию доски для игры '''
    print ('-' *13)
    for i in range(3):
        print ('|',board[0+i*3],'|',board[1+i*3],'|',board[2+i*3], '|' )
        print('-'*13)


def take_move(player_token):
    valid = False
    while not valid:
        player_answer=(input('Ваш ход: ' + player_token + "?"))

        try:
            player_answer = int(player_answer)
        except:
            print('Некорректный ввод. Ввведите число')
            continue
        if player_answer>=1 and player_answer<=9:
            if (str(board[player_answer-1]) not in 'XO'):
                board[player_answer-1] = player_token
                valid = True
            else:
                print("Клетка занята")
        else:
            print("Введите число от 1 до 9")

def check_win(board):
    win_comb=((0,1,2), (3,4,5), (0,3,6), (6,7,8), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

    for each in win_comb:
        if board[each[0]]==board[each[1]]==board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter %2 ==0:
            take_move('X')
        else:
            take_move('O')
        counter +=1

        if counter > 4:
            tmp=check_win(board)
            if tmp:
                print(tmp,"Ты выиграл")
                win = True
                break

        if counter ==9:
            print("Ничья")
            break
    draw_board(board)
main(board)


draw_board(board)




    # print (f'{position[0]:^5}|{position[1]:^5}|{position[2]:^5}|')
    # print('------------------')
    # print (f'{position[3]:^5}|{position[4]:^5}|{position[5]:^5}|')
    # print('------------------')
    # print (f'{position[6]:^5}|{position[7]:^5}|{position[8]:^5}|')

    # index=int(input(f'\n\nХод {"игрока" if sign == "x" else "противника"} '))
    # position [index - 1] = sign




# **4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.**
# *Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc*

# pathRead = r'text3.txt'
# pathWrite = r'text4.txt'

# try:
#     with open (pathRead) as data:
#         file = data.read().split(' ')
# except:
#     print('ошибка файла')

# print(file)
# file=str(file)

# zipDig = f'{file.count("a")}a{file.count("b")}b{file.count("c")}c'

# print(zipDig)
# unZip = ''
# zip = ''
# for i in zipDig:
#     if i.isdigit():
#         zip += i
#     else:
#         unZip += str(int(zip) * i)
#         zip = ''
# print(unZip)
# try:
#     with open (pathWrite, 'w') as data:
#         data.write(str((unZip)))
#         data.write('\n')
#         data.write(str((zipDig)))
# except:
#     print("Ошибка работы с файлом")


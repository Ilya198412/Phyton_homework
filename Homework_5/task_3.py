# **3. Создайте программу для игры в 'Крестики-нолики'.**


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


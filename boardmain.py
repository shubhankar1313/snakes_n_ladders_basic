import random, re
from colorama import init, Fore, Style
init(convert = True)

def element_is_normal(element):
    if '(' in element:
        return False
    else:
        return True

def coordinate_of_element(element):
    row = (100 - int(element))//10
    return row, check_board[row].index(str(element))
    
# def checkSL(value):
#     # NEED TO WORK
#     global board, check_board
#     # 4 - (100-4)//10 = 9, 4%10-1. 87 - (100-87)//10 = 1, 87%10 - 1 = 6.
#     index = index_of_element(value)
#     if '(' in board[row][index]:
#         print(row, index)
#         sub_index = board[row][index].index('(')
#         print(sub_index)

def dice_roll(choice):
    global value, prev_value

    prev_value = pointers[choice]
    value = dice()
    pointers[choice] += value
    main()
    # print(pointer1, value)

def dice():
    return random.randint(1, 6)
    # return 4

def print_board(board):
    print('-' * 82)
    for row in board:
        print('|' + '|'.join(row) + '|')
        print('-' * 82)

def board_func(change = None):
    global board

    board = [['  100   ', '99 ' + Fore.BLUE + '(L8)' + Fore.WHITE, '  98   ', '97 ' + Fore.MAGENTA + '(S1)' + Fore.WHITE, '  96   ', '95 ' + Fore.MAGENTA + '(S2)' + Fore.WHITE, '  94   ', '  93   ', '92 ' + Fore.BLUE + '(L7)' + Fore.WHITE, '  91   '],
             ['   81   ', '  82   ', '  83   ', '  84   ', '  85   ', '  86   ', '  87   ', '88 ' + Fore.MAGENTA + '(S3)' + Fore.WHITE, '  89   ', '  90   '],
             [' 80 ' + Fore.BLUE + '(L8)' + Fore.WHITE, '  79   ', '78 ' + Fore.MAGENTA + '(S1)' + Fore.WHITE, '  77   ', '76 ' + Fore.BLUE + '(L5)' + Fore.WHITE, '  75   ', '  74   ', '  73   ', '  72   ', '71 ' + Fore.BLUE + '(L7)' + Fore.WHITE],
             ['   61   ', '62 ' + Fore.MAGENTA + '(S4)' + Fore.WHITE, '  63   ', '  64   ', '  65   ', '  66   ', '67 ' + Fore.BLUE + '(L6)' + Fore.WHITE, '  68   ', '  69   ', '  70   '],
             ['   60   ', '  59   ', '  58   ', '  57   ', '56 ' + Fore.MAGENTA + '(S2)' + Fore.WHITE, '  55   ', '  54   ', '  53   ', '  52   ', '  51   '],
             ['   41   ', '42 ' + Fore.BLUE + '(L4)' + Fore.WHITE, '  43   ', '  44   ', '  45   ', '  46   ', '  47   ', '48 ' + Fore.MAGENTA + '(S5)' + Fore.WHITE, '  49   ', '50 ' + Fore.BLUE + '(L6)' + Fore.WHITE],
             ['   40   ', '  39   ', '38 ' + Fore.BLUE + '(L1)' + Fore.WHITE, '  37   ', '36 ' + Fore.MAGENTA + '(S6)' + Fore.WHITE, '  35   ', '  34   ', '  33   ', '32 ' + Fore.MAGENTA + '(S7)' + Fore.WHITE, '  31   '],
             [' 21 ' + Fore.BLUE + '(L4)' + Fore.WHITE, '  22   ', '  23   ', '24 ' + Fore.MAGENTA + '(S3)' + Fore.WHITE, '  25   ', '26 ' + Fore.MAGENTA + '(S5)' + Fore.WHITE, '  27   ', '28 ' + Fore.BLUE + '(L5)' + Fore.WHITE, '  29   ', '30 ' + Fore.BLUE + '(L3)' + Fore.WHITE],
             ['   20   ', '  19   ', '18 ' + Fore.MAGENTA + '(S4)' + Fore.WHITE, '  17   ', '  16   ', '  15   ', '14 ' + Fore.BLUE + '(L2)' + Fore.WHITE, '  13   ', '  12   ', '  11   '],
             ['  1 ' + Fore.BLUE + '(L1)' + Fore.WHITE, '   2   ', '   3   ', ' 4 ' + Fore.BLUE + '(L2)' + Fore.WHITE, '   5   ', ' 6 ' + Fore.MAGENTA + '(S6)' + Fore.WHITE, '   7   ', ' 8 ' + Fore.BLUE + '(L3)' + Fore.WHITE, '   9   ', '10 ' + Fore.MAGENTA + '(S7)' + Fore.WHITE]]
    
    if change != None and change[1] != 0:
        # prev = coordinate_of_element(change[1])
        curr = coordinate_of_element(change[0])
        curr_element = board[curr[0]][curr[1]]
        if element_is_normal(curr_element):
            curr_element += '*'
            board[coordinate_of_element(change[1])[0]][coordinate_of_element(change[1])[1]] = curr_element
    
    print_board(board)
    
def main():
    global pointers, value, prev_value, turn, controls
    
    if value != 0:
        board_func([pointers[turn - 1], prev_value]) # with var
        print('\n' + f"Player {turn} rolled {value}!")
        # print(pointers[turn - 1], prev_value) # testing
        if turn == 1:
            turn = 2
        else:
            turn = 1
        value = 0
    else:
        board_func()

    print('\n' + Fore.RED + "Player 1" + Fore.WHITE + f" Pos: {pointers[0]}\n" + Fore.GREEN + "Player 2" + Fore.WHITE + f" Pos: {pointers[1]}")
    
    choice = input(f"\nPlayer {turn} Press {controls[turn]} to Roll the Dice: ")
    
    if choice.lower() == 's':
        dice_roll(0)
    elif choice.lower() == 'n':
        dice_roll(1)
    else:
        pass
        # Error handling

if __name__ == "__main__":
    pointers, value, prev_value, turn, controls = [0, 0], 0, 0, 1, {1 : 'S', 2 : 'N'}

    check_board = [['100', '99', '98', '97', '96', '95', '94', '93', '92', '91'],
         ['81', '82', '83', '84', '85', '86', '87', '88', '89', '90'],
         ['80', '79', '78', '77', '76', '75', '74', '73', '72', '71'],
         ['61', '62', '63', '64', '65', '66', '67', '68', '69', '70'],
         ['60', '59', '58', '57', '56', '55', '54', '53', '52', '51'],
         ['41', '42', '43', '44', '45', '46', '47', '48', '49', '50'],
         ['40', '39', '38', '37', '36', '35', '34', '33', '32', '31'],
         ['21', '22', '23', '24', '25', '26', '27', '28', '29', '30'],
         ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11'],
         ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']]
    main()
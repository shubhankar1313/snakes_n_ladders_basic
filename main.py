import random, re
from colorama import init, Fore, Style
init(convert = True)

def checkSL(value):
    global board, check_board
    # 4 - (100-4)//10 = 9, 4%10-1. 87 - (100-87)//10 = 1, 87%10 - 1 = 6.
    row = (100 - value)//10
    index = check_board[row].index(str(value))
    if '(' in board[row][index]:
        print(row, index)
        sub_index = board[row][index].index('(')
        print(sub_index)

def dice_roll(choice):
    global pointer1, pointer2, board

    value = dice()
    if choice == 's':
        pointer1 += value
        checkSL(pointer1)
    else:
        pointer2 += value

    # print(pointer1, value)

def dice():
    # return random.randint(1, 6)
    return 4

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
    
    print_board(board)
    
def main():
    global pointer1, pointer2, turn, button
    
    board_func()
    
    print('\n' + Fore.RED + "Player 1" + Fore.WHITE + f" Pos: {pointer1}\n" + Fore.GREEN + "Player 2" + Fore.WHITE + f" Pos: {pointer2}")
    
    choice = input(f"\nPlayer {turn} Press {button} to Roll the Dice: ")
    
    dice_roll(choice.lower())

if __name__ == "__main__":
    pointer1, pointer2, turn, button = 0, 0, 1, 'S'
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

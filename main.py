from colorama import init, Fore, Style
init(convert = True)

def print_board(board):
    print('-' * 82)
    for row in board:
        print('|' + '|'.join(row) + '|')
        print('-' * 82)

def board(change = None):
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
    global pointer1, pointer2, turn
    
    board()
    
    print('\n' + Fore.RED + "Player 1" + Fore.WHITE + f" Pos: {pointer1}\n" + Fore.GREEN + "Player 2" + Fore.WHITE + f" Pos: {pointer2}")
    
    choice = input(f"\nPlayer {turn} Press {button} to Roll the Dice: ")
    
if __name__ == "__main__":
    pointer1, pointer2, turn, button = 0, 0, 1, 'S'
    main()

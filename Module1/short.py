import random
from colorama import Fore, Style, init

init(autoreset=True)

board = ['1','2','3','4','5','6','7','8','9']

def show():
    print()
    print(Fore.CYAN + board[0], "|", board[1], "|", board[2])
    print(Fore.YELLOW + "--+---+--")
    print(Fore.CYAN + board[3], "|", board[4], "|", board[5])
    print(Fore.YELLOW + "--+---+--")
    print(Fore.CYAN + board[6], "|", board[7], "|", board[8])
    print()

def win(s):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]

    for a,b,c in wins:
        if board[a] == board[b] == board[c] == s:
            return True
    return False

print(Fore.MAGENTA + "🎮 TIC TAC TOE 🎮")

player = input(Fore.GREEN + "Choose X or O: ").upper()
ai = 'O' if player == 'X' else 'X'

while True:
    show()

    move = int(input(Fore.BLUE + "Enter position (1-9): "))

    if board[move-1] in ['X','O']:
        print(Fore.RED + "Already Taken!")
        continue

    board[move-1] = player

    if win(player):
        show()
        print(Fore.GREEN + "🎉 You Win!")
        break

    if all(i in ['X','O'] for i in board):
        show()
        print(Fore.YELLOW + "🤝 Match Draw!")
        break

    while True:
        ai_move = random.randint(0,8)

        if board[ai_move] not in ['X','O']:
            board[ai_move] = ai
            break

    if win(ai):
        show()
        print(Fore.RED + "😈 AI Wins!")
        break
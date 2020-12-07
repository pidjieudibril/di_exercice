
def display_board():
    blankBoard = ("""
            *******************
            |     |     |     |
            |  {}  |  {}  |  {}  |
            |     |     |     |
            |*****************|
            |     |     |     |
            |  {}  |  {}  |  {}  |
            |     |     |     |
            |*****************|
            |     |     |     |
            |  {}  |  {}  |  {}  |
            |     |     |     |
            |*****************|
        """).format(board[0][0],board[0][1],board[0][2],board[1][0],board[1][1],board[1][2],board[2][0],board[2][1],board[2][2])
    print(blankBoard)


board=[
    ["1","2","3"],
    ["4","5","6"],
    ["7","8","9"]
    ]



def player_input(player):

    case=input("dand quel case veux tu jouer?")
    for i in board:
        try:
            n_case=i.index(case)
            i[n_case]=player
        except:
            continue

    display_board()

def play():
        player1 = input("svp entrer une valeur entre  'X' ou 'O' ")
        turn=0
        while turn<9:
            turn += 1
            if turn %2!=0 and player1.upper() == 'X':
                player2 = 'O'
                print("tu as choisie " + player1 + ".le jouer 2 sera " + player2)
                player_input(player1.upper())
                player_input(player2)
            elif turn %2 !=0 and player1.upper() == 'O':
                 player2 = 'X'
                 print("tu as choisie " + player1 + ". tu as choisie " + player2)
                 player_input(player1.upper())
                 player_input(player2)
            else:
                 player1 = input("svp entrer une valeur entre  'X' ou 'O' ")

play()







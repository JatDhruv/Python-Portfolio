# random module needed to make the computer moves
import random

# the player token by default
playerToken = "X"
# the empty tic-tac-toe table
defaultBoard = [
    ["( )", "( )", "( )"],
    ["( )", "( )", "( )"],
    ["( )", "( )", "( )"]
]


def exampleGrid():
    return "(0,0)|(0,1)|(0,2)\n-----|-----|-----\n(1,0)|(1,1)|(1,2)\n-----|-----|-----\n(2,0)|(2,1)|(2,2)"


def playerInput():
    placeholder = False
    # this boolean is used to loop the following while loop, and it won't be called outside the function
    global playerToken
    # this global variable is used as giving the ability to call it outside the function gives more flexibility
    playerToken = input("Welcome to TicTacToe!\nChoose your symbol:\nInput X or O\n")
    while not placeholder:
        if playerToken == "X":
            print("Chosen Token: X")
            playerToken = "X"
            return "X"
        elif playerToken == "x":
            print("Chosen Token: x")
            playerToken = "X"
            return "X"
        elif playerToken == "O":
            print("Chosen Token: O")
            playerToken = "O"
            return "O"
        elif playerToken == "o":
            print("Chosen Token: O")
            playerToken = "O"
            return "O"
        else:
            playerToken = input("Try Again!\nInput X or O\n")


def OccupiedX(x, y):
    if defaultBoard[x][y] != "(X)" and "(O)":
        defaultBoard[x][y] = "(X)"
        return True
    else:
        return False


def OccupiedY(x, y):
    if defaultBoard[x][y] != "(X)" and "(O)":
        defaultBoard[x][y] = "(O)"
        return True
    else:
        return False


def HumanMove():
    c = False
    while not c:
        if playerToken == "X":
            print("X Turn")
            print("Input the coordinates of your move:\n", exampleGrid(), "\n", sep="")
            try:
                x = int(input("X coordinates: "))
                c = True
            except ValueError:
                print("Wrong! Input a number coordinate:\nExample: \n", exampleGrid(), sep="")
            try:
                y = int(input("Y coordinates: "))
            except ValueError:
                print("Wrong! Input a number coordinate:\nExample: \n", exampleGrid(), sep="")
                c = False
            try:
                c = OccupiedX(x, y)
                if not c:
                    print("Try again")
            except:
                print("Try again")
                c = False
        else:
            print("O Turn")
            print("Input the coordinates of your move:\n", exampleGrid(), "\n", sep="")
            try:
                x = int(input("X coordinates: "))
                c = True
            except ValueError:
                print("Wrong! Input a number coordinate:\nExample: \n", exampleGrid(), sep="")
            try:
                y = int(input("Y coordinates: "))
            except ValueError:
                print("Wrong! Input a number coordinate:\nExample: \n", exampleGrid(), sep="")
                c = False
            try:
                c = OccupiedY(x, y)
                if not c:
                    print("Try again")
            except:
                print("Try again")
                c = False
    for a in defaultBoard:
        print(a)


def ComputerMove():
    c = False

    while not c:
        x = int(random.random() * 3)
        y = int(random.random() * 3)
        if playerToken == "O":
            # for now the computer moves will be just printed to the screen 8 would be top right square and 0 would be
            # bottom left
            if defaultBoard[x][y] != "(X)" and "(O)":
                print("Computer Moves: (", x, ",", y, ")", sep="")
                defaultBoard[x][y] = "(X)"
                for z in defaultBoard:
                    print(z)
                break
        else:
            # for now the computer moves will be just printed to the screen 8 would be top right square and 0 would be
            # bottom left
            if defaultBoard[x][y] != "(X)" and "(O)":
                print("Computer Moves: (", x, ",", y, ")", sep="")
                defaultBoard[x][y] = "(O)"
                for z in defaultBoard:
                    print(z)
                break


def GameWin():
    # X player
    if defaultBoard[0][0] == "(X)" and defaultBoard[0][1] == "(X)" and defaultBoard[0][2] == "(X)":
        print("Player X Wins!")
        return True
    elif defaultBoard[1][0] == "(X)" and defaultBoard[1][1] == "(X)" and defaultBoard[1][2] == "(X)":
        print("Player X Wins!")
        return True
    elif defaultBoard[2][0] == "(X)" and defaultBoard[2][1] == "(X)" and defaultBoard[2][2] == "(X)":
        print("Player X Wins!")
        return True
    elif defaultBoard[0][0] == "(X)" and defaultBoard[1][1] == "(X)" and defaultBoard[2][2] == "(X)":
        print("Player X Wins!")
        return True
    elif defaultBoard[0][1] == "(X)" and defaultBoard[1][1] == "(X)" and defaultBoard[2][1] == "(X)":
        print("Player X Wins!")
        return True
    elif defaultBoard[2][0] == "(X)" and defaultBoard[1][1] == "(X)" and defaultBoard[0][2] == "(X)":
        print("Player X Wins!")
        return True
    elif defaultBoard[0][0] == "(X)" and defaultBoard[1][0] == "(X)" and defaultBoard[2][0] == "(X)":
        print("Player X Wins!")
        return True
    elif defaultBoard[0][2] == "(X)" and defaultBoard[1][2] == "(X)" and defaultBoard[2][2] == "(X)":
        print("Player X Wins!")
        return True
    # O Player
    elif defaultBoard[0][0] == "(O)" and defaultBoard[0][1] == "(O)" and defaultBoard[0][2] == "(O)":
        print("Player O Wins!")
        return True
    elif defaultBoard[1][0] == "(O)" and defaultBoard[1][1] == "(O)" and defaultBoard[1][2] == "(O)":
        print("Player O Wins!")
        return True
    elif defaultBoard[2][0] == "(O)" and defaultBoard[2][1] == "(O)" and defaultBoard[2][2] == "(O)":
        print("Player O Wins!")
        return True
    elif defaultBoard[0][0] == "(O)" and defaultBoard[1][1] == "(O)" and defaultBoard[2][2] == "(O)":
        print("Player O Wins!")
        return True
    elif defaultBoard[0][1] == "(O)" and defaultBoard[1][1] == "(O)" and defaultBoard[2][1] == "(O)":
        print("Player O Wins!")
        return True
    elif defaultBoard[2][0] == "(O)" and defaultBoard[1][1] == "(O)" and defaultBoard[0][2] == "(O)":
        print("Player O Wins!")
        return True
    elif defaultBoard[0][0] == "(O)" and defaultBoard[1][0] == "(O)" and defaultBoard[2][0] == "(O)":
        print("Player O Wins!")
        return True
    elif defaultBoard[0][2] == "(O)" and defaultBoard[1][2] == "(O)" and defaultBoard[2][2] == "(O)":
        print("Player O Wins!")
        return True
    else:
        return False


q = 0
finished = False
playerInput()
while not finished:
    HumanMove()
    finished = GameWin()
    if finished:
        break
    ComputerMove()
    finished = GameWin()
    if finished:
        break
    q += 1
    if q > 4:
        finished = True
        print("Draw!")

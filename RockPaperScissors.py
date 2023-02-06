import random
player = 0
computer = 0


def GameNumber():
    global games
    c = False
    while not c:
        try:
            games = int(input("Pick a number of games to play before deciding a winner:\n"))
            c = True
        except ValueError:
            print("Cannot be a letter, decimal, or word! Try Again!")
        except:
            print("Wrong, Try Again!")
    print("Best out of:", games, "is this number correct?")
    global confirm
    confirm = input("Yes or No:\n")


def HumanMove():
    c = False
    global hMove
    humanMove = input("Make your move:\n")
    while not c:
        if humanMove == "rock" or humanMove == "Rock" or humanMove == "r" or humanMove == "R":
            print("ROCK!", end=" ")
            hMove = "Rock"
            c = True
        elif humanMove == "paper" or humanMove == "Paper" or humanMove == "p" or humanMove == "P":
            print("PAPER!", end=" ")
            hMove = "Paper"
            c = True
        elif humanMove == "scissors" or humanMove == "Scissors" or humanMove == "scissor" or humanMove == "Scissor" or humanMove == "s" or humanMove == "S":
            print("SCISSORS!", end=" ")
            hMove = "Scissors"
            c = True
        else:
            humanMove = input("Try Again, Rock Paper or Scissors:\n")


def ComputerMove():
    global cMove
    x = int((random.random())*3)+1
    if x == 1:
        cMove = "Rock"
    elif x == 2:
        cMove = "Paper"
    else:
        cMove = "Scissors"
    print("Computer moved:", cMove)


def Winner():
    global player
    global computer
    if cMove == hMove:
        print("Draw!")
    elif cMove == "Rock" and hMove == "Paper":
        print("You Win!")
        player += 1
    elif cMove == "Rock" and hMove == "Scissors":
        print("You Lose!")
        computer += 1
    elif cMove == "Paper" and hMove == "Rock":
        print("You Lose!")
        computer += 1
    elif cMove == "Paper" and hMove == "Scissors":
        print("You Win!")
        player += 1
    elif cMove == "Scissors" and hMove == "Rock":
        print("You Win!")
        player += 1
    elif cMove == "Scissors" and hMove == "Paper":
        print("You Lose!")
        computer += 1


print("Welcome to Rock Paper Scissors!")
GameNumber()
c = False
while not c:
    if confirm == "yes" or confirm == "Yes" or confirm == "y" or confirm == "Y":
        for i in range(games):
            print("Round :", i+1)
            HumanMove()
            ComputerMove()
            Winner()
            print("Score:\nPlayer -", player, "Computer -", computer, end="\n\n")
        c = True
    elif confirm == "no" or confirm == "No" or confirm == "n" or confirm == "N":
        GameNumber()
    else:
        confirm = input("Try Again, Yes or No:\n")





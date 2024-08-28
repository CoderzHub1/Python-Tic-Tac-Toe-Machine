print("This is the Tic Tac Toe Unbeatable machine")
boardArr = [1,2,3,4,5,6,7,8,9]
# Winning Conditions: [1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]
# Board Design and Printing initial Board
board= f"{boardArr[1-1]} | {boardArr[2-1]} | {boardArr[3-1]} \n ----------- \n {boardArr[4-1]} | {boardArr[5-1]} | {boardArr[6-1]} \n ----------- \n {boardArr[7-1]} | {boardArr[8-1]} | {boardArr[9-1]} "
print(f"The starting board:\n {board}\n\nYou play as O\n Let's Start:")

#Function to change a boardArr item
def cba(en, to):
    boardArr[to-1] = en
    return f"Successfully changed element no {en} to {to}"

# Funtion to check for win
def winCheck():
    winner = ""
    if boardArr[0:3]==["O","O","O"] or boardArr[0:3]==["X","X","X"]:
        if boardArr[0:3]==["O","O","O"]:
            winner = "O"
        else:
            winner = "X"
    
    elif boardArr[3:6]==["O","O","O"] or boardArr[3:6]==["X","X","X"]:
        if boardArr[3:6]==["O","O","O"]:
            winner = "O"
        else:
            winner = "X"
    
    elif boardArr[6:9]==["O","O","O"] or boardArr[6:9]==["X","X","X"]:
        if boardArr[6:9]==["O","O","O"]:
            winner = "O"
        else:
            winner = "X"

    elif boardArr[0:7:3]==["O","O","O"] or boardArr[0:8:3]==["X","X","X"]:
        if boardArr[0:7:3]==["O","O","O"]:
            winner = "O"
        else:
            winner = "X"

    elif boardArr[1:8:3]==["O","O","O"] or boardArr[1:8:3]==["X","X","X"]:
        if boardArr[1:8:3]==["O","O","O"]:
            winner = "O"
        else:
            winner = "X"

    elif boardArr[2:9:3]==["O","O","O"] or boardArr[2:9:3]==["X","X","X"]:
        if boardArr[2:9:3]==["O","O","O"]:
            winner = "O"
        else:
            winner = "X"

    elif boardArr[0:9:4]==["O","O","O"] or boardArr[0:9:4]==["X","X","X"]:
        if boardArr[0:9:4]==["O","O","O"]:
            winner = "O"
        else:
            winner = "X"
    
    elif boardArr[2:7:2]==["O","O","O"] or boardArr[2:7:2]==["X","X","X"]:
        if boardArr[2:7:2]==["O","O","O"]:
            winner = "O"
        else:
            winner = "X"

    else:
        winner=None
    return winner

while winCheck()==None:
    userInput = input(f"Board Situation:\n {f"{boardArr[1-1]} | {boardArr[2-1]} | {boardArr[3-1]} \n ----------- \n {boardArr[4-1]} | {boardArr[5-1]} | {boardArr[6-1]} \n ----------- \n {boardArr[7-1]} | {boardArr[8-1]} | {boardArr[9-1]} "}\n Enter your move (make sure you enter an integer): ")
    cba("O", int(userInput))
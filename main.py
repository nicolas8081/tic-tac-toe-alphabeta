
# figure out what the evaluation function and depth should 
# implement the alphabeta pruning 

def printBoard(myList: list):
    alphabetString = "ABCDEFGH"

    print("  1 2 3 4 5 6 7 8")
    for row in range(len(myList)):
        print(alphabetString[row], end=" ")
        for column in range(len(myList[row])):
            print(myList[row][column], end=" ")
        print()

def inputBoardValidation(move : str, list2d : list):
    if len(move) > 2:
        print("Invalid")
    row = move[0].upper()
    column = int(move[1]) - 1
    match row:
        case "A":
            row = 0
        case "B":
            row = 1
        case "C":
            row = 2
        case "D":
            row = 3
        case "E":
            row = 4
        case "F":
            row = 5
        case "G":
            row = 6
        case "H":
            row = 7
        case 404:
            return "Not Found"
        case _:
            return "Unknown Status"
    list2d[row][column] = "X"
    return (row,column)
    
def checkForWinner(move, row, column, list2d) -> int:
    left, right = column - 1, column + 1
    up, down = row - 1, row + 1
    totalLeftRight = 0
    totalUpDown = 0

    if move == "X":
        while left >= 0:
            if list2d[row][left] == "X":
                totalLeftRight += 1
                left -= 1
            else:
                break

        while right < len(list2d[row]):
            if list2d[row][right] == "X":
                totalLeftRight += 1
                right += 1
            else:
                break

        while up >= 0:
            if list2d[up][column] == "X":
                totalUpDown += 1
                up -= 1
            else:
                break

        while down < len(list2d):
            if list2d[down][column] == "X":
                totalUpDown += 1
                down += 1
            else:
                break

        if totalLeftRight + 1 >= 4 or totalUpDown + 1 >= 4:
            print(5000)
            return 5000  # User has won

    print(0)
    return 0  # No winner found by this check
    
def getaMove(list2d):
    gameCheckerFlag = True
    while gameCheckerFlag:
        move = input("Enter your move: ")
        row, column = inputBoardValidation(move, list2d)
        outcome = checkForWinner("X", row, column, list2d)
        print(outcome)
        printBoard(list2d)

def playGame():
    rows, columns = 8 , 8
    list2d = [["-" for _ in range(rows)] for _ in range(columns)]
    printBoard(list2d)
    getaMove(list2d)

def main():
    playGame()

main()
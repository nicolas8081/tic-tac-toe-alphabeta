def printBoard(myList: list):
    alphabetString = "ABCDEFGH"

    print("  1 2 3 4 5 6 7 8")
    for row in range(len(myList)):
        print(alphabetString[row], end=" ")
        for column in range(len(myList[row])):
            print(myList[row][column], end=" ")
        print()

def inputBoardValidation(value : str):
    if len(str) > 2:
        print("Invalid")
    letter = value[0]
    number = int(value[1])
    match letter:
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
    

def main():
    rows = 8
    columns = 8
    list2d = [['$']*columns]*rows
    printBoard(list2d)

main()

def printBoard(myList: list):
    alphabetString = "ABCDEFGH"

    print("  1 2 3 4 5 6 7 8")

    for i in range(len(myList)):
        if i % 8 == 0:
            print(alphabetString[i // 8], end=" ")

        print(myList[i], end=" ")

        if (i + 1) % 8 == 0:
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
    myList = ['$'] * 64
    printBoard(myList)
main()
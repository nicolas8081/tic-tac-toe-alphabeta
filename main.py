
def printBoard():
    alphabetString = "ABCDEFGH"
    print("   1  2  3  4  5  6  7  8")
    for i in range(8):
        print(alphabetString[i], end= " ")
        for i in range(8):
            print(" _ ", end= "")
        print("\n")

def main():
    printBoard()
main()
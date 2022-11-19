row = int(input('Enter number of row: '))
val = int(input('Enter number of diamond: '))

def dm(row,val):
    for l in range(val):
        for i in range(1, row + 1):
            for j in range(1, row - i + 1):
                print(" ", end="")
            for j in range(1, 2 * i):
                print("*", end="")
            print()

        for i in range(row - 1, 0, -1):
            for j in range(1, row - i + 1):
                print(" ", end="")
            for j in range(1, 2 * i):
                print("*", end="")
            print()
dm(row,val)
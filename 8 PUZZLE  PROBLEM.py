def print_puzzle(rows, cols):
    count = 1
    print("\nPuzzle Layout:")
    for i in range(rows):
        for j in range(cols):
            print(count, end="\t")
            count += 1
        print()
def main():
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        if rows <= 0 or cols <= 0:
            print("Rows and columns must be positive integers.")
            return
        print_puzzle(rows, cols)
    except ValueError:
        print("Invalid input. Please enter integers.")
main()


rows = int(input(f"Enter the # of rows: "))
columns = int(input(f"Enter the # of columns: "))
symbol = input(f"Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()


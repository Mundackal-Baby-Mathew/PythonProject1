#nested loops = The "inner loop" will finish all of its iterations before
#finishing one iteration of the "outer loop"

rows = int(input("How many number of rows: "))
columns = int(input("How many number of columns: "))
symbols = input("Enter your symbol to display: ")

for i in range (rows):
    for j in range(columns):
        print(symbols,end="")
    print()

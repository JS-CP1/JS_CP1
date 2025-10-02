#JS, 1st, Multiplication Table
def get_printable(num):
    if len(str(num)) == 1:
        printable = f"  {num} |"
    elif len(str(num)) == 2:
        printable = f"{num} |"
    elif len(str(num)) == 3:
        printable = f"{num}|"
    else:
        printable = f"{num}|"
    return printable
row = 1
column = 1
table = []
sizes = int(input("How big do you want the table.\n ").strip())
for size in range(sizes):
    for size in range(sizes):
        product = row * column
        product = get_printable(product)
        if size == sizes - 1:
            table.append(product + "\n")
        table.append(product)
        column += 1
    row += 1
    column = 0
print(*table)
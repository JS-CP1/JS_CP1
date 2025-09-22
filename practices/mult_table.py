# JS, 1st, Multiplication Table
while True:
    size = str(input("What number would you like the multiplication table to go up to?\n").strip())
    while len(size) > 2:
        size = str(input("That is too many numbers, try again.\n"))
    size = int(size)
    table = [[" |  x |"]]
    column = "1"
    int_column = 1
    row = "0"
    int_row = 0
    for _ in range(size):
        if len(column) == 1:
            table[0].append(" " + column + " |")
        elif len(column) == 2:
            table[0].append(column + " |")
        else:
            table[0].append(column + "|")
        int_column += 1
        column = str(int_column).strip()
    int_row += 1
    row = str(int_row).strip()
    while int_row <= size:
        for _ in range(size + 1):
            int_column = 0
            column = str(int_column).strip()
            if len(row) == 1:
                table.append([f" |  {row.strip()} |"])
            else:
                table.append([f" | {row.strip()} |"])
            int_column += 1
            column = str(int_column).strip()
            for _ in range(size):
                result = str(int_row * int_column)
                int_row = int(row)
                if len(result) == 1:
                    table[int_row].append(f" {result.strip()} |")
                elif len(result) == 2:
                    table[int_row].append(f"{result.strip()} |")
                else:
                    table[int_row].append(f"{result.strip()}|")
                int_column += 1
                column = str(int_column).strip()
            int_row += 1
            row = str(int_row).strip()
    for i in range(size + 1):
        print(*table[i])
    again = input("Would you like to do another?\n").strip().lower()
    if again != "yes": break
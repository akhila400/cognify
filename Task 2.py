def print_number_pattern(rows, pattern_type):
    if pattern_type == 'pyramid':
        for i in range(1, rows + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    elif pattern_type == 'triangle':
        for i in range(1, rows + 1):
            print(" " * (rows - i), end="")
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    elif pattern_type == 'diamond':
        for i in range(1, rows + 1):
            print(" " * (rows - i), end="")
            for j in range(1, i + 1):
                print(j, end=" ")
            print()
        for i in range(rows - 1, 0, -1):
            print(" " * (rows - i), end="")
            for j in range(1, i + 1):
                print(j, end=" ")
            print()
    elif pattern_type == 'squre':
       for i in range(size):
        for j in range(size):
          print(i * size + j + 1, end=" ")
        print()
    else:
        print("Invalid pattern type. Please choose 'pyramid', 'triangle','diamond' or 'Squre'.")


rows = int(input("Enter the number of rows: "))
pattern_type = input("Enter the pattern type ('pyramid', 'triangle','diamond','Squre'): ")


print_number_pattern(rows, pattern_type)
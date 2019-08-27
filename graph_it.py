import sys
_ = input("How many rows of boxes (e.g., 3)? ")
rows = int(_)
_ = input("How many columns of boxes (e.g., 4)? ")
columns = int(_)
_ = input("How many rows of spaces in each box (e.g., 1)? ")
row_space = int(_)
_ = input("How many columns of spaces in each box (e.g., 3)? ")
col_space = int(_)
int(col_space)

for r in range(rows):
    for rs  in range(row_space+1):
        if rs == 0:
            for c in range(columns):
                print("+", end = "")
                for cs in range(col_space):
                    print("-", end = "")
                    cs += 1
            c += 1
            print("+")
        else:
            for c in range(columns):
                print("|", end = "")
                for cs in range(col_space):
                    print(" ", end = "")
                    cs += 1
            c += 1
            print("|")
        rs += 1
    r += 1

# Last line
for c in range(columns):
    print("+", end = "")
    for cs in range(col_space):
        print("-", end = "")
        cs += 1
    c += 1
print("+")

sys.exit(0)

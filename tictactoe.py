# write your code here
matrix = input("Enter cell: ")
print("---------")
print(f"| {matrix[0]} {matrix[1]} {matrix[2]} |")
print(f"| {matrix[3]} {matrix[4]} {matrix[5]} |")
print(f"| {matrix[6]} {matrix[7]} {matrix[8]} |")
print("---------")

row_1 = (matrix[0], matrix[1], matrix[2])
row_2 = (matrix[3], matrix[4], matrix[5])
row_3 = (matrix[6], matrix[7], matrix[8])
col_1 = (matrix[0], matrix[3], matrix[6])
col_2 = (matrix[1], matrix[4], matrix[7])
col_3 = (matrix[2], matrix[5], matrix[8])
diag_1 = (matrix[0], matrix[4], matrix[8])
diag_2 = (matrix[6], matrix[4], matrix[2])

def win_test(threes):
    if "".join(threes) == "XXX":
        return "X"
    elif "".join(threes) == "OOO":
        return "O"
    elif "_" in "".join(threes):
        return "_"

x_wins = []
o_wins = []
open_cell = []

if win_test(row_1) == "X":
    x_wins.append("X")
elif win_test(row_1) == "O":
    o_wins.append("O")
elif win_test(row_1) == "_":
    open_cell.append("_")

if win_test(row_2) == "X":
    x_wins.append("X")
elif win_test(row_2) == "O":
    o_wins.append("O")
elif win_test(row_2) == "_":
    open_cell.append("_")

if win_test(row_3) == "X":
    x_wins.append("X")
elif win_test(row_3) == "O":
    o_wins.append("O")
elif win_test(row_3) == "_":
    open_cell.append("_")

if win_test(col_1) == "X":
    x_wins.append("X")
elif win_test(col_1) == "O":
    o_wins.append("O")
elif win_test(col_1) == "_":
    open_cell.append("_")

if win_test(col_2) == "X":
    x_wins.append("X")
elif win_test(col_2) == "O":
    o_wins.append("O")
elif win_test(col_2) == "_":
    open_cell.append("_")

if win_test(col_3) == "X":
    x_wins.append("X")
elif win_test(col_3) == "O":
    o_wins.append("O")
elif win_test(col_3) == "_":
    open_cell.append("_")

if win_test(diag_1) == "X":
    x_wins.append("X")
elif win_test(diag_1) == "O":
    o_wins.append("O")
elif win_test(diag_1) == "_":
    open_cell.append("_")

if win_test(diag_2) == "X":
    x_wins.append("X")
elif win_test(diag_2) == "O":
    o_wins.append("O")
elif win_test(diag_2) == "_":
    open_cell.append("_")

#print(len(x_wins))
#print(len(o_wins))
#print(open_cell)

if len(x_wins) > 0 and len(o_wins) > 0 and len(open_cell) >= 0:
    print("Impossible")
elif matrix.count("X") > matrix.count("O") + 1:
    print("Impossible")
elif matrix.count("O") > matrix.count("X") + 1:
    print("Impossible")
elif len(x_wins) == 0 and len(o_wins) == 0 and len(open_cell) == 0:
    print("Draw")
elif len(x_wins) == 0 and len(o_wins) == 0 and len(open_cell) > 0:
    print("Game not finished")
elif len(x_wins) == 1 and len(o_wins) == 0 and len(open_cell) >= 0:
    print("X wins")
elif len(x_wins) == 0 and len(o_wins) == 1 and len(open_cell) >= 0:
    print("O wins")

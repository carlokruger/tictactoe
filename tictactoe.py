# write your code here
rows = list()
columns = []
diags = []
game_board = []
x_winner = ["X", "X", "X"]
o_winner = ["O", "O", "O"]
x_wins = 0
o_wins = 0
x_s = 0
o_s = 0
spaces = 0
row_1 = []
row_2 = []
row_3 = []
init_matrix = ""
current_state = ""
current_player = "X"

num_matrix = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]


def create_init_state():

    global init_matrix
    global row_1
    global row_2
    global row_3

    init_matrix = input("Enter cells: ")
    row_1 = [init_matrix[0], init_matrix[1], init_matrix[2]]
    row_2 = [init_matrix[3], init_matrix[4], init_matrix[5]]
    row_3 = [init_matrix[6], init_matrix[7], init_matrix[8]]


def create_rows():
    global row_1
    global row_2
    global row_3
    global rows
    rows.append(row_1)
    rows.append(row_2)
    rows.append(row_3)


def print_gameboard():
    global rows

    print("---------")
    print(f"| {rows[0][0]} {rows[0][1]} {rows[0][2]} |")
    print(f"| {rows[1][0]} {rows[1][1]} {rows[1][2]} |")
    print(f"| {rows[2][0]} {rows[2][1]} {rows[2][2]} |")
    print("---------")


def create_columns():
    global rows
    global columns
    columns = [
        [rows[0][0], rows[1][0], rows[2][0]],
        [rows[0][1], rows[1][1], rows[2][1]],
        [rows[0][2], rows[1][2], rows[2][2]]
    ]


def create_diags():
    global rows
    global diags
    diags = [[rows[0][0], rows[1][1], rows[2][2]],
             [rows[2][0], rows[1][1], rows[0][2]]]


def create_gameboard():
    global game_board
    global rows
    global columns
    global diags
    game_board = [rows] + [columns] + [diags]


def count_winners():
    global game_board
    global x_winner
    global o_winner
    global x_wins
    global o_wins
    global spaces
    global x_s
    global o_s

    x_wins = game_board.count(x_winner)
    o_wins = game_board.count(o_winner)
    spaces = game_board.count("_")
    x_s = game_board.count("X")
    o_s = game_board.count("O")


def check_game_state():
    global x_wins
    global o_wins
    global spaces
    global x_s
    global o_s
    global current_state

    if x_wins == 1 and o_wins == 0:
        current_state = "X wins"

    elif o_wins == 1 and x_wins == 0:
        current_state = "O wins"

    elif spaces > 0 and o_wins == 0 and x_wins == 0:
        current_state = "Game not finished"

    elif x_wins > 0 and o_wins > 0:
        current_state = "Impossible"

    elif (x_s > o_s + 1) or (o_s > x_s + 1):
        current_state = "Impossible"

    elif x_wins == 0 and o_wins == 0 and spaces == 0:
        current_state = "Draw"

    return current_state

def is_two_digits(some_text):
    if some_text.replace(" ", "").isdigit() and len(some_text.replace(" ", "")) == 2:
        return True
    else:
        return False

def is_in_coords(some_text):
    if 1 <= int(some_text.replace(" ", "")[0]) <= 3 \
            and 1 <= int(some_text.replace(" ", "")[1]) <= 3:
        return True
    else:
        return False


# Deal with initial setup
create_init_state()
create_rows()
print_gameboard()

# setup game board
create_columns()
create_diags()
create_gameboard()

# Take in new X
while True:
    text_in = input("Enter the coordinates: ")
    if not is_two_digits(text_in):
        print("You should enter numbers!")

    elif not is_in_coords(text_in):
        print("Coordinates should be from 1 to 3!")

    elif is_two_digits(text_in) and is_in_coords(text_in):
        x, y = text_in.split()
        x = int(x)
        y = int(y)
        cell = (x - 1) + (9 - (3 * y))
        new_xy = num_matrix[cell]
        new_x = int(new_xy[0])
        new_y = int(new_xy[1])

        if rows[new_x][new_y] != "_":
            print("This cell is occupied! Choose another one!")
        elif rows[new_x][new_y] == "_":
            rows[new_x][new_y] = current_player
            create_columns()
            create_diags()
            create_gameboard()
            print_gameboard()
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
            break

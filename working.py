board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# Backtracking algorithm with recursion
def solve(board):

    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        # check if number inserted is valid num
        if valid_num(board, i, (row, col)):
            # if value added is valid, add to board
            board[row][col] = i

            # recursively solve the board until we try and find all the correct value on board
            # if we loop through all numbers and no nums are valid we will return false
            # if solve isnt true then we will then backtrack to previous value and reset value and try different value
            if solve(board):
                return True

            board[row][col] = 0
    
    return False



# Is the number given valid / correct or not
def valid_num(board, num, position):
    # Check row
    for i in range(len(board[0])):
        # check through each element in row is equal to number we have added in
        # if position we checking is the num we just inserted then ignore it
        if board[position[0]][i] == num and position[1] != i:
            return False
    
    # Check column
    for i in range(len(board)):
        # check if our current x (column) value is equal to the number we just inserted
        # if position we checking is the num we just inserted then ignore it
        if board[i][position[1]] == num and position[0] != i:
            return False
    
    # Check box
    box_x = position[1] // 3 #column
    box_y = position[0] // 3 #row

    for i in range(box_y * 3, box_x * 3 + 3):
        for j in range(box_x * 3, box_y * 3 + 3):
            if board[i][j] == num and (i, j) != num: # check the value we inserted and make sure it wasnt already added
                return False # return false if duplicate is found

    return True



# Visual output of board
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

print_board(board)

# find empty square/spaces we are trying to solve for
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])): # length of each row
            if board[i][j] == 0:
                return (i, j) # row, column
    return None # no blank squares

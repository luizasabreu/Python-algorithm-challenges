# Tic tac toe input
# 1:  X | O | X
#    -----------
# 2:    |   |  
#    -----------
# 3:  O |   |
#     A   B  C
# Imagine if your user enters "C1" and you need to see if there's an X or O in that cell on the board. 
# To do so, you need to translate from the string "C1" to row 0 and column 2 so that you can check board[row][column].
# Your task is to write a function that can translate from strings of length 2 to a tuple (row, column). 
# Name your function get_row_col; 
# it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.
# For example, calling get_row_col("A3") should return the tuple (2, 0) 
# because A3 corresponds to the row at index 2 and column at index 0 in the board.

board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]

def get_row_col(code):
    col = 0
    row = 0
    code_dict = {"A": 0,
                 "B": 1,
                 "C": 2
                 }
    for i in code:
        if i in code_dict.keys():
            col = code_dict[i]
        else:
            row = int(i)-1
    return (row, col)

print(get_row_col("A3"))


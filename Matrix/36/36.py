# IDEA
# to check if the sudoku is valid we need to check all rows, columns and 3x3 squares
# and return False if we find any duplicates or True if we don't
# To apply this idea we will create three helper functions to get rows, columns and 3x3 squares
# then we will iterate through all of them and check if there are any duplicates
# TIME COMPLEXITY
# The time complexity is O(1) because the board is always 9x9
# SPACE COMPLEXITY
# The space complexity is O(1) because we only need to use constant number of variables

from typing import List


def dot_ignore(t):
    return [num for num in t if num != "."]


def get_column(t_2, c_ind):
    return [row[c_ind] for row in t_2]


def get_row(t_2, r_ind):
    return t_2[r_ind]


def parse_to_one_dim(data):
    return [num for row in data for num in row]


def get_square(t_2, r_ind, c_ind):
    return parse_to_one_dim([row[c_ind:c_ind + 3] for row in t_2[r_ind:r_ind + 3]])


def check_corr(t):
    t = dot_ignore(t)
    return len(t) == len(list(set(t)))


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                if not check_corr(get_square(board, i, j)):
                    return False
        for i in range(9):
            if not check_corr(get_row(board, i)):
                return False
        for i in range(9):
            if not check_corr(get_column(board, i)):
                return False
        return True

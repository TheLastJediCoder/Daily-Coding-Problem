"""
This problem was asked by Slack.

You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the 
bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]

Return two, as there are only two ways to get to the bottom right:

    Right, down, down, right
    Down, right, down, right

The top left corner and bottom right corner will always be 0.
"""

test_case = [[0, 0, 1],
             [0, 0, 1],
             [1, 0, 0]]


def find_paths_to_bottom(matrix: list[list]) -> int:
    n = len(matrix)
    m = len(matrix[0])

    table = [[0 for j in range(m)] for i in range(n)]

    table[0][0] = 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                table[i][j] = 0
            elif i == 0 and j > 0:
                table[i][j] = table[i][j - 1]
            elif j == 0 and i > 0:
                table[i][j] = table[i - 1][j]
            elif i > 0 and j > 0:
                table[i][j] = table[i][j - 1] + table[i - 1][j]
    return table[n - 1][m - 1]


print(find_paths_to_bottom(test_case))

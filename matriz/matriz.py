from typing import List
import random


# We could work with numpy arrays, they are faster.
def create_matrix() -> List[List[int]]:
    """
    Creates a 5x5 randomized matrix with integers elements.
    >>> mat = create_matrix()
    >>> len(mat)
    5
    >>> all(isinstance(mat[i][j], int) for j in range(5) for i in range(5))
    True
    """
    return [[random.randint(1, 10) for j in range(5)] for i in range(5)]


def find_seq(matrix: List[List[int]]):
    """
    Finding sequences of four consecutive numbers in a 5x5 matrix horizontally and vertically.
    >>> mat = [[1, 2, 3, 4, 5], [2, 7, 3, 8, 2], [3, 5, 10, 3, 7], [4, 7, 10, 1, 8], [5, 5, 3, 7, 8]]
    >>> find_seq(mat)
    Horizontal sequence found: 1-4 at (0,0)-(0,3)
    Horizontal sequence found: 2-5 at (0,1)-(0,4)
    Vertical sequence found: 1-4 at (0,0)-(3,0)
    Vertical sequence found: 2-5 at (1,0)-(4,0)
    """
    hor_seq = [(i, j) for i in range(5) for j in range(2) if matrix[i]
               [j] == matrix[i][j+1]-1 == matrix[i][j+2]-2 == matrix[i][j+3]-3]
    ver_seq = [(i, j) for i in range(2) for j in range(5) if matrix[i]
               [j] == matrix[i+1][j]-1 == matrix[i+2][j]-2 == matrix[i+3][j]-3]

    for (i, j) in hor_seq:
        print(
            f"Horizontal sequence found: {matrix[i][j]}-{matrix[i][j+3]} at ({i},{j})-({i},{j+3})")

    for (i, j) in ver_seq:
        print(
            f"Vertical sequence found: {matrix[i][j]}-{matrix[i+3][j]} at ({i},{j})-({i+3},{j})")

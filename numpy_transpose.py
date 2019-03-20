"""
Program: numpy_transpose.py

Purpose: This example illustrates transpose of a matrix.

Study Material:

* https://www.khanacademy.org/math/linear-algebra/matrix-transformations/matrix-transpose/v/linear-algebra-transpose-of-a-matrix

Associated thoughts:

Why is Matrix Transpose useful?

* http://mathforum.org/library/drmath/view/71949.html

"""

import pprint

import numpy as np


def main():
    print("Simple Matrix.")
    mat = np.arange(9).reshape(3, 3)
    pprint.pprint(mat)

    print("----")

    print("Transpose of the Matrix.")
    transposed = np.transpose(mat)
    pprint.pprint(transposed)


if __name__ == '__main__':
    main()



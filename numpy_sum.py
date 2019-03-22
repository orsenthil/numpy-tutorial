"""
Axis is the dimension of the matrix. For the 2d matrix, we often say rows or columns instead of axis.
But when more than 2 dimensions are involved, we refer to them as axis.

According to numpy documentation, axes are defined for arrays with more than one dimension. A 2-dimensional array has
two corresponding axes: the first running vertically downwards across rows (axis 0), and the second running
horizontally across columns (axis 1).

Many operation can take place along one of these axes.
For example, we can sum each row of an array, in which case we operate along columns, or axis 1:

If you do .sum(axis=n), then dimension n is collapsed and deleted, with each value in the new matrix equal to the
sum of the corresponding collapsed values.

References

* https://docs.scipy.org/doc/numpy-1.13.0/glossary.html
* https://stackoverflow.com/questions/17079279/how-is-axis-indexed-in-numpys-array/17079437#17079437
"""


import numpy as np


def main():
    mat = np.arange(12).reshape((3, 4))
    print("Original Matrix:")
    print(mat)

    collapse_rows_with_sum = np.sum(mat, axis=1)
    print("Matrix Collapsed with Sum along the rows:")
    print(collapse_rows_with_sum)


if __name__ == '__main__':
    main()
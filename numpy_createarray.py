"""
A numpy array is a grid of values,

* All of the same type. (unlike python arrays which can be heterogenous).
* Is Indexed by a tuple of non negative integers.


The number of dimensions is the rank of the array;
the shape of an array is a tuple of integers giving the size of the array along each dimension.

Arrays can be initialized in variety of ways.

Reference

* http://cs231n.github.io/python-numpy-tutorial/
"""

import numpy as np


def main():
    print("Single Dimensional Array.")
    a = np.array([1, 2, 3])
    print(a)
    print("Two Dimensional Array.")
    a = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
    print(a)
    print("Array of Zeros")
    a = np.zeros((4, 5))
    print(a)
    print("Array of Ones")
    a = np.ones((3, 2, 3))
    print(a)
    print("Constant Array")
    a = np.full((1, 2, 3, 4), 5)
    print(a)
    print("Create an Identity Matrix")
    a = np.eye(4)
    print(a)
    print("Creating a Random Array")
    a = np.random.random((2, 5))
    print(a)



if __name__ == '__main__':
    main()
"""
Roll the specified axis backwards, until it lies in a given position.

start parameter denotes the axis which is rolled until it lies before this position.
The default, 0, results in a “complete” roll.

Reference:
https://docs.scipy.org/doc/numpy/reference/generated/numpy.rollaxis.html


What is an axis or How is axis indexed in numpy array?

the axis number of the dimension is the index of that dimension within the array's shape
* https://stackoverflow.com/a/17079437/18852


Why is rollaxis so confusing?
* https://stackoverflow.com/a/29903842/18852

"""

import numpy as np


def main():
    a = np.arange(8).reshape(4, 2, 1)
    print("shape")
    print(a.shape)
    print("rollaxis 0, 1, 2")
    print(np.rollaxis(a, 0).shape)
    print(np.rollaxis(a, 1).shape)
    print(np.rollaxis(a, 2).shape)
    print("rollaxis 0, start 1")
    print(np.rollaxis(a, 0, 1).shape)
    print("rollaxis 1, start 1")
    print(np.rollaxis(a, 1, 1).shape)
    print("rollaxis 2, start 1")
    print(np.rollaxis(a, 2, 1).shape)
    print("rollaxis 0, start 2")
    print(np.rollaxis(a, 0, 2).shape)
    print("rollaxis 1, start 2")
    print(np.rollaxis(a, 1, 2).shape)
    print("rollaxis 2, start 2")
    print(np.rollaxis(a, 2, 2).shape)

if __name__ == '__main__':
    main()
"""
Numpy linspace returns evenly spaced numbers over a specified interval.

We specify the start point, and the end point, and the total number points we want within that interval.
The linspace function will return those.


References
----------

* https://www.sharpsightlabs.com/blog/numpy-linspace/

"""

import numpy as np


def main():
    print("linspace from 0 to 100 of 5 values.")
    values = np.linspace(start=0, stop=100, num=5)
    print(values)
    print("linspace from 0 to 100 of 5 values, excluding the endpoint")
    values = np.linspace(start=0, stop=100, num=5, endpoint=False)
    print(values)
    print("linspace from 0 to 100 of 5 values, with return step.")
    values = np.linspace(start=0, stop=100, num=5, endpoint=False, retstep=True)
    print(values)


if __name__ == '__main__':
    main()
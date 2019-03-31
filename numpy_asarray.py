"""
asarray is a numpy numpy method to convert the input to an ndarray, but it does not copy the input if it is already an
ndarray.

"""

import numpy as np


def main():
    a = [1, 2, 3]
    out = np.asarray(a)
    print(out)

    a = np.array([1., 2, 3], dtype=np.float16)
    print(a)
    print(a.dtype)
    out = np.asarray(a, dtype=np.int32)
    print(out)
    print(out.dtype)


if __name__ == '__main__':
    main()
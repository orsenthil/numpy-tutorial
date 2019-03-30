"""
arange is an array-valued version of the built in python range function.
This can be used instead of linspace, but when using a non integer step, such as 0.1,
the results will often not be consistent. It is better to use `numpy.linspace` for these cases.
"""

import numpy as np


def main():
    out = np.arange(15)
    print(out)

    out = np.arange(15, dtype=np.float32)
    print(out)

    # When using a non-integer step, such as 0.1, the results will often not
    # be consistent.  It is better to use `numpy.linspace` for these cases.

    out = np.arange(0, 2, 0.1, dtype=np.float32)
    print(out)


if __name__ == '__main__':
    main()
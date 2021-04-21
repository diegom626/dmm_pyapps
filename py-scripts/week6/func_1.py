#!/usr/bin/env python


def multi(x, y, z=1):
    """

    :rtype: object
    """
    return x*y*z


a = multi(10, 25, 100)
b = multi(x=10, y=15, z=100)
c = multi(y=15, z=100, x=1)
d = multi(10, 2)
print a
print b
print c
print d

#!/usr/bin/env python

from __future__ import print_function

def looksay(number):
    """
    >> looksay("1")
    '11'
    >>> looksay("11")
    '21'
    >>> looksay("21")
    '1211'
    >>> looksay("1211")
    '111221'
    >>> looksay("111221")
    '312211'
    """
    result = []
    for d in number:
        if not result:
            result.append([1, d])
        elif d == result[-1][1]:
            result[-1] = [result[-1][0] + 1, d]
        else:
            result.append([1, d])
    return "".join("{0}{1}".format(*r) for r in result)

def test1():
    number = str(1113122113)
    for _ in range(40):
        number = looksay(number)
    print(len(number))  


def test2():
    number = str(1113122113)
    for _ in range(50):
        number = looksay(number)
    print(len(number))    


if __name__ == '__main__':
    from doctest import testmod
    testmod()
    test1()
    test2()

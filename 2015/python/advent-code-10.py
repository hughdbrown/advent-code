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
        if not result or d != result[-1][1]:
            result.append([1, d])
        else:
            result[-1][0] += 1
    return "".join("{0}{1}".format(*r) for r in result)


def test1(number, iterations):
    return number if not iterations else test1(looksay(number), iterations - 1)
    # for _ in range(iterations):
    #     number = looksay(number)
    #return number


if __name__ == '__main__':
    from doctest import testmod
    testmod()
    result = test1("1113122113", 40)
    print(len(result))
    result = test1(result, 10)
    print(len(result))

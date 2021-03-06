#!/usr/bin/env python
from __future__ import print_function

from collections import Counter, defaultdict
from string import lowercase


def double_letters(word):
    """
    >>> double_letters("aa")
    1
    >>> double_letters("aaa")
    1
    >>> double_letters("aba")
    0
    >>> double_letters("abba")
    1
    """
    # Index the word: letter-position
    d = defaultdict(list)
    for i, dd in enumerate(word):
        d[dd].append(i)

    # Make a dict of letter-consecutive letter counts
    s = {
        k: sum(i == j - 1 for i, j in zip(v, v[1:]))
        for k, v in d.items()
        if len(v) >= 2
    }
    # Only one double letter count per unique letter allowed. Seems to be th erule.
    return sum(v > 0 for v in s.values())


def good_password(password):
    """
    >>> good_password("hijklmmn")
    False
    >>> good_password("abbceffg")
    False
    >>> good_password("abbcegjk")
    False
    """
    # Check for forbidden letters
    s = set(password).intersection(set('iol'))
    if s:
        return False

    # Check for triple letters
    int_word = [ord(c) for c in password]
    if not any((c1, c2) == (c2 - 1, c3 - 1) for c1, c2, c3 in zip(int_word, int_word[1:], int_word[2:])):
        return False

    # Check for 2 or more double letters
    return double_letters(password) >= 2


def next_password(password):
    """
    >>> next_password('abcdefgh')
    'abcdefgi'
    >>> next_password('ghijklzz')
    'ghjaaaaa'
    """
    # Fast operation if forbidden letter found
    for c in "ilo":
        i = password.find(c)
        if i >= 0:
            j = lowercase.index(c) + 1
            return password[:i] + lowercase[j] + "a" * (8 - i - 1)

    # Increment last letter, rollover/carry if necessary
    for i in range(7, -1, -1):
        left, c, right = password[:i], password[i], password[i + 1:]
        if c == 'z':
            password = left + 'a' + right
        else:
            j = lowercase.index(c) + 1
            return left + lowercase[j] + right


def main1(password):
    """
    >>> main1("abcdefgh")
    'abcdffaa'
    >>> main1("ghijklmn")
    'ghjaabcc'
    """
    while not good_password(password):
        password = next_password(password)
    return password


if __name__ == '__main__':
    from doctest import testmod
    testmod()
    new_password = main1('hepxcrrq')
    print(new_password)
    new_password = main1(next_password(new_password))
    print(new_password)    

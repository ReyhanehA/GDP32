#!/usr/bin/env python3
# Evaluate an arithmetic expression
# jill-jenn vie et christoph durr - 2014-2015

# convert roman numbers

import sys

roman = [['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
         ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
         ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
         ['', 'M', 'MM', 'M'*3, 'M'*4,'M'*5,'M'*6,'M'*7,'M'*8,'M'*9]]


def roman2int(s):
    """Decode roman number

    :param s: string representing a roman number between 1 and 9999
    :returns: the decoded roman number
    :complexity: linear (if that makes sense for constant bounded input size)
    """
    val = 0
    pos10 = 1000
    beg = 0
    for pos in range(3, -1, -1):
        for digit in range(9,-1,-1):
            r = roman[pos][digit]
            if s.startswith(r, beg):
                beg += len(r)
                val += digit * pos10
                break
        pos10 //= 10
    return val


def int2roman(val):
    """Code roman number

    :param val: integer between 1 and 9999
    :returns: the corresponding roman number
    :complexity: linear (if that makes sense for constant bounded input size)
    """
    s = ''
    pos10 = 1000
    for pos in range(3, -1, -1):
        digit = val // pos10
        s += roman[pos][digit]
        val %= pos10
        pos10 //= 10
    return s

#! /usr/bin/env python2.7

import itertools

def answer(x, y, z):
    count = 0
    months_with_31 = (1, 3, 5, 7, 8, 10, 12)
    months_with_30 = (4, 6, 9, 11)
    months_with_28 = 2
    possibilities = set(itertools.permutations([x,y,z]))
    for possibility in possibilities:
        if possibility[0] in months_with_31 and possibility[1] <= 31:
            count += 1
            date = str(possibility[0]).zfill(2) + '/' + str(possibility[1]).zfill(2) + '/' + str(possibility[2]).zfill(2)
        elif possibility[0] in months_with_30 and possibility[1] <= 30:
            count += 1
            date = str(possibility[0]).zfill(2) + '/' + str(possibility[1]).zfill(2) + '/' + str(possibility[2]).zfill(2)
        elif possibility[0] == months_with_28 and possibility[1] <= 28:
            count += 1
            date = str(possibility[0]).zfill(2) + '/' + str(possibility[1]).zfill(2) + '/' + str(possibility[2]).zfill(2)
    if count == 1:
        return date
    else:
        return "Ambiguous"

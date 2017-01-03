#!/usr/bin/env python

import sys, os
import numpy as np


def maxsoftfunc(x):

    return np.exp(x) / np.sum(np.exp(x))

def main():

    array = [0.1, 1.1, 2.1]

    ans = maxsoftfunc(array)

    print(ans)


    total = 0
    for i in ans:

        total += i

    print(total)



if __name__=="__main__":
    main()

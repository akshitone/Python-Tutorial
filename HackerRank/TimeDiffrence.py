
import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.


def time_delta(t1, t2):
    #     Sun 10 May 2015 13:54:36 -0700
    #     Sun 10 May 2015 13:54:36 -0000
    #     Sat 02 May 2015 19:54:36 +0530
    #     Fri 01 May 2015 13:54:36 -0000
    time_format = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, time_format)
    t2 = datetime.strptime(t2, time_format)
    print((t1-t2).total_seconds())
    return str(int(abs((t1-t2).total_seconds())))


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

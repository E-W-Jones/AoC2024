from numpy import sign
from itertools import pairwise

def report_safe_undampened(report):
    print(report)
    s = 0
    for l, r in pairwise(report):
        d = r - l
        if s == 0:
            s = sign(d)
        if sign(d) != s:
            return False
        if not 1<=abs(d)<=3:
            return False
    return True

def report_safe(report, dampener=False):
    if not dampener:
        return report_safe_undampened(report)

    for i in range(len(report)+1):
        if report_safe_undampened([x for n, x in enumerate(report) if n != i]):
            return True
    return False


count = 0

with open('input.txt') as filein:
    for line in filein.readlines():
        report = [int(i) for i in line.rstrip('\n').split()]
        count += report_safe(report, dampener=True)
print(count)

#!/bin/python

import sys

def lowestTriangle(base, area):
    # Complete this function
    return int(round(((2*area)/base) + (area % base > 0)))

base, area = raw_input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
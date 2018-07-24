#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:49:26 2018

@author: Qiaoyi
"""

input_file = open('knapsack1.txt', 'r')
lines = []
for line in input_file:
    line = line.split()
    lines.append([int(line[0]), int(line[1])])
    
capacity = lines[0][0]
items = lines[1:]

subproblems = []
subproblems.append([0 for cap in range(capacity+1)])

for i, item in enumerate(items):
    subproblem = []
    for cap in range(capacity+1):
        subproblem.append(max(subproblems[i][cap], subproblems[i][cap-item[1]]
        +item[0] if cap-item[1] >=0 else 0))
    subproblems.append(subproblem)
    
print(subproblems[-1][-1])
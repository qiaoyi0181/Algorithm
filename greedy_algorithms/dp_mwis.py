#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 14:05:32 2018

@author: Qiaoyi
"""

weights_file = open('mwis.txt', 'r')
weights = []
for line in weights_file:
    weights.append(int(line))
weights = weights[1:]

n = len(weights)
max_weight_values = [0, weights[0]]

for i in range(2, n+1):
    max_weight_values.append(max(max_weight_values[i-1], max_weight_values[i-2]+weights[i-1]))
    
i = n
mwis = []
while i>=1:
    if max_weight_values[i-1] >= max_weight_values[i-2] + weights[i-1]:
        i -= 1
    else:
        mwis.insert(0, weights[i-1])
        i -= 2

checks = [1, 2, 3, 4, 17, 117, 517, 997]

check_result = ''

for check in checks:
    if weights[check-1] in mwis:
        check_result += '1'
    else:
        check_result += '0'
        
print('check result = '+check_result)
        

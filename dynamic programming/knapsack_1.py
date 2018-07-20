#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 16:28:25 2018

@author: Qiaoyi
"""

input_file = open('knapsack_big.txt', 'r')
values = []
weights = []

for line in input_file:
    line = line.split()
    values.append(int(line[0]))
    weights.append(int(line[1]))
    
weight_size = weights[0]
values = values[1:]
weights = weights[1:]

def knapsack(W, weight, value, n):
    if W == 0 or n == 0:
        return 0
    
    if weight[n-1] > W:
        return knapsack(W, weight, value, n-1)
    
    else:
        return max(knapsack(W, weight, value, n-1), 
                   value[n-1]+knapsack(W-weight[n-1], weight, value, n-1))
        
print(knapsack(weight_size, weights, values, len(values)))
    
    

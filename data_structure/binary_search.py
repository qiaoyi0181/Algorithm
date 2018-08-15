#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 12:06:57 2018

@author: Qiaoyi
"""
"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    left = 0
    right = len(input_array) - 1
    while left <= right:
        m = int((left+right)/2)
        if input_array[m] == value:
            return m
        elif input_array[m] > value:
            right = m - 1
        elif input_array[m] < value:
            left = m + 1
    return -1 

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 12:11:00 2018

@author: Qiaoyi
"""

"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def quicksort(array):
    less = []
    equal = []
    greater  = []
    if len(array) > 1:
        pivot = array[0]
        for i in array:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            elif i > pivot:
                greater.append(i)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)   

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 15:24:39 2018

@author: Qiaoyi
"""
import numpy as np
import sys
import gc
from itertools import combinations
import math

infinity = sys.maxint

def tsp(towns):
    n = len(towns)
    
    global binomials
    binomials = [[None for i in range(n+1)] for i in range(n+1)]
    
    a0 = np.zeros((n, binomial(n, n/2)), dtype=np.float32) #even m
    a1 = np.zeros((n, binomial(n, n/2)), dtype=np.float32) # odd m
    
    def a_(s, j):
        if j == 0:
            if len(s) == 1 and s[0] == 0:
                return np.float32(0.0)
            else:
                return np.float32(infinity)
        else:
            if len(s) % 2:
                return a0[j][index(s)]
            else:
                return a1[j][index(s)]
            
    def update_a(s, j, val):
        if len(s) % 2:
            a0[j][index(s)] = val
        else:
            a1[j][index(s)] = val
            
    for m in range(2, n+1):
        print('m = %i' % m)
        gc.collect()
        for s in combinations(range(n), m):
            if 0 not in s:
                continue
            for j in s:
                if j == 0:
                    continue
                update_a(s, j, min([a_(excluded(s, j), k) + dist(towns, k, j) for k in s if k != j]))
     
    return min([a_(range(n), j) + dist(towns, j, 0) for j in range(1, n)])

def dist(towns, i, j):
    return math.sqrt((towns[i][0]-towns[j][0])*(towns[i][0]-towns[j][0]) + (towns[i][1]-towns[j][1])*(towns[i][1]-towns[j][1]))

def index(s):
    res = 0
    for i in range(len(s)):
        res += binomial(s[i], i+1)
    return res

def excluded(lst, elem):
    return filter(lambda x: x != elem, lst)

def binomial(n, k):
    if n < k: return 0
    if binomials[n][k]: return binomials[n][k]
    ntok = 1
    for t in xrange(min(k, n-k)):
        ntok = ntok*(n-t)//(t+1)
    binomials[n][k] = ntok
    return ntok

def main():
    f = open('tsp.txt')
    n = int(f.readline())
    towns = [np.array([float(x) for x in line.split()], dtype=np.float32) for line in f]
    
    print tsp(towns)


main()












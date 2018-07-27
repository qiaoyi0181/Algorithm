#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 13:56:31 2018

@author: Qiaoyi
"""

import sys

infinity = sys.maxint

def floyd_warshall(n, edges):
    A = [[[infinity for i in range(n)] for i in range(n)] for i in range(2)]
    
    #Base cases
    for i in range(n):
        for j in range(n):
            if i == j:
                A[0][i][j] = 0
            elif ('%i,%i' % (i, j)) in edges:
                A[0][i][j] = edges['%i,%i' % (i, j)]
            else:
                A[0][i][j] = infinity
                
    #Dynamic programming
    for k in range(1, n+1):
        for i in range(n):
            for j in range(n):
                A[k % 2][i][j] = min(A[(k-1) % 2][i][j], A[(k-1) % 2][i][k-1] + A[(k-1) % 2][k-1][j])
                
    #Check for negative cycles
    for i in range(n):
        if A[n % 2][i][i] < 0:
            return None
        
    return A[n % 2]


def main():
    
    for i in [1,2,3]:
        print('Graph %i:' % i)
        f = open('g%i.txt' % i, 'r')
        n, m = [int(x) for x in f.readline().split()]
        edges = {}
        for line in f:
            u, v, w = [int(x) for x in line.split()]
            edges['%i,%i' % (u, v)] = w
        APSP = floyd_warshall(n, edges)
        if APSP is None:
            print('There is a negative cycle!')
        else:
            shortest = infinity
            for u in range(n):
                for v in range(n):
                    if APSP[u][v] < shortest:
                        shortest = APSP[u][v]
            print('Shortest shortest path: %i' % shortest)
            
main()
            






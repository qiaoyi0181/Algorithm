#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:51:26 2018

@author: Qiaoyi
"""
from heapq import heappop, heappush, heapify

weights_file = open('huffman.txt', 'r')

weights = []

for line in weights_file:
    weights.append(int(line))

weights = weights[1:]
    
heap = [[weight, ['']] for weight in weights]
heapify(heap)
while len(heap) > 1:
    lo = heappop(heap)
    hi = heappop(heap)
    for pair in lo[1:]:
        pair[0] = '0' + pair[0]
    for pair in hi[1:]:
        pair[0] = '1' + pair[0]
    heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
sorted_heap = sorted(heappop(heap)[1:], key=lambda p:(len(p[-1])))

min_length = len(sorted_heap[0][0])
max_length = len(sorted_heap[-1][0])

print('min length = ' + str(min_length))
print('max length = ' + str(max_length))




























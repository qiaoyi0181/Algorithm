#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:25:19 2018

@author: Qiaoyi
"""

from heapq import heappush, heappop, heapify
from collections import defaultdict

txt = "this is an example for huffman encoding"
symb2freq = defaultdict(int)
for ch in txt:
    symb2freq[ch] += 1
# in Python 3.1+:
# symb2freq = collections.Counter(txt)


    

"""Huffman encode the given dict mapping symbols to weights"""
heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
heapify(heap)
while len(heap) > 1:
    lo = heappop(heap)
    hi = heappop(heap)
    for pair in lo[1:]:
        pair[1] = '0' + pair[1]
    for pair in hi[1:]:
        pair[1] = '1' + pair[1]
    heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
print(sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p)))
 

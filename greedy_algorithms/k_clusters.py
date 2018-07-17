#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:35:47 2018

@author: Qiaoyi
"""

edges_file = open('clustering1.txt', 'r')

edges = []

for line in edges_file:
    line = line.split()
    try:
        edges.append([int(line[0]), int(line[1]), int(line[2])])
    except:
        pass
    
edges.sort(key=lambda x: x[2])

vertices = {}
for edge in edges:
    vertices[edge[0]] = edge[0]
    vertices[edge[1]] = edge[1]

costs = {}
for v in vertices:
    costs[v] = 0
    
num_clusters = len(vertices)

for edge in edges:
    head1 = vertices[edge[0]]
    while vertices[head1] != head1:
        head1 = vertices[head1]
        
    head2 = vertices[edge[1]]
    while vertices[head2] != head2:
        head2 = vertices[head2]
        
    if head1 != head2:
        if num_clusters <= 4:
            spacing = edge[2]
            break
        vertices[head2] = head1
        costs[head1] += (edge[2] + costs[head2])
        num_clusters -= 1
        
print(spacing)











#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:20:45 2018

@author: Qiaoyi
"""

jobs_file = open('jobs.txt', 'r')

weight = 0
length = 0
job = []

for line in jobs_file:
    line = line.split()
    try:
        weight = int(line[0])
        length = int(line[1])
        #job.append([weight, length, weight-length])
        job.append([weight, length, float(weight)/float(length)])
         
    except:
        pass

job = sorted(job, key=lambda x: (x[2]), reverse=True)  

sumLength = 0
sumTime = 0

for x in job:
    sumLength += x[1]
    sumTime += sumLength * x[0]
    
print(sumTime)
    

input_file = open('2sum.txt', 'r')

result = {}
dic = {}


for line in input_file:
	num = long(line)
	key = num/10000
	if key not in dic:
		dic[key] = {}
	if num in dic[key]:
		dic[key][num] += 1
	else:
		dic[key][num] = 1

input_file.close()

for key1 in dic:
	if key1 > 0:
		continue

	for key2 in range(-2-key1, 1-key1):
		if key2 in dic:
			for value2 in dic[key2]:
				for value1 in dic[key1]:
					if dic[key1][value1] != 1 or dic[key2][value2] != 1:
						continue
					sum_temp = value1 + value2

					if abs(sum_temp) <= 10000 and sum_temp not in result:
						result[sum_temp] = True


print(len(result))

# This method is way too slow...

'''
import sys

data = [int(num) for num in open('2sum.txt', 'r')]
targets = range(-10000, 10001)
h = {}
answers = {}

for num in data:
	h[num] = True

for num in data:
	for t in targets:
		if t-num in h:
			if num == t-num:
				continue
			if t not in answers:
				answers[t] = set([tuple(sorted([num, t-num]))])
			else:
				answers[t].add(tuple(sorted([num, t-num])))

print(len(answers))
'''



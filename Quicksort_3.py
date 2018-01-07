#numList = []
#for line in open('QuickSort.txt', 'r').readlines():
#    numList.append(int(line))

numList = [4,5,2,3,1]
#n = [2,1,12,13,16,10,9,5,18,8,17,20,19,3,4,11,14,6,7,15]

count_pivot_first = 0
count_pivot_second = 0
count_pivot_third = 0

#CASE I

def countComparsionWithFirst(n):
	global count_pivot_first
	if len(n) <= 1:
		return n
	else:
		count_pivot_first += len(n) - 1
		i = 0
		for j in range(len(n)-1):
			if n[j+1] < n[0]:
				n[i+1], n[j+1] = n[j+1], n[i+1]
				i += 1
		n[0], n[i] = n[i], n[0]
		first_part = countComparsionWithFirst(n[:i])
		second_part = countComparsionWithFirst(n[i+1:])
		first_part.append(n[i])
		return first_part + second_part

#CASE II

def countComparsionWithLast(n):

	global count_pivot_second
	if len(n) <= 1:
		return n
	else:
		count_pivot_second += len(n) - 1
		n[0], n[-1] = n[-1], n[0]  #The only difference with the previous one
		i = 0
		for j in range(len(n)-1):
			if n[j+1] < n[0]:
				n[i+1], n[j+1] = n[j+1], n[i+1]
				i += 1
		n[0], n[i] = n[i], n[0]
		first_part = countComparsionWithFirst(n[:i])
		second_part = countComparsionWithFirst(n[i+1:])
		first_part.append(n[i])
		return first_part + second_part


#CASE III

def middle_index(x):
    if len(x)%2 == 0:
        middle_index = len(x)/2 - 1
    else:
        middle_index = len(x)/2
    return middle_index

def median_index(x, i, j, k):
    if (x[i]-x[j])*(x[i]-x[k]) < 0:
        return i
    elif (x[j]-x[i])*(x[j]-x[k]) < 0:
        return j
    else:
        return k

def countComparsionWithMedian(n):
	global count_pivot_third
	if len(n) <= 1:
		return n
	else:
		count_pivot_third += len(n) - 1
		k = median_index(n, 0, middle_index(n), -1) #Difference with previous two
		if k != 0:
			n[0], n[k] = n[k], n[0]
		i = 0
		for j in range(len(n)-1):
			if n[j+1] < n[0]:
				n[i+1], n[j+1] = n[j+1], n[i+1]
				i += 1
		n[0], n[i] = n[i], n[0]
		first_part = countComparsionWithFirst(n[:i])
		second_part = countComparsionWithFirst(n[i+1:])
		first_part.append(n[i])
		return first_part + second_part

countComparsionWithFirst(numList)
countComparsionWithLast(numList)
countComparsionWithMedian(numList)

print(count_pivot_first)
print(count_pivot_second)
print(count_pivot_third)
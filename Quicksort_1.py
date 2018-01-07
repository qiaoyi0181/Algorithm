#compute the total number of comparisons used to sort 
#the given input file by QuickSort

n = []
for line in open('QuickSort.txt', 'r').readlines():
    n.append(int(line))

n = [4,5,2,3,1]
#n = [2,1,12,13,16,10,9,5,18,8,17,20,19,3,4,11,14,6,7,15]

count = 0

def partition(n, start, end):
    pivot = n[start]
    i = start + 1
    for j in range(start+1, end):
        if n[j] < pivot:
            n[i], n[j] = n[j], n[i]
            i += 1

    n[start], n[i-1] = n[i-1], n[start]
    return i - 1

def quicksort(n, start, end):
    if end - start <= 1:
        return 0
    else:
        n[start], n[end-1] = n[end-1], n[start] #uncomment for using the final one as the pivot
        split = partition(n, start, end)
        count = end - start - 1
        smaller = quicksort(n, start, split)
        bigger = quicksort(n, split+1, end)
        return count + smaller + bigger

print(quicksort(n, 0, len(n)))
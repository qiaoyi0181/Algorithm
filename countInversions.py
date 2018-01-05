with open('/Users/Qiaoyi/Desktop/sc_bcc_histogram/IntegerArray.txt') as f:
    numbers = f.readlines()

numbers = [int(x.strip()) for x in numbers]

count = 0

def countInversions(n):
    global count 

    midIndex = len(n)/2

    leftPart = n[:midIndex]
    rightPart = n[midIndex:]

    if len(n) > 1:

        countInversions(leftPart)
        countInversions(rightPart)

        i = 0
        j = 0

        a = leftPart
        b = rightPart

        for k in range(len(n) + 1):
            if a[i] < b[j]:
                n[k] = a[i]
                i += 1
                if i == len(a) and j != len(b):
                    while j != len(b):
                        k += 1
                        n[k] = b[j]
                        j += 1
                    break
            elif a[i] > b[j]:
                count += (len(a) - i)
                n[k] = b[j]
                j += 1
                if j == len(b) and i != len(a):
                    while i != len(a):
                        k += 1
                        n[k] = a[i]
                        i += 1
                    break
    return n

countInversions(numbers)
print(count)

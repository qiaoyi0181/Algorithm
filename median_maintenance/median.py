import heapq

f = [int(num) for num in open('Median.txt', 'r')]
h_low = []
h_high = []

sum = 0

for data in f:
	if len(h_low) > 0:
		if data > -h_low[0]:
			heapq.heappush(h_high, data)
		else:
			heapq.heappush(h_low, -data)
	else:
		heapq.heappush(h_low, -data)


	if len(h_low) > len(h_high) + 1:
		heapq.heappush(h_high, -heapq.heappop(h_low))
	elif len(h_high) > len(h_low):
		heapq.heappush(h_low, -heapq.heappop(h_high))

	sum += -h_low[0]

print(sum%10000)

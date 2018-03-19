data = open('dijkstraData.txt', 'r')
vertices = dict()
for line in data.readlines():
	tmp = line.split()
	vertices[int(tmp[0])] = {int(x.split(',')[0]):int(x.split(',')[1]) for x in tmp[1:]}
data.close()

length = 200
expend = [1]
nonexpend = list(range(2, length+1))
distance = {x:0 for x in range(1, length+1)}

while len(expend) < length:
	maxlimit = 1000000
	tmpdist = maxlimit
	lenvw = tmpdist
	for v in expend:
		for w in nonexpend:
			if w in vertices[v].keys():
				lenvw = distance[v] + vertices[v][w]
				if lenvw < tmpdist:
					tmpdist = lenvw
					tmpv = v
					tmpw = w
	if tmpdist == maxlimit: break
	expend.append(tmpw)
	nonexpend.remove(tmpw)
	distance[tmpw] = tmpdist

for num in [7,37,59,82,99,115,133,165,188,197]:
	print(str(distance[num]))
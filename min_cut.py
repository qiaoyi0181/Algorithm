import random
import sys

def readGraph(filename):
    vertices = []
    edges = set([])

    for line in open(filename):
        field = [int(f) for f in line.split()]
        vertex = field.pop(0)
        vertices.append(vertex)

        incident = [tuple(sorted([vertex, f])) for f in field]
        edges.update(incident)

    return vertices, list(edges)

def RandomContraction(vertices, edges):
    while len(vertices) > 2:
        edge = random.choice(edges)
        a, b = edge
        vertices.remove(b)
        new_edges = []

        for e in edges:
            if e == edge:
                continue
            if b in e:
                if e[0] == b:
                    other = e[1]
                if e[1] == b:
                    other = e[0]
                e = tuple(sorted([a, other]))
            new_edges.append(e)
        edges = new_edges

    return vertices, edges

vertices, edges = readGraph(sys.argv[1])

minimum = 100000
for i in range(0, 1000):
    v, e = RandomContraction(vertices[:], edges[:])
    #minimum = len(e)
    print(v, len(e))
    if len(e) < minimum:
        minimum = len(e)

print("min cut: %d" % minimum)




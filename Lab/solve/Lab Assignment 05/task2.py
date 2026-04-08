# task 2

fileopen = open("input2.txt", "r")
fileclose = open("output2.txt", "w")

import math
import heapq
line = fileopen.readline()
readline = int(line)
graph = {}

def Dij(graph, source):
    p_queue = []
    l = len(graph)
    prevNode = [None] * (l+1)
    traveled = [False] * (l+1)
    goal = [math.inf] * (l+1)
    goal[source] = 0

    for nodes in graph:
        heapq.heappush(p_queue, (goal[nodes], nodes))

    while (p_queue != []):
        out_val = heapq.heappop(p_queue)[1]
        if (traveled[out_val] == True):
            continue
        traveled[out_val] = True
        
        for i in graph[out_val]:
            a = goal[out_val]+i[1]
            if (a < goal[i[0]]):
                goal[i[0]] = a
                prevNode[i[0]] = out_val
                heapq.heappush(p_queue,(goal[i[0]],i[0]))
    re_goal = goal[-1]
    return re_goal

######################################################################

for i in range(readline):
    readline = fileopen.readline().split()
    n,e = int(readline[0]), int(readline[1])

    for i in range(1, n+1):
        graph[i] = []
        
    for i in range(e):
        readline = fileopen.readline().split()
        out_val1 = readline[0]
        nn1 = readline[1]
        ee1 = readline[2]
        out_val,nn,ee = int(out_val1),int(nn1),int(ee1)

        graph[out_val].append((nn, ee))
        graph[nn].append((out_val, ee))

    l = len(graph)
    if (l == 0):
        fileclose.write(str(0)  +  " ")
    else:
        fileclose.write(str(Dij(graph, 1))   +  " ")

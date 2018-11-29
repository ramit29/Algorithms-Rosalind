#!/usr/bin/env python3

f = open("kshv.sif","r")
connected_nodes=[]
for i in f:
    i=i.strip("\n").split("\t")
    connected_nodes.append([i[0],i[2]])
def adjacency_list(list):
    dict={}
    for i in list:
        if i[0] not in dict.keys():
            dict[i[0]]=[i[1]]
        else:
            dict[i[0]].append(i[1])
        if i[1] not in dict.keys():
            dict[i[1]]=[i[0]]
        else:
            dict[i[1]].append(i[0])




    return dict
adj_list=adjacency_list(connected_nodes)

def bfs(adlist,start):
    visited=[]
    queue=[start]
    while queue:
        vertex=queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            edges=adlist[vertex]
            for i in edges:
                queue.append(i)
    return visited
print(bfs(adj_list,"kshv_ORFK9"))

#!/usr/bin/env python3
#requires graph represented as an adjacency list

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


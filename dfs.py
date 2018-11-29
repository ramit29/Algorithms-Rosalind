#!/usr/bin/env python3

#works on dictionary functioning as an adjacency list
def dfs(adlist,start):
    visited=[]
    queue=[start]
    while queue:
        vertex=queue.pop(-1)
        if vertex not in visited:
            visited.append(vertex)
            edges=adlist[vertex]
            for i in edges:
                queue.append(i)
    return visited
print(dfs(adj_list,"kshv_ORFK9"))

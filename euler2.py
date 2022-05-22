#!/usr/bin/python3

def eulerCycle(G, start): # G = graph (dictionary)
    path = [start]
    #construct a set of all edges in graph:
    edgesRemaining = set()
    for n in G.keys():
        for neighbor in G[n]:  # neighbor is a neighbor of node.
            edgesRemaining.add((n,neighbor))
    n = start
    while len(edgesRemaining)!=0:
        for neighbor in G[n]:
            edge = (n,neighbor)
            if edge in edgesRemaining:
                edgesRemaining.remove(edge)
                path.append(neighbor)
                break
        n = neighbor
        print(neighbor, edgesRemaining,path)
    return path

print(eulerCycle({0:[1],1:[0]}, 1))

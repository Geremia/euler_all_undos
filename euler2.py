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
                G[n].remove(neighbor)
                path.append(neighbor)
                if G[n] == []:
                    G.pop(n)
                    n = list(G.keys())[0]
                else:
                    n = neighbor
                break
        print(neighbor, edgesRemaining,path)
    return path
#print(eulerCycle({0:[3], 1:[0], 2:[1,6], 3: [2], 4: [2], 5: [4], 6: [5,8], 7: [9], 8: [7], 9:[6]},6))
print(eulerCycle({0:[1],1:[0,2],2:[1,0]}, 0))
